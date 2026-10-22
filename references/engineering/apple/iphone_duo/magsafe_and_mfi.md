# MagSafe Attach, MFi, and Qi2 for Duo accessories

Primary public mechanical source: Apple **Accessory Design Guidelines for Apple
Devices**, updated **2026-09-21** —
[PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf),
[Accessories hub](https://developer.apple.com/accessories/).

iPhone Duo is MagSafe + Qi2 **25 W** on the phone. As of the Guidelines extract
used for this note, Duo was **not yet named** in MagSafe/Qi device lists — use
general MagSafe Attach geometry plus Duo Size and Weight until Duo sheets appear.

This page is engineering guidance, **not legal advice**.

## What is public vs gated

| Content | Access |
|---|---|
| MagSafe Attach magnet Ø, grades, pull force, keep-ins (§42) | **Public** PDF |
| MagSafe Charger Mounts (§22) | **Public** PDF |
| Device Power Inductive / Qi transmitter shall-rules (§37) | **Public** PDF |
| MagSafe Charger dimensional drawings | Public download index |
| Duo phone dimensional drawings | **Not** on public index (2026-10-22) |
| Full Qi v2.3 / test books | WPC **members only** (older public zip exists) |
| MFi royalties / MagSafe charger licensing details | **NDA** after program approval |

## MagSafe Attach — key public numbers (§42)

Case and accessory magnet rings (figures in Guidelines):

| Parameter | Value |
|---|---|
| Outer diameter | **54.10 mm** |
| Inner diameter | **46.00 mm** |
| Case magnets | N45SH NdFeB; surface gauss ≤ **0.215 T** |
| Accessory magnets | N48H NdFeB; surface gauss ≤ **0.215 T** |
| Self-alignment | ≤ **1.55 mm** radial |
| Case pull (to charger-class accessory) | **1000–1300 gf** normal to case back |
| Accessory pull (to device) | **650–1510 gf** (config-dependent) |
| MagSafe / Qi 2.0+ **case** rear over array | Uniform thickness ≤ **2.1 mm** (recommend **2.0 mm**) |
| Dock-related case bottom buildup | ≤ **1.8 mm** for dock compatibility |
| Accessory keep-in | Magnetic attach surface ≤ **30 mm** from ring center toward top in supported orientations; **6 mm** clearance beyond keep-in |

Orientation magnet and polarity cross-sections are figure-defined in the PDF
(case orientation magnet width **6.00 mm**, magnet thickness **0.55 mm**, etc.).
Read figures 42-2 through 42-7 directly for production CAD.

Cases claiming MagSafe or Qi wireless power **2.0+** shall integrate the MagSafe
Case Magnet Array, enclose the device, and must not use rear card pockets
(§5.1.4 / §42.1).

## MagSafe Charger Mounts (§22)

Stands/docks that **hold Apple’s MagSafe Charger puck** (rather than integrating
a coil) follow Chapter **22** keep-ins from MagSafe Charger dimensional drawings.

Measured 25W MagSafe Charger (A2580) panel ≈ **Ø 55.4–55.5 mm**, thickness ≈
**4.45–4.53 mm** (ChargerLAB) — useful for puck bore design; prefer Apple’s
charger drawings for authoritative keep-ins.

## MFi scope (FAQ)

From [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html):

- MFi covers accessories using **licensed MFi technologies/components**.
- **Protective cases and folios that do not integrate MFi components are outside
  MFi.**
- Developers of **non-electronic** accessories need not join; Apple points them
  to the Accessory Design Guidelines.
- Program fee listed publicly as **USD $99**/year; royalty details under NDA.

Market language: **“MagSafe compatible”** (magnets) ≠ **“Made for MagSafe”**
(licensed MagSafe charging path).

## Qi2 relationship

- WPC Qi2 Magnetic Power Profile is the industry MagSafe-class magnetic standard.
- Qi2 **25 W** launched with Qi v2.2.1 (July 2025 marketing); full latest Qi
  specs are largely member-gated.
- Apple Guidelines: inductive transmitters shall be Qi Certified (v2.0+;
  recommend v2.2+).
- Duo marketing: MagSafe **and** Qi2 25W / Qi-certified chargers.

## Practical matrix for this host’s printed accessories

| Accessory type | Typical path |
|---|---|
| 3D-printed stand holding a MagSafe **puck** | Guidelines **§22**; no MFi for pure mechanics |
| Passive magnet wallet / mount | Guidelines **§42.2**; no MFi if non-electronic |
| MagSafe-compatible case (magnets only) | **§42.1**; MFi not required solely for magnets |
| Integrated Qi2/MagSafe **charger** product | WPC Qi cert + EMC/FCC; MagSafe branding/licensing separate |
| MagSafe NFC / Find My features | Likely Apple program / MFi-related — gated |

## Medical / magnet hygiene

Apple Support advises keeping magnets and wireless chargers away from implanted
medical devices (typical guidance distances on support pages). Document
warnings on commercial mounts.

## Related host pages

- `device.md` — Duo envelopes and camera-half MagSafe rule
- `cases.md` — Folio under-kickstand charging vs Duo Case
- `references/tooling/` — printer/slicer notes for fabricating mounts
