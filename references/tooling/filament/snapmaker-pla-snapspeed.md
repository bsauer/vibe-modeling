# Snapmaker PLA SnapSpeed

Used with Snapmaker U1 + Snapmaker Orca in this workspace (including SnapSpeed
Black). Provenance: 2026-10-21 / 2026-10-22 sessions; see
`references/tooling/README.md`.

## Profile pairing

- Prefer the filament profile **Snapmaker PLA SnapSpeed @U1** with process
  **0.20 mm High Quality @Snapmaker U1 (0.4 nozzle)** unless detail requires
  another nozzle/process.
- Match the loaded tool color in Orca to the physical spool (for example Black
  on the active single-extruder slot).

## Temperature bands (session / published range used)

| Parameter | Guidance |
|---|---|
| Nozzle | **210–230 °C** high-speed band; **220 °C** used successfully |
| Bed | Published useful range cited as **25–60 °C**; Tg noted near **~59 °C** |
| Textured PEI start point | **55 °C** (avoid 65 °C soft first layers / extra elephant foot) |

Elephant-foot compensation around **0.15 mm** was already appropriate in the
reviewed stand project; lowering bed heat is preferred over stacking more
compensation when SnapSpeed is over-heated on PEI.

## Drying

If the spool has been open, dry before critical cosmetic or thin-feature prints.
Session note: about **55 °C for ~6 hours** per Snapmaker guidance referenced in
review. Moisture shows up as fuzzy walls and weak layer bonds (especially thin
rings).

## Process hygiene

- Fan: **100%** after the first layer is normal for this PLA family in the
  reviewed projects.
- Single-color jobs: disable prime/wipe tower.
- Do not carry Bambu filament/printer project keys into Snapmaker Orca projects
  (see `references/tooling/slicers/snapmaker-orca.md`).
