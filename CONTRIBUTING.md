# Contributing to library/

Workflow, branch rules, worktrees, and PR discipline live in the **m-of-n**
repo's `CONTRIBUTING.md`. They apply here identically.

Library-specific:

1. `bin/ingest <type> <source>` — never hand-create a record directory.
2. Fill `distilled.md` before setting `status: distilled`. CI rejects TODOs at
   that status.
3. Run `bin/validate && bin/export` before opening a PR. Commit the regenerated
   `exports/`.
4. One topic per branch. Topics are sized so branches do not collide.
5. Never commit a PDF, spreadsheet, or ebook. CI rejects it.

## Bumping the pin in mofn/

Merging here does not change anything in `mofn/` until the submodule pin moves:

```sh
cd ../mofn && bin/lib-sync --update
```

That is deliberate. A report cites `library@<commit>`, so the bibliography a
report was written against cannot shift underneath it.
