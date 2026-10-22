# Tooling References

Shared knowledge about printers, slicers, filament, and CAD applications used
with this host. Design-specific slice forks and change lists stay under
`designs/<design>/`. Playbooks stay under `playbooks/` and should cite these
notes when they need machine or slicer facts.

## Layout

```text
references/tooling/
  printers/          # make / model beds, nozzles, process baselines
  slicers/           # applications, 3MF portability, UI workflows
  filament/          # material profiles and drying / temp bands
  cad/               # CAD applications (placeholder until populated)
```

## Current inventory

| Path | Status |
|---|---|
| `printers/snapmaker/u1.md` | Snapmaker U1 bed, clearance, nozzle time tradeoffs |
| `slicers/snapmaker-orca.md` | Snapmaker Orca 3MF pitfalls, scarf enum, paint workflows |
| `filament/snapmaker-pla-snapspeed.md` | Snapmaker PLA SnapSpeed temps and drying |
| `cad/` | Empty — no CAD-app facts captured from the source sessions yet |

## Provenance

Initial content was distilled from workspace print sessions recorded in agent
transcripts [iPhone Duo plate trim](ca6aa2d4-451f-4406-9bf4-6d5baa660a69) and
[Duo stand Orca review](ab7b0a54-df61-425e-adf0-49fc83433f37) (2026-10-21 /
2026-10-22). Prefer measured or vendor-published values when they conflict with
session notes; mark unresolved items as assumptions.

## Rules

1. Keep entries **reusable**. Put one-off design numbers in the design README or
   change list; link here for the general rule.
2. Prefer **make/model** paths for printers (`printers/<vendor>/<model>.md`).
3. Prefer **application** paths for slicers and CAD tools.
4. Do not edit `agentic-pipelines/` for host tooling notes.
5. Host `AGENTS.md` and CAD playbooks override conflicting tooling defaults when
   they set structural or artifact policy.
