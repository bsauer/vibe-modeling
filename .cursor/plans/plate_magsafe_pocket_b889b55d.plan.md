---
name: Plate MagSafe Pocket
overview: Add a top-drop Apple 25 W MagSafe pocket to the 260 mm sloped Duo plate at the measured magnet-ring center, with a tuned bore, an open floor under the puck, a thumb notch, and a gently bent cable path that leaves the back edge away from the user. Fit coupons and a center-check template print first.
todos:
  - id: host-plan
    content: Write and promote a short current host plan for the mesh edit under plans/current, regenerate and check plan indexes.
    status: pending
  - id: measure
    content: Caliper the 25 W puck (diameter, thickness, cable exit height, strain-relief collar length and diameter). Record values; stop if they differ from the assumptions below.
    status: pending
  - id: script
    content: "Add add_magsafe_pocket.py with named constants and asserts: pocket at the X-ray ring center, Ø34 floor opening with ledge, 4 vents filled, floor slot, pinched bottom raceway to the back edge, thumb notch. One function builds both the plate and the coupons."
    status: pending
  - id: coupons
    content: Generate the fit-coupon 3MF (center-check template plus three bore coupons) and print it.
    status: pending
  - id: tune
    content: Apply coupon results to the constants (ring center, bore diameter, pinch width). Record the chosen values and why.
    status: pending
  - id: mesh
    content: Generate the model-only MagSafe plate 3MF with the existing bed placement; leave the sloped plate unchanged.
    status: pending
  - id: verify
    content: Section-check center, bore, ledge, opening, walls, vent fill, floor slot, raceway, pinch points, notch, flat bottom, and sloped ends.
    status: pending
  - id: docs
    content: Update the iphone-duo README and today's journal. Do not commit.
    status: pending
isProject: false
---

# MagSafe pocket in the 260 mm Duo plate

## Existing plate (measured from the mesh)

The file [designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate 260 sloped.3mf](designs/iphone-duo/iPhone-Duo-Plate/iPhone%20Duo%20Plate%20260%20sloped.3mf) is a single manifold solid, **260 × 173 × 12 mm**, placed on the Snapmaker U1 bed at X 5.5–265.5 mm. It is a shallow tray for an **open** Duo, back down, not a stand. Local coordinates below have the origin at the plate center and Z = 0 at the plate bottom.

- Phone well: X −82.5 to +83.3, Y −59.1 to +59.9 (**165.8 × 119.0 mm**), about 0.6 mm clearance per side around the open phone (164.6 × 117.8 × 5.2 mm). Well depth **5.25 mm**, so the phone sits flush with the rim. Well center is **(0.4, 0.4)**.
- Floor under the well is **6.75 mm** (Z 0 to 6.75).
- Camera slot: through opening X 15.5 to 82.5, Y 29.1 to 59.1 (**67 × 30 mm**) in the +X / +Y corner.
- Twenty **Ø18 mm** through vents. No finger notch. No charger.

Orientation: the camera end of the phone is +Y. With the phone open in landscape, that is the edge farthest from the user, so **+Y is the back edge** and −Y faces the user. The camera half is +X.

## Where the magnet ring is

Apple has not published the Duo ring position. The reference [references/engineering/apple/iphone_duo/device.md](references/engineering/apple/iphone_duo/device.md) only says the MagSafe face is on the camera half. It does not say the ring is centered on that half. The previous plan assumed it was.

The X-ray in `designs/iphone-duo/iPhone-Duo-Plate/Screenshot 2026-10-22 at 1.31.26 PM.png` gives a better estimate. A circle fit to the ring gives Ø53.8 mm against Apple's 54.1 mm ring OD, so the image scale is trustworthy (phone height 117.8 mm = 1141 px). Results:

- Across the half, the ring is centered within about 0.4 mm.
- Along the phone, the ring center is about **2.7 mm away from the camera end**.

Estimated pocket center in plate coordinates: **(41.2, −2.3) mm**. This replaces the earlier (41.6, 0.4).

The well holds the phone to about 0.6 mm per side and MagSafe self-alignment is at most 1.55 mm, so this center is the alignment lock. It must be confirmed physically with the center-check template before the full plate is cut. The corrected center also clears the camera slot: the wall between bore and slot grows from about 0.7 mm to about **3.4 mm**, so the camera slot is not modified.

## Puck

Target puck: Apple **25 W MagSafe Charger (A2580 / A3250)**, **Ø 55.4–55.5 mm × 4.45–4.53 mm** per the reference, braided cable about **Ø 2.35 mm** exiting radially from the rim (confirmed by the Folio photo in the design folder). Treat the following as unverified until measured with calipers in the `measure` step: cable exit height above the puck back, strain-relief collar diameter and length, and whether any molded elbow exists.

Stop condition: if the puck in hand is the older **15 W (A2140)**, or the caliper values differ from the above by more than 0.2 mm, stop and revise the plan before cutting.

## The pocket

All values are named constants in the script with `assert()` guards.

- `minimum_wall_thickness = 2.0` mm. `minimum_structural_overlap = 2.0` mm (declared for policy; the part is one solid with no joins). No feature may leave less than 2.0 mm of plastic. There is no fallback that accepts thinner walls; if a check fails, stop and revise the plan.
- **Center** `(41.2, −2.3)` from the X-ray, replaced by the center-check result.
- **Bore** starting value Ø **56.0 mm**, final value chosen from the coupons (55.8 / 56.0 / 56.2). Pick the tightest bore the puck drops into by hand and lifts out of only with the push-out hole. That light friction, plus the cable in the floor slot, keeps the puck seated when the phone is lifted. No crush ribs, lip, or adhesive unless the coupons show the puck still lifts out.
- Bore tessellated with at least **256 segments** so flat facets do not shrink the printed hole.
- **Depth** 4.6 mm from the well floor, so the puck face sits 0.07–0.15 mm below the floor and the phone rests on plastic, not on the puck.
- **Open floor**: a Ø **34 mm** through-hole on the same center, leaving a **ledge** 2.15 mm thick and about 11 mm wide that carries the puck rim. The hole lets you push the puck out from below and lets heat escape from the puck back.
- **Vents**: fill the four vents the bore intersects before cutting, centers about **(25.6, 0)**, **(50.8, 0)**, **(25.6, −21.8)**, **(50.8, −21.8)**. Recheck the list at the final center. The other sixteen stay open.
- Check the ledge between the Ø34 hole and every remaining vent, and between the bore and the camera slot, against the 2.0 mm minimum.

## Thumb notch

The phone sits flush in a tight well and is held by roughly 0.65–1.5 kgf of magnet pull, so it needs a grip.

- One thumb scoop at the **−X short end** of the well (the cover half, far from the magnets), centered on the well's Y center.
- About **25 mm** wide along Y, reaching about **12 mm** into the rim, sloping down to **1.5 mm** below the well floor at the well edge so a fingertip gets under the phone.
- Lifting from this end peels the phone off the puck, which needs much less force and does not pull the puck up.
- Check that the scoop leaves at least 2.0 mm to the nearest vent and to the sloped outer end.

## Cable path

Goal: the cable leaves the plate at the **back edge (+Y)**, away from the user, never across the front or the user's side. Assumption to confirm with the user before the script runs: "exit through the top of the plate" means the back (+Y) edge. If it means rising out of the top surface instead, revise this section.

The camera slot blocks a straight run to +Y from the pocket, so the cable goes around the +X side, where the rim is solid:

1. **Gate**: a 5 mm wide opening in the bore wall at the puck's +X rim, open at the top, so puck and cable drop in together. Width is confirmed against the measured strain-relief collar.
2. **Floor slot**: a through slot in the well floor, about **3.0 mm** wide, running about **12 mm** in +X from the gate to just inside the well wall. The cable descends gradually from its exit height on the puck rim (about 4.4 mm above the plate bottom) into the raceway below. No sharp bend at the strain relief. The phone covers the slot.
3. **Bottom raceway**: open on the bottom, **2.8 mm** wide × **3.2 mm** deep, continuing in +X under the solid rim to about X = 100, then turning to +Y with a centerline bend radius of at least **20 mm**, and running straight to the **+Y back edge**. It never crosses a vent or the camera slot.
4. **Pinch points**: three short narrowings, each about 3 mm long, where the raceway mouth closes to **2.05 mm** (coupon variants 1.9 / 2.05 / 2.2), so the 2.35 mm braid snaps in and stays when the plate is lifted. The 2.8 mm raceway prints as a short bridge with no supports.
5. Roof over the raceway is at least 3.5 mm everywhere outside the floor slot. The bottom face outside the raceway, the floor slot, and the Ø34 hole stays at Z = 0, so the plate sits flat.

## Fit coupons (new 3MF)

New file `designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate MagSafe fit coupons.3mf`, model-only, all parts flat on the U1 bed inside the 5 mm edge margin, no supports.

- **Center-check template**: a 0.8 mm sheet in the phone's open outline (164.6 × 117.8 mm), with the camera-slot cutout and a Ø56 hole at the candidate center. Lay it on the back of the open phone with its edges aligned, then drop the puck into the hole. If the magnets pull the puck to one side of the hole, the center is off; mark and measure the offset and update the center. Engraved crosshair ticks at 1 mm spacing around the hole make the offset readable.
- **Three bore coupons**, each a roughly 75 × 75 mm cut from the production pocket geometry at full floor height: bore, ledge, Ø34 opening, gate, floor slot, and the first 30 mm of pinched raceway. Bores **55.8 / 56.0 / 56.2 mm** with pinch widths **1.9 / 2.05 / 2.2 mm**, identified by 1, 2 or 3 notches on one edge.
- Coupons are built by the same script functions as the plate, so the tested geometry is the production geometry.

Fit checks with the coupons: puck drops in by hand; puck stays put when lifted by its cable; face sits just below the coupon floor; puck pushes out through the Ø34 hole; cable lies in the floor slot without a kink; braid snaps into the pinch and stays.

## Files

- New script [designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py](designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py) using the pinned `manifold3d` via `uv run`. It edits the existing mesh; the plate is not rebuilt in OpenSCAD.
- New coupon mesh `designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate MagSafe fit coupons.3mf`.
- New plate mesh `designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate 260 sloped magsafe.3mf`, same bed transform as the current plate, model-only so Orca does not inherit the old Bambu profile errors.
- Short note in [designs/iphone-duo/README.md](designs/iphone-duo/README.md) and today's journal. A current host plan file is written at the start of the edit, per repo policy. No commit unless you ask.

## Checks before calling it done

- One manifold shell for the plate; each coupon is one shell.
- Bore center within **0.1 mm** of the confirmed center; bore at the tuned diameter, depth 4.6 mm, ledge 2.15 mm thick.
- Ø34 opening passes through; ledge width at least 2.0 mm everywhere.
- Every wall between bore, Ø34 hole, remaining vents, camera slot, floor slot, raceway, and notch is at least **2.0 mm** by the shortest path.
- Camera slot unchanged.
- Filled vents do not remain as holes inside the pocket; the other vents still pass through.
- Raceway 2.8 × 3.2 mm, open on the bottom, bend radius at least 20 mm, pinch points at the tuned width, exiting only the +Y back edge.
- Bottom face outside the openings still at Z = 0 in bed coordinates.
- Thumb notch present at −X; outer sloped ends otherwise unchanged. No Watch puck.

Structural joins: not applicable (one solid, no seam). Minimum internal edge: passed only if the 2.0 mm section checks pass. Revision/config: these mesh files, not an OpenSCAD revision. Build scope: mesh boolean, not `scad_build_all.py`.
