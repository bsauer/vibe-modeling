# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Read AGENTS.md first

`AGENTS.md` is the canonical host policy and overrides everything else, including
`agentic-pipelines/AGENTS.md` (the pinned upstream framework submodule). This file
only summarizes commands and architecture; do not treat it as a policy substitute.
Key rules that most often bite:

- **Plan-governed work.** Substantial changes need an approved plan in
  `plans/current/` (check `plans/current/index.md`). Mark items `[x]`/`[?]`/`[-]`,
  regenerate indexes, and archive finished plans to `plans/past/`.
- **No kanban.** Never create kanban artifacts even if upstream framework docs suggest them.
- **Never edit `agentic-pipelines/`.** Update it only via the submodule-update playbook.
- **Docs move with code.** Update README, playbooks, references, and today's
  `journal/YYYY-MM-DD.md` in the same task. Journal "Today's Intentions" and
  "Notes / Reflections" are user-only.
- **Git.** Ask before committing or pushing. Push to `origin` (the personal fork),
  never `upstream`. Generated `output/` and `revisions/` artifacts are committed.
- **Completion summaries** must report plan status, structural-join status,
  minimum edge/material width status, and build/audit details (AGENTS.md §12).

## Environment and commands

Python 3.13 via uv (`uv sync`); run project Python with `uv run`. OpenSCAD must be
on `PATH` or passed with `--openscad-path`.

```bash
# Tests (stdlib unittest, tests/ add scripts/ to sys.path)
uv run python -m unittest discover -s tests
uv run python -m unittest tests.test_scad_build_views.ScadBuildViewTests.<test_name>

# Plan indexes (after any plan change; --check to verify)
uv run python scripts/regenerate_plan_indexes.py --repo-root .
uv run python scripts/regenerate_plan_indexes.py --check --repo-root .

# Multipart design (has designs/<d>/parts.json): complete build, then audit
uv run python scripts/scad_build_all.py --design <d> --config designs/<d>/configs/rev_000N.json
uv run python scripts/scad_build_all.py --design <d> --config designs/<d>/configs/rev_000N.json --audit-only

# Rebuild every stale multipart design (same as VS Code "Rebuild stale CAD designs")
uv run python scripts/rebuild_stale_designs.py --all

# Single-part design (no parts.json); --dry-run prints commands only
uv run python scripts/scad_build.py --design <d> --config designs/<d>/configs/rev_000N.json

# Assembly contract and supplementary assembly review (after build + audit pass)
uv run python scripts/validate_cad_assembly_contract.py --design <d>
uv run python scripts/scad_render_assembly_review.py --design <d> --config <cfg> --set full
uv run python scripts/scad_render_assembly_review.py --design <d> --config <cfg> --set full --audit-only

# Publish an immutable numbered revision (never reuse a published number;
# --dry-run still writes config and revision files)
uv run python scripts/scad_new_revision.py --design <d> --base-config designs/<d>/configs/rev_000N.json
```

Prefer `rebuild_stale_designs.py` for routine rebuilds rather than hand-running
OpenSCAD. README examples reference `example_box`, which no longer exists in
`designs/`; substitute a real design such as `cyberdeck-2`.

## Architecture

**Design layout.** Each `designs/<design>/` holds `src/main.scad` (CLI entrypoint,
selects a part by numeric `part_id`), geometry modules in `src/parts/` and
`src/lib/`, versioned parameter sets in `configs/rev_000N.json`, and for multipart
designs `parts.json` (authoritative export list) plus `assembly.json` (product,
subassembly, and interface contract, validated against `parts.json`). Config JSON
values become OpenSCAD `-D` defines.

**Build pipeline (`scripts/`).** `scad_build.py` renders one part to STL plus a fixed
set of 16 view PNGs and fails if any is missing. `scad_build_all.py` drives it per
`parts.json` entry, stages inside `output/<design>/`, checks the exact expected file
set, writes `build_manifest.json` with config, parts-manifest, source-tree, Git,
and artifact hashes, then atomically promotes a flat directory. `--audit-only`
re-verifies those hashes and is the only proof that an output is current.
`rebuild_stale_designs.py` compares design-tree mtimes against the installed
manifest and reuses its `config.path`. `scad_render_assembly_review.py` produces
an assembly STL, review PNGs, and `assembly_review_manifest.json` bound to the
build manifest hash; it must run only after a passing complete build.

**Artifact destinations are fixed.** `output/<design>/` is the only mutable
destination and must end flat with no `.scad` files or staging directories.
`revisions/<design>/rev_000N/` is immutable. Never create `output/<design>_rev_*`.

**Structural CAD rules** (AGENTS.md §10) apply to all geometry: each design defines
`minimum_wall_thickness` and `minimum_structural_overlap` (overlap ≥ wall), joins
need real positive-volume overlap guarded by `assert()`, and a clean render does not
prove structure. The structural-joins playbook is mandatory for load-bearing work.

**Knowledge base.** `playbooks/` holds task workflows indexed in AGENTS.md §6;
pick the matching one before CAD work. `references/engineering/` holds versioned
specs (ten-inch rack, servos, Apple device envelopes, joint standards) and
`references/tooling/` holds printer, slicer, and filament notes.
`docs/solarpunk_series.md` is the single source of truth for every `solarpunk_*`
design and must be updated whenever one changes.
