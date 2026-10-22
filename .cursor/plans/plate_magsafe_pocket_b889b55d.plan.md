---
name: Plate MagSafe Pocket
overview: Add a top-drop Apple 25 W MagSafe pocket to the existing 260 mm sloped Duo plate, with one open-bottom cable raceway copied from the desk stand, cut into the current mesh rather than remodeling the plate.
todos:
  - id: host-plan
    content: Write and promote a short current host plan for the mesh edit.
    status: pending
  - id: script
    content: "Add add_magsafe_pocket.py: fill 4 vents, cut Ø56×4.6 pocket, 5 mm gate, 4×3.2 mm open raceway to +X."
    status: pending
  - id: mesh
    content: Generate the model-only MagSafe 3MF with the existing bed placement; leave the sloped plate unchanged.
    status: pending
  - id: verify
    content: Section-check membrane, camera ligament, raceway, vent fill, flat bottom, and sloped ends.
    status: pending
  - id: docs
    content: Update the iphone-duo README and today's journal. Do not commit.
    status: pending
isProject: false
---

# MagSafe pocket in the 260 mm Duo plate

## Root cause

The file [designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate 260 sloped.3mf](designs/iphone-duo/iPhone-Duo-Plate/iPhone%20Duo%20Plate%20260%20sloped.3mf) is a single manifold solid, **260 × 173 × 12 mm**, already placed on the Snapmaker U1 bed at X 5.5–265.5 mm. It is a shallow tray for an **open** Duo, not a stand.

- Phone well: **165.8 × 119.0 mm**, about 0.6 mm clearance per side around the open phone (164.6 × 117.8 × 5.2 mm). Well depth is **5.25 mm**, so the open phone sits flush with the rim.
- Floor under that well is **6.75 mm** (local Z −6.00 to +0.75).
- Camera bump slot is the rounded opening in the **+X / +Y** corner. Twenty **Ø18 mm** vents pierce the floor. The mesh has no charger.

Duo MagSafe is the camera-half ring, centered on that half when the phone is in this well: about **(41.6, 0.4) mm** in plate coordinates. Apple has not published the ring drawing; this center follows the open/closed envelopes already in [references/engineering/apple/iphone_duo/device.md](references/engineering/apple/iphone_duo/device.md). A 55.5 mm puck there clears the well walls, but it is only **0.8 mm** from the camera slot and it covers four vents. Those two facts are the actual geometry problem.

The puck cannot sit under a plastic window. Guidelines allow at most ~2 mm of case plastic over a ring, and this plate is a holder for Apple’s puck, so the charging face has to be the floor of an open pocket. The 25 W puck (A2580 / A3250) is **Ø 55.4–55.5 mm × 4.45–4.53 mm**, with a **Ø 2.35 mm** braided cable and **no** molded strain-relief elbow. That puck fits in the 6.75 mm floor and still leaves a **2.15 mm** membrane. The old 15 W puck’s elbow does not.

The referenced stand ([Duo Desk Stand with watch charger.stl](designs/iphone-duo/iPhone+Duo+MagSafe+++Apple+Watch+Charging+Stand/Duo%20Desk%20Stand%20with%20watch%20charger.stl)) does not use a closed cable tunnel. Its underside is an open recess, and the rear exit pinch measures about **4 mm wide × 3.2 mm deep**. The cable is pressed in from below and the part still sits flat. The plate needs that same open-bottom raceway. It does not need the Watch puck or the tilted bore.

```mermaid
flowchart LR
  phone[Open Duo back down in the well]
  puck[25W puck dropped in from the top]
  gate[Side gate at the puck rim]
  race[Open-bottom raceway]
  edge[Cable leaves under the plus-X edge]
  phone --> puck --> gate --> race --> edge
```

## The cut

Keep the sloped plate untouched. Write a new model-only 3MF beside it. Edit the existing mesh with the project’s `manifold3d` (already pinned). Do not rebuild this plate in OpenSCAD.

Pocket, in local plate coordinates:

- Center **(41.6, −0.8) mm**. That is the camera-half center, shifted **1.2 mm** away from the camera slot so the ligament is **2.0 mm**. The shift is inside MagSafe’s **1.55 mm** self-alignment, so the phone still snaps onto the puck.
- Bore **Ø 56.0 mm** (0.5 mm diametral clearance on a 55.5 mm puck) so it drops in from the top on a 0.4 mm nozzle.
- Depth **4.6 mm** from the well floor, charging face flush. Membrane under the coil **2.15 mm**.
- Before the pocket is cut, fill the four vents the bore intersects, centers about **(25.6, 0)**, **(50.8, 0)**, **(25.6, −21.8)**, **(50.8, −21.8)**. Leaving them would punch the membrane. The other sixteen vents stay.

Cable path, same idea as the stand:

- One **U-groove, open on the bottom**, **4.0 mm wide × 3.2 mm deep**, from the puck’s **+X** rim straight to the plate’s **+X** bottom edge. That edge is solid: no vents, no camera slot, and the slope is only the top rim, so the flat bottom foot is preserved.
- A **5 mm** gate in the bore wall, open at the top, so the puck and cable drop in together. The gate is the only place the membrane is broken. The 2.35 mm braid then presses down into the groove.
- Roof over the groove is about **3.5 mm**. Nothing crosses the coil.

The cable trapped in the side gate is what keeps the puck from falling out when the plate is lifted. No lip and no press-fit.

## What you do not need to install

No new skill, slicer access, or CAD app. `uv` and `manifold3d` 3.3.2 are already in this repo. Snapmaker Orca stays your slice step after the mesh exists. A fit check is dropping the **25 W braided** puck in and setting the open phone on the camera half.

Stop condition: if the puck in hand is the older smooth-cable **15 W (A2140)** with the molded elbow, the gate and bore change. Say so before the cut. Otherwise the 25 W puck is the one Duo is rated for.

## Files

- New script [designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py](designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py) with the numbers above as named constants.
- New mesh `designs/iphone-duo/iPhone-Duo-Plate/iPhone Duo Plate 260 sloped magsafe.3mf`, same bed transform as the current plate, model-only so Orca does not inherit the old Bambu profile errors.
- Short note in [designs/iphone-duo/README.md](designs/iphone-duo/README.md) and today’s journal. A current host plan file is written at the start of the edit, per repo policy. No commit unless you ask.

## Checks before calling it done

- One manifold shell.
- Bore Ø 56.0 mm, depth 4.6 mm, membrane ≥ 2.0 mm, camera-slot ligament ≥ 2.0 mm.
- The four filled vents do not remain as holes inside the pocket; the other vents still pass through.
- Raceway 4.0 × 3.2 mm, open on the bottom, exiting only the +X edge. Bottom face outside the groove still at Z = 0 in bed coordinates, so the plate sits flat.
- Outer sloped ends unchanged. No Watch puck.

Structural joins: not applicable (one solid, no seam). Minimum internal edge: passed only if those section checks pass. Revision/config: this mesh file, not an OpenSCAD revision. Build scope: mesh boolean, not `scad_build_all.py`.
