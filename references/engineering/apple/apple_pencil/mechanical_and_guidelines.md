# Apple Pencil — mechanical envelopes and guidelines

Checkpoint **2026-10-22**. Prefer Apple Size and Weight; treat community holder
IDs as provisional until calipered on your hardware.

## Official outer envelopes

| Model | Length | Diameter | Notes |
|---|---|---|---|
| Pro | 166 mm | 8.9 mm | Flat magnet face for edge attach |
| USB-C | 155 mm | 8.9 mm | Sliding end cap for USB-C; shorter body |
| 2nd gen | 166 mm | 8.9 mm | Same length/Ø class as Pro |
| 1st gen | 175.7 mm tip-to-cap | 8.9 mm | Removable cap over Lightning |

**Do not use** Wikipedia / some secondary articles claiming USB-C Ø **7.4 mm**.

## Public Accessory Design Guidelines (Pencil)

Apple **Accessory Design Guidelines** (R31 / 2026-09-21 PDF) mention Pencil
primarily for **screen overlays**:

- Overlay thickness for Pencil use: ≤ **0.095 mm** (Guidelines extract)

There is **no** public chapter for Pencil barrel mounts, tip threads, or Pencil
magnet arrays comparable to MagSafe Attach §42.

Device-side Pencil / stylus magnet keepouts, if any, live on **iPad**
dimensional drawings — not on a Pencil ARD. No Pencil PDFs were found on the
public [dimensional-drawings index](https://developer.apple.com/accessories/dimensional-drawings/).

MFi / AIS may hold additional stylus specs under NDA — treat as inaccessible
here.

## Tips

- Official 4-pack fits Pro, USB-C, 2nd gen, and 1st gen.
- Tips unscrew; geometry (OD, length, thread) **unpublished**.
- Spare-tip cavities in CAD: measure a tip before locking print dimensions.

## Magnetic attach design rules

| Model | Edge magnets do | Sleeve / clip implication |
|---|---|---|
| Pro / 2nd gen | Attach + pair + wireless charge | Leave flat face exposed or removable; thick/ferrous covers can block charge |
| USB-C | Attach for **storage** only | Charge needs sliding USB-C clearance; magnets don’t charge |
| 1st gen | Cap magnet only | Design for Lightning/adapter cable access, not iPad-edge charge |

Plastics alone do not “demagnetize” the pen; the failure mode is **covering** the
charge face or preventing seating on the iPad’s magnetic connector.

## Holder clearances (community — low–medium confidence)

No Apple-published holder ID. Maker guidance clusters roughly:

- Rigid printed sleeve ID ≈ **9.1–9.5 mm** over 8.9 mm barrel (tolerance-dependent)
- Length stop: design for **155 mm** (USB-C) vs **166 mm** (Pro/2nd) vs **175.7 mm** (1st) separately, or the longest if one holder must fit all

Always measure your target Pencil before freezing a press-fit.

## Gaps for precision CAD

| Item | Status |
|---|---|
| Flat chord width / magnet spacing | Unpublished |
| USB-C slider travel | Unpublished |
| Tip thread / OD | Unpublished |
| Pencil dimensional drawings | None public |
| Attach force / wireless charge power | Unpublished |

## Related

- Lineup/compatibility: `lineup.md`
- MagSafe phone docks (different system): `../iphone_duo/magsafe_and_mfi.md`
- Duo + Pencil USB-C: `../iphone_duo/device.md` and Duo specs
