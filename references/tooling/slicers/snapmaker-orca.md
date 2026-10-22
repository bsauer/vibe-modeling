# Snapmaker Orca

Snapmaker’s Orca-based slicer used with the Snapmaker U1 in this workspace.
Provenance: 2026-10-21 / 2026-10-22 print sessions; see
`references/tooling/README.md`.

## Opening foreign 3MF projects

A 3MF may embed another vendor’s printer project. Opening a **Bambu Lab A2L**
project inside Snapmaker Orca produced rejection warnings for:

- Relative extruder distances without an expected `G92 E0` reset
  (`use_relative_e_distances`)
- `prime_tower_brim_width: -1`

**Mitigation:** save a **model-only** 3MF (mesh + placement, no foreign printer
profile) and apply Snapmaker U1 / SnapSpeed profiles in Orca. Geometry can be
unchanged while the project keys are stripped.

Do not assume a 3MF that slices cleanly in Bambu Studio / Bambu Orca will open
cleanly in Snapmaker Orca.

## Scarf joint seam enum (encoding trap)

UI path: **Process → Quality → Seam → Scarf joint seam (beta)**.

Orca / Snapmaker Orca store `seam_slope_type` as
`SeamScarfType { None, External, All }`:

| UI label | Meaning | Valid 3MF / config value |
|---|---|---|
| **None** | No scarf | `none` |
| **Contour** | Scarf outer silhouette only; **holes not scarfed** | `external` |
| **Contour and hole** | Scarf outer silhouette **and** hole walls | `all` |

**Do not** write the UI word `contour` into `seam_slope_type`. Snapmaker Orca
rejects it and rewrites the setting to `none`, showing a compatibility dialog
such as: ``seam_slope_type` (`contour`) was replaced with `none``.

Practical choice for press-fit bores:

- Prefer **Contour** (`external`) when hole diameter accuracy matters.
- Use **Contour and hole** (`all`) after a fit print if bore seams still look
  harsh and the puck still seats.

In at least one Snapmaker Orca build, `has_scarf_joint_seam` was **not** the
primary on/off switch; `seam_slope_type` controlled scarf enablement.

## Support painting (tree supports)

Typical workflow for parts with a local overhang and a keep-clear cavity:

1. Enable **tree(auto)** supports in Process → Support.
2. Open **Support painting** on the top toolbar.
3. **Support enforcer** (green): paint ceilings / crowns that must be supported.
4. **Support blocker** (red): paint press-fit bores, cable notches, and faces
   that must stay empty.
5. Prefer **build-plate-only** trees when the overhang can still be reached;
   re-slice and inspect preview until the cavity stays hollow.

## Seam painting

1. Global seam **Aligned** (or as required).
2. **Seam painting**: enforce a vertical band on a **hidden** face; optionally
   block show faces.
3. Slice and confirm seam dots in Preview sit on the painted rear / hidden side.

## Functional PLA baseline (0.4 mm, High Quality)

Stock **0.20 mm High Quality @Snapmaker U1 (0.4 nozzle)** is a good cosmetic
starting point but is often too light for load-bearing stands (phones, MagSafe
torque). Session recommendation pattern:

| Lever | Prototype-ish stock | Stronger functional target |
|---|---|---|
| Walls | 2 | **3** (4 if pillar flexes) |
| Infill | 15% grid | **20–25% gyroid** (or cubic) |
| Bottom shells | 3 | **4–5** |
| Only one wall top | on | **off** for better top faces |
| Bed (SnapSpeed / textured PEI) | 65 °C | **55–60 °C** (try 55 first) |
| Supports | off | **on** when rings / ceilings overhang |
| Prime tower | on (multi-tool default) | **off** for single color |
| Outer / top speed | 60 / 150 mm/s | **60–80 / 120–150 mm/s** |

Keep nozzle near **220 °C** with SnapSpeed (see filament note). Design-specific
encoded forks belong beside the design (for example
`designs/iphone-duo/.../snapmakeru1-recommended-CHANGE_LIST.md`).

## Related

- Printer: `references/tooling/printers/snapmaker/u1.md`
- Filament: `references/tooling/filament/snapmaker-pla-snapspeed.md`
