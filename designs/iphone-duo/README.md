# iphone-duo (print assets)

This directory holds MagSafe desk-stand / plate print files and the in-progress
bare iPhone Duo plate modification. General phone/case engineering references
live in `references/engineering/apple/iphone_duo/`; narrative research is in
`reports/iPhone Duo accessory design.md`.

## iPhone Duo Plate: MagSafe pocket (in progress)

Governing plan:
`plans/current/2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket.md`.
Design detail: `.cursor/plans/plate_magsafe_pocket_b889b55d.plan.md`.

### Current hardware and artifact status — 2026-10-22

The user reports an Apple A3502, puck Ø55.50 × 4.37 mm, cable Ø3.05 mm,
no separate collar, and an actual bare Duo available for testing.

**The existing fit-coupon 3MF is superseded for this hardware.**
It and `iPhone-Duo-Plate/add_magsafe_pocket.py` still use the previous smaller
cable channel and unvalidated seating/retention assumptions. Do not print that
file as the next fit test. No corrected CAD was generated in this checkpoint.

Next: measure the magnet center directly with the puck attached to the phone.
The governing plan defines A/B measurements and the coordinate conversion.
Protected bare-phone support locations and cable exit height also remain open.

The revised sequence is physical measurements, shared geometry correction,
independent bore/cable coupons, actual phone-removal and charging tests, then
the full plate and requested grille. The source
`iPhone-Duo-Plate/iPhone Duo Plate 260 sloped.3mf` remains unchanged.
Generated artifacts belong in `output/iphone-duo/`.

After the script has been corrected and reviewed, its build entrypoints are:

```bash
uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --coupons
uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --plate
```

Running these commands now reproduces the superseded geometry; a successful
build does not establish fit for the measured charger. The revised plate is
not print-ready. Structural connections, minimum material widths, support
contact, and physical fit remain unverified.
