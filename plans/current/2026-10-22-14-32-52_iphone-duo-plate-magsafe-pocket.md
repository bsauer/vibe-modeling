---
plan_id: 2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket
title: MagSafe pocket for the 260 mm iPhone Duo plate
summary: Revise the plate and fit tests for the measured Apple A3502 and bare Duo; confirm alignment and support before regenerating coupons.
status: current
created_at: 2026-10-22-14-32-52
---

# MagSafe pocket for the 260 mm iPhone Duo plate

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Scope and current evidence

The user requested a plan review and step-by-step guidance, then supplied the
hardware measurements below. This checkpoint records those measurements and
revises the plan; it does not generate or approve a final plate.

Design detail:
`.cursor/plans/plate_magsafe_pocket_b889b55d.plan.md`.
Retain the earlier requested grille and +Y back-edge exit, but validate the
functional interfaces before completing that geometry.

User-reported on 2026-10-22:
- Charger A3502; puck Ø55.50 × 4.37 mm.
- Cable Ø3.05 mm; no separate collar.
- Actual phone available and used bare.

Existing script/coupon generation is a historical completed checkpoint under
superseded assumptions. Its Ø2.8 channel, 1.90–2.20 mm pinches, 4.6 mm pocket
depth, and retention tests are not valid acceptance evidence for this hardware.
Do not direct the user to print the old coupon as the next step.
The old artifact remains unchanged for provenance.

## Next physical step: direct center measurement

Attach the unplugged puck to the open phone's back with its cable relaxed.
Measure A from the camera-half outer side edge to the nearest puck rim, and B
from the camera-end body edge to the nearest puck rim, parallel to the body
axes through the puck center. Remove/reseat three times and record each result.

For the nominal phone centered in this well:
`center_x = 54.95 - A`; `center_y = 31.55 - B`.
If repeat spread exceeds 0.3 mm, improve the measuring datums before fixing the
center. Include the well's phone play in final assembly validation.
A printed locator is needed only if direct measurements are not repeatable.
See the detail plan for the coordinate convention and fixture formula correction.

## Revised execution checklist

- [x] 1. Record measured hardware and phone configuration.
- [x] 2. Revise/synchronize design plan, host plan, and README; mark old coupons superseded.
- [ ] 3. Confirm physical datums and support.
  - [ ] 3.1 Receive repeated A/B magnet-center measurements.
  - [ ] 3.2 Identify protected bare-phone support locations and height stack.
  - [ ] 3.3 Resolve cable exit height and complete 3D transition.
- [ ] 4. Revise shared geometry and generate corrected coupons.
  - [ ] 4.1 Derive pocket depth from measured puck and phone support height; retire fixed 4.6 mm depth.
  - [ ] 4.2 Test bore fit independently from cable retention.
  - [ ] 4.3 Start cable clearance trials at 3.6 × 3.6 mm without pinch lips; treat this as provisional.
  - [ ] 4.4 Include full cable transition/bend and production-derived pocket geometry.
  - [ ] 4.5 Verify exported geometry, vertical/XY ligaments, bed placement, slicer paths, and provenance.
- [ ] 5. Print and test corrected coupons.
  - [ ] 5.1 Record printed dimensions and settings; select fit.
  - [ ] 5.2 Test actual phone attachment/removal without using cable as a tether.
  - [ ] 5.3 Repeat retention and charging checks warm; verify protected phone contact.
- [ ] 6. Apply physical results and finish the plate/grille/back-edge exit.
- [ ] 7. Export and verify final geometry and physical desk-use behavior.
- [ ] 8. Update README, plan, and journal at the CAD checkpoints.

Generated artifacts belong in `output/iphone-duo/`; source script remains in
`designs/iphone-duo/iPhone-Duo-Plate/`. Use pinned manifold3d via `uv run`.
Structural minimums are 2.0 mm for walls and overlap; verify final ligaments
in all relevant directions. Thin fixtures/flexible elements need an explicit
part-specific rationale, not an implicit exemption.

No geometry changed in this checkpoint. Structural joins and minimum internal
edge/material width: not applicable to this documentation edit; proposed
revised geometry remains unverified. No commit or push.

## Historical coupon checkpoint (superseded for A3502 fit validation)

The evidence below records the earlier build only. It is not acceptance of the
revised dimensions, phone support, retention, or charging behavior.


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
