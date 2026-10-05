"""Minimal nested YAML reader — enough for library records, no dependencies.

Replaces the two-level parser in bin/validate, which silently flattened
`relations: {see_also: [...]}` into a list and made every crosswalk edge
disappear. Handles arbitrary nesting of block maps and block sequences,
which is all these records use.

Not a YAML implementation. No anchors, flow collections, multi-line scalars
or tags — the record schema forbids all of them anyway.
"""


def _strip_comment(v):
    """Drop a trailing ` # comment`, as YAML does for plain scalars.

    A quoted scalar keeps everything inside its quotes; a `#` not preceded by
    whitespace (a URL fragment, `#R-0001`) is not a comment.
    """
    v = v.strip()
    if v and v[0] in "\"'":
        q, i = v[0], 1
        while i < len(v):
            if q == '"' and v[i] == "\\":
                i += 2
                continue
            if v[i] == q:
                if q == "'" and v[i + 1:i + 2] == "'":
                    i += 2
                    continue
                rest = v[i + 1:].strip()
                # Only a comment may follow a closing quote; anything else
                # means this was not one quoted scalar, so leave it intact.
                return v[:i + 1] if not rest or rest.startswith("#") else v
            i += 1
        return v
    if v.startswith("#"):
        return ""
    for i in range(1, len(v)):
        if v[i] == "#" and v[i - 1] in " \t":
            return v[:i].rstrip()
    return v


def _scalar(v):
    v = _strip_comment(v)
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v == "[]":
        return []
    if v == "{}":
        return {}
    return v


def parse(text):
    root = {}
    # stack of (indent, container); container is dict or list
    stack = [(-1, root)]
    pending_key = None          # (indent, dict, key) awaiting a nested block
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        raw_e = raw.expandtabs(2)
        indent = len(raw_e) - len(raw_e.lstrip())
        line = raw.strip()

        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        cur = stack[-1][1]

        if pending_key and indent > pending_key[0]:
            d, k = pending_key[1], pending_key[2]
            cur = [] if line.startswith("- ") else {}
            d[k] = cur
            stack.append((indent, cur))
            pending_key = None
        elif pending_key:
            pending_key = None

        if line.startswith("- "):
            item = _strip_comment(line[2:])
            if not isinstance(cur, list):
                continue
            if ":" in item and not item.startswith(("http", "\"", "'")):
                k, _, v = item.partition(":")
                d = {k.strip(): _scalar(v)}
                cur.append(d)
                # A sequence item that is a map: its remaining keys sit at the
                # indent of this first key, so push the dict so they attach to
                # it rather than being dropped. Without this, every list of
                # multi-key maps silently collapses to its first key.
                stack.append((indent + 2, d))
                if not v:
                    pending_key = (indent + 2, d, k.strip())
            else:
                cur.append(_scalar(item))
        elif ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), _strip_comment(v)
            if not isinstance(cur, dict):
                continue
            if v:
                cur[k] = _scalar(v)
            else:
                cur[k] = {}
                pending_key = (indent, cur, k)
    return root
