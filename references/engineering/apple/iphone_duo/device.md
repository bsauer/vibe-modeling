# iPhone Duo — device envelope and keepouts

Primary: [Apple iPhone Duo Technical Specifications](https://www.apple.com/iphone-duo/specs/),
[Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/).
Full narrative: `reports/iPhone Duo accessory design.md`.

## Size and weight (Apple official)

| State | Height | Width | Depth | Mass |
|---|---|---|---|---|
| Open | 117.8 mm (4.64 in) | 164.6 mm (6.48 in) | 5.2 mm (0.21 in) | 254 g |
| Closed | 117.8 mm (4.64 in) | 84.1 mm (3.31 in) | 11.3 mm (0.44 in) | 254 g |

Closed is short/wide (“passport”); open is landscape-dominant. Tall MagSafe
wallets sized for conventional iPhones overhang the **117.8 mm** short edge.

### Provisional bump keepout

PhoneArena lists ~**10.4 mm** open thickness including camera bump. Method
undocumented — provisional keepout only until calipers or Apple ARD exist.

## Displays and materials (context)

| Item | Apple claim |
|---|---|
| Inner OLED | Marketed 7.6″ (rect. 7.58″), 1878×2670 @ 430 ppi, nano-texture |
| Outer OLED | Marketed 5.4″ (rect. 5.36″), 1398×2034 @ 460 ppi |
| Enclosure | Grade 5 titanium; Ceramic Shield 2 outer front; Ceramic Shield back |
| Hinge cover | 3D-printed titanium |
| Sealing | IP68 (6 m / 30 min IEC 60529) |
| Colors | Night Sky, Star White |
| Models | A3447 (US); regional A3719 / A3720 / A3721 |
| FCC | Parent BCG-E9188A (A3447) |

Ignore pre-announce rumor thicknesses (~9–9.5 mm folded) — obsolete vs Apple.

## MagSafe / Qi2 on the phone

Apple confirms:

- MagSafe wireless charging up to **25 W**
- Qi2 wireless charging up to **25 W** (or Qi-certified chargers)
- Hardware: magnet array, alignment magnet, Accessory Identification NFC,
  magnetometer

Apple does **not** publish Duo magnet-ring center coordinates or OD on-phone.

### Placement rule (hands-on consensus)

The MagSafe/Qi2 charging face is on the **rear camera half only** (under the
camera plateau). The other outer face is the cover display. Hinge **closure**
magnets are a separate array — do not treat them as MagSafe.

### Stand stability

When **open**, upright MagSafe pucks can tip from asymmetric mass. Prefer:

- Closed upright MagSafe, or
- Flat pads, or
- Open cradles with a **ledge** under the non-magnet half

## Qualitative keepouts (no Duo ARD mm yet)

Leave clear until Duo dimensional drawings publish:

- Camera plateau + flash (rear dual 48 MP Fusion Main + Ultra Wide)
- Outer 12 MP Center Stage camera
- Inner under-display FaceTime camera
- USB-C (bottom), stereo speakers / mics
- Top volume buttons
- Right-side Touch ID side button + Camera Control
- Full **hinge spine** / titanium hinge cover (no crush clamps)
- MagSafe rear attach face
- eSIM only — no SIM tray cutout needed

## Technical drawings status

| Artifact | Status (2026-10-22) |
|---|---|
| Apple Size and Weight | Public |
| Accessory Design Guidelines PDF | Public (general MagSafe; Duo not named in device lists) |
| Public Duo dimensional drawings | **Not** on [dimensional-drawings index](https://developer.apple.com/accessories/dimensional-drawings/) |
| Partner manufacturer drawings | Reported gated (Engadget) |
| MagSafe Charger puck drawings | Public (charger, not phone) |
| developer.apple.com/iphone-duo | App/SDK layout — not mechanical ARD |

## Obsolete / unreliable for CAD

- Pre-launch fold thickness rumors
- PhoneArena display pixel count conflicting with Apple (use Apple)
- Unofficial battery mAh aggregators
- Printables / MakerWorld “Duo” models that only reuse overall mm — visualization
  only
- Models titled “MagSafe Duo” that mean Apple’s **discontinued dual MagSafe
  desk charger**, not this phone
