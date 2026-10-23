---
plan_id: 2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket
title: MagSafe pocket for the 260 mm iPhone Duo plate
summary: Add a tuned 25 W MagSafe puck pocket, slot vent grille, thumb notch, and back-edge cable raceway to the sloped Duo plate, validated first by production-derived fit coupons.
status: current
created_at: 2026-10-22-14-32-52
---

# MagSafe pocket for the 260 mm iPhone Duo plate

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Scope and approval

Design detail lives in `.cursor/plans/plate_magsafe_pocket_b889b55d.plan.md`,
reviewed and revised with the user on 2026-10-22. The user approved items 1-8 of
the review, the vent grille, and the back-edge cable exit ("top" means the +Y
back edge). The user confirmed the puck in hand is the 25 W MagSafe Charger. On
2026-10-22 the user asked to "create the test-piece 3mf", which authorizes
items 1 and 2 below. Items 3 onward need the coupon results and a further go-ahead.

Generated meshes go to `output/iphone-duo/` (AGENTS.md section 8: the only
mutable artifact destination, including coupons). The geometry script is source
and lives in `designs/iphone-duo/iPhone-Duo-Plate/`.

Governance values: `minimum_wall_thickness = 2.0 mm`,
`minimum_structural_overlap = 2.0 mm` (declared; the plate is one solid with no
printed joins). No feature may leave less than 2.0 mm of plastic.

## Coupon questions and decision thresholds

- Center-check template: is the magnet-ring center at the X-ray estimate
  (41.2, -2.3)? Measure the four gaps between the puck and the Ø66 template
  hole. Offset = half the difference of opposite gaps. Accept the estimate when
  both offsets are at most 0.3 mm; otherwise move the center by the measured
  offset and reprint the template.
- Bore coupons (55.8 / 56.0 / 56.2 mm): choose the tightest bore the puck drops
  into by hand, that holds the puck when the coupon is turned over and shaken
  lightly, and that releases the puck when pushed through the Ø34 opening.
  If even 55.8 does not hold, add crush ribs through a plan revision.
- Pinch widths (1.90 / 2.05 / 2.20 mm): choose the widest pinch that holds the
  braided cable when the coupon is lifted by its edge, without denting the braid.

## Checklist

- [x] 1. Shared geometry script.
  - [x] 1.1 Add `designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py` with named constants, asserts, vent fill, slot grille, pocket, Ø34 opening, gate, floor slot, pinched raceway with back-edge exit, and thumb notch.
  - [x] 1.2 One code path builds both the plate and the coupons.
- [x] 2. Fit coupons.
  - [x] 2.1 Generate `output/iphone-duo/iPhone Duo Plate MagSafe fit coupons.3mf`: center-check template plus three bore/pinch coupons, labeled by 1-3 edge notches.
  - [x] 2.2 Verify every object is one manifold shell, bores and centers match, ledge 2.15 mm, and no material thinner than 2.0 mm except declared label notches and crop corners.
  - [x] 2.3 Fit the layout inside the Snapmaker U1 bed with 5 mm edge margin.
- [ ] 3. Physical evidence (user).
  - [ ] 3.1 Caliper the puck: diameter, rim thickness, cable diameter, cable-center height, collar.
  - [ ] 3.2 Print coupons with production settings and record results against the thresholds above.
- [ ] 4. Tune constants from the coupon results and record the chosen values.
- [ ] 5. Generate `output/iphone-duo/iPhone Duo Plate 260 sloped magsafe.3mf`, model-only, same bed placement as the source plate.
- [ ] 6. Verify the plate: sections, walls, grille lands, raceway roof, flat bottom, sloped ends.
- [ ] 7. Update `designs/iphone-duo/README.md` and today's journal at each checkpoint.
  - [x] 7.1 Coupon checkpoint documented (README, journal, Cursor design plan).
  - [ ] 7.2 Plate checkpoint documented.

## Coupon checkpoint evidence (2026-10-22)

Command: `uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --coupons`
(manifold3d 3.3.2, Python 3.13, Git base `c44023d`). Output bytes are reproducible.

- Source plate SHA-256 `e287a4e3d8810c331e0c83b041d7983deefa1721808aeb5794165f6ed649cd86`.
- Every object reloads from the written 3MF as one manifold shell sitting at Z = 0.
- Bores measured 55.799 / 55.999 / 56.199 mm at center (41.200, -2.300). Ledge opening 33.999 mm; ledge 2.15 mm.
- Pinch gaps measured perpendicular to the path: 1.900 / 2.050 / 2.200 mm.
- Thin-material scan (morphological opening at 2.0 mm), every 0.2 mm through the full height: none, excluding a 3 mm band at the coupon crop edges and label notches. Template: none.
- Bed layout inside the 270 mm U1 bed with 5 mm margin: template X 5-175.6 / Y 5-128.8; coupons X 5-225 / Y 136.8-238.4.

Deviations from the design plan, recorded there too:

- Raceway depth 3.4 mm instead of 3.2 mm, so the braid clears the 0.8 mm pinch lips.
- Template hole Ø66 instead of Ø56 so the puck can self-center; +Y side flattened at Y = 27.1 for the 2.0 mm strip.
- The raceway opens into a full-height notch near the sloped back edge, where the roof would thin below 2.0 mm.
- Grille slots must reach the border band at one end, which removes the island slot between the pocket and the camera slot.
- Fixed during build: a zero-width sliver at pinch-lip ends and a floor-slot start that ignored the coupon bore.
