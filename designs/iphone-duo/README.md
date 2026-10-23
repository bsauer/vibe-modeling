# iphone-duo (print assets)

This directory holds **MagSafe desk-stand / plate** print files whose product
names include “Duo” (for example MagSafe Duo desk stands and trimmed plates).

It is **not** the engineering reference for Apple’s foldable **iPhone Duo**
phone or Apple’s official **iPhone Duo Folio with Kickstand** / **iPhone Duo
Case**.

For phone/case/MagSafe accessory design specs, use:

- `references/engineering/apple/iphone_duo/`
- Narrative research: `reports/iPhone Duo accessory design.md`

## iPhone Duo Plate: MagSafe pocket (in progress)

Governing plan: `plans/current/2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket.md`
(design detail in `.cursor/plans/plate_magsafe_pocket_b889b55d.plan.md`).

`iPhone-Duo-Plate/add_magsafe_pocket.py` edits the existing
`iPhone Duo Plate 260 sloped.3mf` mesh with manifold3d. It adds a 25 W MagSafe
puck pocket at the estimated magnet-ring center, a Ø34 push-out opening, a
parallel-slot vent grille that replaces the twenty round vents, a thumb notch,
and a pinched underside cable raceway that exits the back (+Y) edge. The source
plate is never modified. Generated meshes go to `output/iphone-duo/`.

```bash
uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --coupons
uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --plate
```

`--coupons` writes `output/iphone-duo/iPhone Duo Plate MagSafe fit coupons.3mf`:

- **Center-check template** (print lip up). Set the puck face-up in the Ø66
  hole, lower the open phone back-down into the lip, lift everything together
  and turn it over. Measure the four puck-to-hole gaps:
  `dx = (gap+X - gap-X) / 2`, `dy = (gap-Y - gap+Y - 3.60) / 2`.
  Nominal gaps are 5.25 mm at ±X and -Y and 1.65 mm at the flat +Y edge.
- **Three coupons** cut from the production geometry, marked by 1, 2 or 3
  V-notches: bore 55.8 / 56.0 / 56.2 mm with cable pinch 1.90 / 2.05 / 2.20 mm.

Selection rules for bore, pinch and center are in the governing plan. The plate
is not print-ready until those results are applied and the plate is verified.
