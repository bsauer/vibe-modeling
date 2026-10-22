# Snapmaker U1 recommended fork — change list

Source: `Duo Desk Stand with watch charger-snapmakeru1.3mf`  
Fork: `Duo Desk Stand with watch charger-snapmakeru1-recommended.3mf`  
Machine: Snapmaker U1 · Nozzle: 0.4 mm · Filament: Snapmaker PLA SnapSpeed Black

Open the **recommended** 3MF in Snapmaker Orca, complete the manual steps below, then slice.

## Encoded in the forked 3MF

| Setting | Was | Now | Why |
|---|---|---|---|
| `wall_loops` | `2` | `3` | Functional desk stand strength (phones + MagSafe torque) |
| `sparse_infill_density` | `15%` | `20%` | Stronger base/pillar without heavy time cost |
| `sparse_infill_pattern` | `grid` | `gyroid` | Isotropic strength; less grid resonance artifacts |
| `bottom_shell_layers` | `3` | `5` | Stiffer base + better underside finish under tray |
| `top_shell_layers` | `5` | `5` | Keep solid MagSafe face / tray tops |
| `only_one_wall_top` | `1` | `0` | Better top-surface quality on MagSafe face and tray |
| `enable_support` | `0` | `1` | Watch-ring ceiling/overhangs need support |
| `support_type` | `tree(auto)` | `tree(auto)` | Minimal scarring vs normal supports |
| `support_threshold_angle` | `30` | `40` | Allow steeper self-support; focus supports on ring |
| `support_on_build_plate_only` | `0` | `1` | Prefer ground-rooted trees; less trapped support in MagSafe cavity |
| `enable_prime_tower` | `1` | `0` | Single-color black print — tower wastes time/filament |
| `has_scarf_joint_seam` | `0` | `0` | Legacy/companion flag; scarf type is controlled by `seam_slope_type` in this Orca build |
| `seam_slope_type` | `none` | `external` | UI label **Contour** (see Scarf section below). Not the string `contour` — that value is invalid here |
| `outer_wall_speed` | `["60", "60"]` | `["80", "80"]` | Slight efficiency bump; still HQ-looking |
| `top_surface_speed` | `["150", "150"]` | `["130", "130"]` | Slightly slower tops for better MagSafe face |
| `textured_plate_temp` | `["65", "65", "65", "65"]` | `["55", "55", "55", "55"]` | SnapSpeed bed max is 60 C; 55 C on textured PEI |
| `textured_plate_temp_initial_layer` | `["65", "65", "65", "65"]` | `["55", "55", "55", "55"]` | Match bed to SnapSpeed range |
| `hot_plate_temp` | `["65", "65", "65", "65"]` | `["55", "55", "55", "55"]` | Keep alternate plate profiles consistent |
| `hot_plate_temp_initial_layer` | `["65", "65", "65", "65"]` | `["55", "55", "55", "55"]` | Keep alternate plate profiles consistent |
| `print_settings_id` | `0.20mm High Quality @Snapmaker U1 (0.4 nozzle)` | `0.20mm High Quality @Snapmaker U1 (0.4) — Duo Stand recommended fork` | Mark custom fork so it is not confused with stock HQ |

Unchanged on purpose:

- Process family: **0.20 mm High Quality** (layer height 0.2, initial 0.25)
- Filament profile: **Snapmaker PLA SnapSpeed @U1**
- Nozzle temp: **220 °C** (SnapSpeed high-speed band)
- Fan: **100%** after first layer
- Orientation: **base-down** on Textured PEI
- Elephant-foot compensation: **0.15 mm**
- Inner wall / infill speeds: **150 / 200 mm/s**

## Manual steps in Snapmaker Orca (required before slice)

These cannot be reliably painted into the 3MF from outside Orca:

1. **Supports — paint / block**
   - Keep tree(auto) enabled (already on in fork).
   - Paint support **onto the Apple Watch ring** (inner ceiling and outer crown).
   - Add support **blockers** in the MagSafe charger cavity and cable notches so trees do not fill the press-fit bore.
   - Prefer build-plate-only trees (already set); if a ring island still fails, allow a short non-ground tree on the ring only.

2. **Seam painting + scarf**
   - Seam position: **aligned** (encoded as `seam_position=aligned`).
   - Scarf type: **Contour** (encoded as `seam_slope_type=external`) — see Scarf section.
   - Paint the seam line to the **rear** of the MagSafe pillar (away from the phone face).
   - Optional upgrade for later reprints: **Contour and hole** (`seam_slope_type=all`) if MagSafe/Watch bore seams still look harsh after a good fit.

3. **Tool / color**
   - Load **SnapSpeed Black** on the active tool.
   - Confirm single-extruder / no unused-tool flush (prime tower already off).

4. **Plate**
   - Confirm **Textured PEI** and bed **55 °C** (encoded for textured + hot plate profiles).

5. **Optional quality polish**
   - Variable layer height **0.12–0.20 mm** on the MagSafe slope if available.
   - Optional light ironing on MagSafe front face only (adds time).

## After first print (fit loop)

| Check | Action |
|---|---|
| MagSafe puck too tight/loose | XY hole compensation ±0.1–0.2 mm; reprint or re-slice |
| Watch puck too tight/loose | Same XY hole compensation |
| MagSafe pillar flex | Bump walls 3→4 or infill 20%→25% |
| Ring scarred by supports | Increase support top Z gap slightly or add interface |
| Desk slip | Print `Duo Desk TPU Foot.stl` in TPU and install |

## Companion parts

- `Duo Desk Stand with watch charger.stl` — geometry source (unchanged)
- `Duo Desk TPU Foot.stl` — print separately with a TPU profile (not this PLA fork)
- `Duo Desk Stand 25W+watch FLAT.stl` — alternate geometry; not used by this fork

## How to regenerate this fork

If the stock 3MF is re-exported from Orca, re-apply the table above (or re-run the fork script used to produce this file) and keep this change list in sync.

## Scarf joint seam — Contour vs Contour and hole

Official Orca meaning ([Seam wiki](https://www.orcaslicer.com/wiki/print_settings/quality/quality_settings_seam)):

| UI label (Snapmaker Orca) | What it does | 3MF / config value (`seam_slope_type`) |
|---|---|---|
| **None** | Scarf disabled; normal Z-seam start/stop | `none` |
| **Contour** | Scarf only on **outer silhouette** walls (the outside of the part). **Holes are not scarfed.** | `external` |
| **Contour and hole** | Scarf on outer silhouette **and** on **hole** outer walls (MagSafe bore, Watch ring ID, cable notches, tray recesses treated as holes) | `all` |

Practical difference on this stand:

- **Contour** — smoothes the visible outside (base perimeter, MagSafe pillar exterior, watch-ring exterior). Hole walls (MagSafe charger ID, Watch puck ID) keep a normal seam. Prefer this when **press-fit diameter** matters; scarf on hole walls can slightly change how the seam blends on a critical ID.
- **Contour and hole** — also blends seams inside the MagSafe and Watch openings. Better cosmetics on those circles; use after a fit-test print if the bore seam bothers you and the puck still seats correctly.

Related scarf keys already present in the recommended 3MF (stock defaults unless noted):

| Key | Value in recommended 3MF | Notes |
|---|---|---|
| `seam_slope_type` | `external` | **Contour** — recommended default for this design |
| `has_scarf_joint_seam` | `0` | Not the primary switch in this Snapmaker Orca build; type above enables scarf |
| `seam_position` | `aligned` | Vertical seam; paint to rear of MagSafe pillar |
| `seam_gap` | `15%` | Stock HQ |
| `seam_slope_min_length` | `20` | Scarf length (mm) |
| `seam_slope_steps` | `10` | Scarf ramp segments |
| `seam_slope_start_height` | `0` | Scarf starts at full prior-layer top |
| `seam_slope_conditional` | `0` | Off — scarf not limited to “smooth only” curves |
| `seam_slope_entire_loop` | `0` | Off — do not scarf the whole perimeter |
| `seam_slope_inner_walls` | `0` | Off — outer wall of contour/hole only |
| `scarf_joint_speed` | `100%` | Relative to wall speed |
| `scarf_joint_flow_ratio` | `1` | Keep at 1 |
| `scarf_angle_threshold` | `155` | Used only if conditional scarf is on |
| `scarf_overhang_threshold` | `40%` | Used only if conditional scarf is on |

How to set in Snapmaker Orca UI: **Process → Quality → Seam → Scarf joint seam (beta)** → choose **Contour** or **Contour and hole**.

### Encoding trap (do not use the UI word in the 3MF)

Snapmaker Orca / OrcaSlicer enum is `SeamScarfType { None, External, All }`. Writing the UI word `contour` into `seam_slope_type` is **invalid** and triggers:

> `seam_slope_type` (`contour`) was replaced with `none`

Always encode Contour as `external` and Contour and hole as `all`.

## Compatibility note (2026-10-22)

An earlier fork wrote `seam_slope_type=contour`, which Snapmaker Orca rejected and reset to `none`. The recommended 3MF now uses the valid enum value `external` (**Contour**).
