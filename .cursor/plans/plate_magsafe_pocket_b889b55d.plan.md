---
name: Plate MagSafe Pocket
overview: Fit an Apple A3502 to the existing 260 mm sloped Duo plate using user-measured hardware, direct phone alignment measurements, independent fit coupons, and a verified back-edge cable route.
todos:
  - id: measure
    content: Record actual charger dimensions and phone configuration.
    status: completed
  - id: locate
    content: Measure the magnet center on the actual bare phone; establish protected support locations and cable exit height.
    status: pending
  - id: script
    content: Revise the existing script for the measured A3502 and independent fit tests; old geometry is superseded.
    status: pending
  - id: coupons
    content: Generate and physically test corrected coupons using production settings.
    status: pending
  - id: plate
    content: Apply the measured fit results, generate the plate, and verify geometry and assembled behavior.
    status: pending
isProject: false
---

# MagSafe pocket in the 260 mm Duo plate

## Current status and controlling inputs

Revised 2026-10-22 after the user supplied measurements during the plan review.
The existing script and generated coupon 3MF still implement the previous
2.35 mm cable assumption. They are superseded for fit validation of this charger;
no corrected CAD has been generated in this documentation checkpoint.

| Input | Value | Evidence |
|---|---|---|
| Charger model | Apple A3502 | User read from hardware |
| Puck diameter | 55.50 mm | User measurement |
| Puck thickness | 4.37 mm | User measurement |
| Cable diameter | 3.05 mm | User measurement |
| Separate collar | None | User observation |
| Phone | Actual Duo available, used bare | User confirmation |
| Magnet center | Not yet physically measured | X-ray estimate only |
| Cable-center height above puck underside | Not yet measured | Resolve in profile/coupon |
| Protected phone support locations | Not yet verified | Inspect actual bare phone |

These are user-reported measurements, not independently verified metrology;
measurement uncertainty has not been supplied. Do not transfer model-specific
dimensions or keep-in details from an A2580/A3250 drawing merely because the
measured envelope matches. Apple lists A3502 among its current MagSafe chargers:
https://support.apple.com/en-us/105047

Governing host plan:
`plans/current/2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket.md`.

## Existing geometry and coordinates

Source: `designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate 260 sloped.3mf`.
One manifold solid, 260 × 173 × 12 mm; preserve the original source.

Plan coordinates: plate center in XY, Z = 0 at the bottom.
The script currently uses source-local Z = -6 at the bottom: add 6 mm to convert
its Z values to this plan frame.

- Well: X -82.5 to 83.3, Y -59.1 to 59.9; center (0.4, 0.4).
- Well floor: Z = 6.75; rim: Z = 12.
- Camera opening: stadium bounded by X 15.5–82.5, Y 29.1–59.1.
- Twenty original Ø18 through vents.
- +X = camera half; +Y = camera end / back cable-exit edge.
- Existing source bed translation: (135.5, 136, 6), applied to source-local mesh.
  Its X bounds are 5.5–265.5 on the 270 mm bed; this is only 4.5 mm clearance
  on the +X side. Verify slicer acceptance explicitly or recenter by 0.5 mm if
  a strict 5 mm margin is required.

## Step 1: measure the magnet center directly

Use the actual phone and charger before printing a template.

1. Open the bare phone flat, with its back facing up and camera end away.
   Support the inner display on a clean, soft surface without forcing the hinge.
2. Attach the unplugged puck normally and let it settle magnetically with its
   cable relaxed. Do not push it toward the estimated center.
3. Measure parallel to the phone's width and height, through the puck center:
   - A: camera-half outer side edge to the nearest puck rim.
   - B: camera-end body edge to the nearest puck rim, using the body edge,
     not the camera bump.
4. Remove and reseat the puck three times; record A and B each time, to 0.1 mm
   if practical. A ruler is useful for preliminary measurements; its precision
   must not be reported as caliper precision.
5. If spread exceeds 0.3 mm on either axis, improve the datums or use an
   edge-registered measuring fixture before fixing the pocket center.

For the nominal 164.6 × 117.8 mm phone centered in the current well:
`center_x = 54.95 - A`, `center_y = 31.55 - B` (mm).
These formulas assume the stated phone envelope and centered seating.
They give (41.2, -2.3) for A = 13.75, B = 33.85; those are predictions,
not measurements to aim for. Verify the actual envelope/clearance if results
disagree. Include the well's approximately ±0.6 mm phone play per axis in the
final alignment check; repeatability of center measurement does not remove it.

The previous Ø66 template is not required for this first measurement.
If a fixture is needed later, use repeatable edge stops and accessible reference
marks. Its clipped +Y hole boundary requires its own formula; the symmetric
four-gap formula is invalid. For symmetric X references, positive displacement
is `(gap-X - gap+X) / 2`, not the opposite sign previously documented.

## Step 2: establish support, seating height, and cable envelope

- The bare phone's cover display must not bear on abrasive grille ribs.
  Identify non-display support locations; use suitable smooth/soft contact
  surfaces and include their compressed thickness in the height stack.
- Retire the fixed 4.6 mm pocket depth. With a measured 4.37 mm puck this would
  recess the face by 0.23 mm relative to the original floor.
- Parameterize puck seating and phone supports together. If the puck face is
  `s` above the original floor and the puck sits directly on its ledge:
  `pocket_depth = 4.37 - s`;
  `ledge_thickness = 6.75 - pocket_depth`.
  Determine `s` from the support stack, printed-height checks, and contact
  requirements. Do not lock an untested height or allow phone rocking.
- Keep the local holder below the relevant charger top datum; verify applicable
  A3502 keep-in geometry and the actual phone assembly.
- Measure/observe the cable exit profile and model the complete 3D cable
  envelope, including its downward transition. No separate collar does not
  justify an immediate sharp bend at the housing.

## Step 3: independent fit coupons

Use shared production geometry, intended material, nozzle, layer height,
orientation, and slicer compensation. Record printed dimensions as well as
nominal dimensions. Do not treat manifoldness as physical-fit evidence.

- Bore trials: start with 55.8 / 56.0 / 56.2 mm as clearance-fit candidates.
  They have 0.3 / 0.5 / 0.7 mm nominal diametral clearance and do not establish
  retention. Choose the smallest that permits gentle insertion and push-out.
- Cable trial: begin with an open 3.6 mm wide × 3.6 mm deep channel as an
  unverified starting candidate for the measured Ø3.05 cable. It gives 0.55 mm
  nominal total clearance in each direction without a retaining lip.
  Check printed clearance and whether the cable remains above the bottom plane.
- Retire 1.90 / 2.05 / 2.20 mm pinch widths and the old 2.8 mm channel.
  Test any new cable retainer separately from bore selection. A retainer must
  preserve a clear cavity above it and must not damage/compress the braid.
- Include the full vertical cable transition and 20 mm starting XY bend radius
  in a functional coupon, rather than assuming an XY radius proves the Z bend.
- Include the Ø34 push-out opening and resulting support ledge where feasible.
  Verify the final ledge after the gate, floor slot, and neighboring cuts.
- Keep the puck seated during repeated actual phone attachment/removal, both
  cold and after representative charging. Support the coupon so its weight is
  not mistaken for production retention. Never lift the assembly by its cable
  as the retention acceptance test.
- If a clearance bore does not retain the puck, add and test shallow sidewall
  retention features, then repeat removal and warm-use checks. The cable is
  not the puck's anti-lift mechanism.

## Step 4: finish the plate after physical results

Keep the source plate, camera opening, thumb access at -X, and back (+Y) cable
exit intent. Retain the requested ordered grille as a later geometry step;
it is not needed to establish charger fit.

Route from the puck's +X edge through the floor into the underside channel,
around the camera opening and out the back. Recompute all margins with the
larger cable channel. Open the terminal channel through the sloped edge where
a roof would otherwise become too thin; the start of that notch is derived
from final geometry, not the previous Y ≈ 81.4 result.

For the grille, retain provisional 4 mm slots / 7.5 mm pitch, 7 mm well-border
margin, 6 mm feature margin, 10 mm hinge spine, 15 mm minimum slot length,
and 0.5 mm top chamfer. Recompute the layout at the measured pocket center.
Apply margins to the finished chamfered boundaries, not only slot centerlines.
Slots running along Y are parallel to the hinge direction in this coordinate
system. Verify both support endpoints of every remaining rib.

Filling old vents and cutting a new grille is a mesh Boolean operation, not
a separately printed plug joint. Still verify continuous material after cuts.
Similar open area does not establish similar cooling. Test representative
charging with the actual phone, adapter, material, and desk contact.
If heat or charging behavior is unacceptable, revise underside airflow/support
clearance and retest rather than claiming the holes guarantee cooling.

## Verification and files

Declare `minimum_wall_thickness = 2.0 mm` and
`minimum_structural_overlap >= minimum_wall_thickness`.
Apply the material minimum to actual structural ligaments in all relevant
section directions, including Z. Do not require material between intentionally
connected voids. Thin measuring sheets and any flexible retainer require an
explicit part-specific rationale; an XY slice scan cannot validate their
vertical thickness. Structural connections remain unverified until audited.

Before printing a revised coupon:
- Verify exact exported dimensions, component count, bed placement, and layer
  paths; check supports/bridges in Orca rather than assuming no supports.
- Save input mesh hash, script/config hash, dependencies, and output hash.
- State what the coupon validates and what it cannot validate.

Before calling the final plate ready:
- Confirm measured center, calibrated bore and seating height, support plane,
  push-out access, camera clearance, notch, and complete cable envelope.
- Measure shortest remaining ligaments after all cuts and chamfers; inspect rib
  endpoints, cable transition/exit, and ledge in XY and vertical sections.
- Check phone placement at the extremes of well play, safe cover-display
  clearance, repeated phone removal, and charging behavior on the desk.
- Verify source exterior preservation except declared changes and flat bed
  contact. Document slicer settings and physical evidence separately from
  manifold/connectivity evidence.

Source script:
`designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py`.
Generated meshes:
`output/iphone-duo/iPhone Duo Plate MagSafe fit coupons.3mf` and
`output/iphone-duo/iPhone Duo Plate 260 sloped magsafe.3mf`.
Update the design README, host plan, and append-only journal at checkpoints.
No commit or push is authorized by this measurement update.
