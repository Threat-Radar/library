#!/usr/bin/env python3
"""Recompute every test vector in expected.yaml from the Annex E, G and H data files.

Derived by the library (not part of ISO/SAE 21434). Run from the repository root:

    python3 -I records/iso/iso-sae-21434-2021/distilled/examples/run-fixtures.derived.py

Exits 1 and lists the cases if any computed result differs from expected.yaml.
"""
from __future__ import annotations

import pathlib
import sys
from decimal import ROUND_HALF_UP, Decimal

import yaml

HERE = pathlib.Path(__file__).resolve().parent


def load(name: str) -> dict:
    return yaml.safe_load((HERE / name).read_text(encoding="utf-8"))


cal = load("annex-e-cal.yaml")
feas = load("annex-g-feasibility.yaml")
tara = load("annex-h-headlamp-tara.yaml")
expected = load("expected.yaml")

RATINGS = ["very_low", "low", "medium", "high"]
failures: list[str] = []
checked = 0


def check(label: str, got, want) -> None:
    global checked
    checked += 1
    if got != want:
        failures.append(f"{label}: computed {got!r}, expected {want!r}")


# Table G.7: attack potential sum -> rating
def potential_rating(total: int) -> str:
    for band in feas["attack_potential"]["mapping"]["bands"]:
        if total >= band["from"] and (band["to"] is None or total <= band["to"]):
            return band["rating"]
    raise ValueError(total)


for case in expected["attack_potential_mapping"]["cases"]:
    check(f"G.7 sum {case['sum']}", potential_rating(case["sum"]), case["rating"])

# Table G.6 values summed for the Table H.7 paths
factor_values = {
    name: {lvl["level"]: lvl["value"] for lvl in factor["levels"]}
    for name, factor in feas["attack_potential"]["factors"].items()
}
h7 = {row["path"]: row for row in tara["feasibility_by_attack_potential"]["ratings"]}
for case in expected["attack_potential_paths"]["cases"]:
    total = sum(factor_values[f][lvl] for f, lvl in case["levels"].items())
    check(f"H.7 {case['path']} sum", total, case["sum"])
    check(f"H.7 {case['path']} sum vs annex", total, h7[case["path"]]["value"])
    check(f"H.7 {case['path']} rating", potential_rating(total), case["rating"])
    check(f"H.7 {case['path']} rating vs annex", potential_rating(total), h7[case["path"]]["rating"])
    for f, lvl in case["levels"].items():
        check(f"H.7 {case['path']} {f}", factor_values[f][lvl], h7[case["path"]][f])

# G.3 formula and Table G.8, with CVSS v3.1 metric values (scope unchanged)
cv = expected["cvss_exploitability"]
lo, hi = (Decimal(str(x)) for x in feas["cvss_exploitability"]["ranges"]["E"])


def exploitability(vector: str) -> Decimal:
    parts = dict(p.split(":") for p in vector.split("/"))
    e = Decimal("8.22")
    for metric in ("AV", "AC", "PR", "UI"):
        e *= Decimal(str(cv["metric_values"][metric][parts[metric]]))
    return e.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def cvss_rating(e: Decimal) -> str:
    for band in feas["cvss_exploitability"]["mapping"]:
        if Decimal(str(band["from"])) <= e <= Decimal(str(band["to"])):
            return band["rating"]
    raise ValueError(e)


for case in cv["cases"]:
    e = exploitability(case["vector"])
    check(f"G.3 {case['vector']} E", e, Decimal(str(case["E"])))
    check(f"G.3 {case['vector']} E within the annex range", lo <= e <= hi, True)
    check(f"G.8 {case['vector']} rating", cvss_rating(e), case["rating"])

# Table G.9 against Table H.6
g9 = {lvl["vector"]: lvl["rating"] for lvl in feas["attack_vector"]["levels"]}
h6 = {row["path"]: row for row in tara["feasibility_by_attack_vector"]["ratings"]}
for case in expected["attack_vector_ratings"]["cases"]:
    check(f"G.9 {case['vector']}", g9[case["vector"]], case["rating"])
    check(f"H.6 {case['path']} vs G.9", h6[case["path"]]["rating"], g9[h6[case["path"]]["vector"]])
    check(f"H.6 {case['path']}", h6[case["path"]]["rating"], case["rating"])

# Table H.8, and the Table H.10 formula across the whole grid
matrix = tara["risk_matrix"]
cols = matrix["columns"]


def matrix_risk(impact: str, feasibility: str) -> int:
    return matrix["rows"][impact][cols.index(feasibility)]


formula = tara["risk_formula"]


def formula_risk(impact: str, feasibility: str):
    r = 1 + formula["impact_values"][impact] * formula["feasibility_values"][feasibility]
    return int(r) if float(r).is_integer() else r


for case in expected["risk_matrix"]["cases"]:
    check(f"H.8 {case['impact']}/{case['feasibility']}", matrix_risk(case["impact"], case["feasibility"]), case["risk"])

agree, disagree = 0, []
for impact in matrix["rows"]:
    for feasibility in cols:
        f, m = formula_risk(impact, feasibility), matrix_risk(impact, feasibility)
        if f == m:
            agree += 1
        else:
            disagree.append({"impact": impact, "feasibility": feasibility, "formula": f, "matrix": m})
fm = expected["risk_formula_vs_matrix"]
check("H.10 vs H.8 agreeing cells", agree, fm["agreeing_cells"])
key = lambda d: (d["impact"], d["feasibility"])  # noqa: E731
check("H.10 vs H.8 disagreeing cells", sorted(disagree, key=key), sorted(fm["disagreeing_cells"], key=key))

# Table H.9: worst path per threat scenario, then Table H.8 and the formula
ratings_by_path = {**{p: r["rating"] for p, r in h6.items()}, **{p: r["rating"] for p, r in h7.items()}}
h9 = {row["threat"]: row for row in tara["risk_values"]["items"]}
for case in expected["risk_values"]["cases"]:
    worst = max((ratings_by_path[p] for p in case["paths"]), key=RATINGS.index)
    check(f"H.9 {case['threat']} aggregated", worst, case["aggregated_feasibility"])
    check(f"H.9 {case['threat']} aggregated vs annex", worst, h9[case["threat"]]["aggregated_feasibility"])
    check(f"H.9 {case['threat']} matrix risk", matrix_risk(case["impact"], worst), case["matrix_risk"])
    check(f"H.9 {case['threat']} formula risk", formula_risk(case["impact"], worst), case["formula_risk"])
    check(f"H.9 {case['threat']} risk vs annex", matrix_risk(case["impact"], worst), h9[case["threat"]]["risk"])

# Table E.1
e1 = cal["cal_by_impact_and_attack_vector"]
for case in expected["cal_lookup"]["cases"]:
    got = e1["rows"][case["impact"]][e1["columns"].index(case["vector"])]
    check(f"E.1 {case['impact']}/{case['vector']}", got, case["cal"])

if failures:
    print(f"{len(failures)} of {checked} checks FAILED:")
    for line in failures:
        print("  " + line)
    sys.exit(1)
print(f"all {checked} checks pass")
