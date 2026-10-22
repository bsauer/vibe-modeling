# iPhone Duo accessory design reference

Research checkpoint: **2026-10-22**. Apple announced iPhone Duo **2026-09-09**;
retail window late October 2026.

## Purpose

Give CAD and print designers a single host index for:

1. Bare-phone open/closed envelopes and keepouts
2. Apple’s two official cases (Folio with Kickstand; Duo Case)
3. Public MagSafe Attach / MFi / Qi2 rules that apply to docks and mounts

## Quick CAD facts (Apple-confirmed unless noted)

| Item | Value | Source class |
|---|---|---|
| Open envelope | **117.8 × 164.6 × 5.2 mm** | Apple specs |
| Closed envelope | **117.8 × 84.1 × 11.3 mm** | Apple specs |
| Mass | **254 g** | Apple specs |
| Wireless | MagSafe + Qi2 up to **25 W** | Apple specs |
| MagSafe location | **Camera-half rear only** | Consensus / hands-on (not mm-coord published) |
| Folio SKUs | MKR64ZM/A Taupe, MKR74ZM/A Navy Blue ($129) | Apple Store |
| Duo Case SKUs | MKR84ZM/A Navy Blue, MKR94ZM/A Sand ($79) | Apple Store |

## Design rules of thumb

1. Model **two phone poses** (open book vs closed passport), not one slab.
2. Treat **Folio** and **Duo Case** as **two dock envelopes**, not one
   “works with Apple cases” claim.
3. Prefer **closed** upright MagSafe mounting; open MagSafe needs a ledge under
   the non-magnet half or the stand tips.
4. Folio docks must leave MagSafe clearance **behind the open kickstand**.
5. Case docks must leave the **exposed titanium hinge** free; do not clamp it.
6. Use public MagSafe Attach ring Ø **54.10 / 46.00 mm** from Apple’s Accessory
   Design Guidelines for magnet pockets; Duo-specific ARDs were not public as of
   this checkpoint.

## Pages in this folder

- `device.md` — chassis, displays, ports, MagSafe placement, drawing gaps
- `cases.md` — Folio vs Case construction, charging paths, dock failure modes
- `magsafe_and_mfi.md` — Guidelines §42 / §22, MFi scope, Qi2 relationship

## Confidence

| Topic | Confidence |
|---|---|
| Apple Size and Weight | High |
| MagSafe Attach public magnet geometry | High (Guidelines PDF 2026-09-21) |
| Camera-half-only MagSafe | High (multiple hands-on; Apple silent on mm) |
| Official case installed thickness | **Unknown** — do not use Amazon package dims |
| Duo dimensional drawings (ARD) | **Missing** from public index |
| Kickstand angles | Low (~90° one review; Apple says “range”) |

Update this tree when Apple publishes Duo dimensional drawings or measured
phone-plus-case stack-ups.
