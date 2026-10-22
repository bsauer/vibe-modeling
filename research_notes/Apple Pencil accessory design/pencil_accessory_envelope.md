# Apple Pencil accessory design (holders, docks, cases, storage)

Research as-of: **2026-10-22**. Separate **Apple-official** claims from **measured / third-party** (low confidence). Cross-check product envelopes with sibling notes `current_pencil_lineup.md` in this folder.

---

## Does iPhone Duo officially support Apple Pencil? Which Pencil models?

### Takeaway
**Yes — Apple officially lists only Apple Pencil (USB-C)** for iPhone Duo. Pro, Gen2, and Gen1 are not listed for Duo. Support is productized as display support with a marketing caveat that enablement is “Coming later this year” (calendar 2026).

### Cited Findings
- Duo specs (Both displays): “Supports Apple Pencil (USB-C)” with footnote **3** — [iPhone Duo Technical Specifications](https://www.apple.com/iphone-duo/specs/).
- Duo marketing FAQ (reported/quoted by secondary press from apple.com/iphone-duo): “Does iPhone Duo work with Apple Pencil or a stylus? Yes. iPhone Duo will work with Apple Pencil (USB‑C). Coming later this year.” — [The Mac Observer](https://www.macobserver.com/news/iphone-duo-apple-pencil-usb-c/); FAQ claim also reflected in search snippets for [apple.com/iphone-duo](https://www.apple.com/iphone-duo/).
- Newsroom (2026-09-09): “Later this year, iPhone Duo will support Apple Pencil with USB-C, allowing users to take notes, sketch, or mark up documents on either display.” — [Apple Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/).
- USB-C Pencil Compatibility lists **iPhone Models → iPhone Duo** (plus iPads) — [Support 121318](https://support.apple.com/en-us/121318); [shop MUWA3AM/A](https://www.apple.com/shop/product/muwa3am/a/apple-pencil-usb-c).
- Pencil Pro / Gen2 / Gen1 tech-specs list **iPad models only** (no iPhone) — [Support 120123](https://support.apple.com/en-us/120123); [111889](https://support.apple.com/en-us/111889); [111920](https://support.apple.com/en-us/111920).
- Apple Support “Apple Pencil compatibility” ([108937](https://support.apple.com/en-us/108937), published 2026-03-10) lists **only iPads** for all four pens and **omits iPhone Duo** — conflicts in scope with USB-C tech specs / Duo specs.
- Secondary (not Apple): hover allegedly present in iOS 27 presentation code; enablement rumors around iOS 27.2 — [r/iPhoneDuo](https://www.reddit.com/r/iPhoneDuo/comments/1wxykjw/iphone_duo_supports_apple_pencil_hover_according/); [Ground.news aggregate](https://ground.news/article/iphone-duo-adding-apple-pencil-support-next-week-with-ios-272). Treat as unverified vs Apple primary.

### Inferences
- Duo-facing docks/holders should assume **USB-C Pencil only**: cable charge via sliding USB-C end, **no** iPad-style magnetic wireless charge on the phone.
- Duo MagSafe/Qi2 is on the **rear camera half** (see host `references/engineering/apple/iphone_duo/device.md`); that is **not** a Pencil attach/charge rail. Do not design as if Duo has iPad edge Pencil magnets.
- Prefer USB-C tech specs + Duo specs over the older iPad-only [108937](https://support.apple.com/en-us/108937) article when deciding phone compatibility.

### Gaps
- Exact live OS build / ship date when Duo Pencil input is enabled was not confirmed on an Apple Support KB as of this research (FAQ/Newsroom: “later this year”).
- Apple has not published whether Duo gets hover, pressure (USB-C lacks pressure anyway), or palm-rejection details beyond “Supports Apple Pencil (USB-C).”
- No Apple claim that Pencil Pro works on Duo.

---

## How do iPad side magnets interact with Pencil Pro / USB-C attach for dock design?

### Takeaway
**Pro and Gen2** use the iPad’s long-edge magnet array to **attach, pair, and wirelessly charge**. **USB-C** uses the same edge magnets for **storage only** (pairs/charges over USB-C cable). Dock/case design must keep the Pencil **flat magnetic face** free of thick or ferromagnetic material if on-device attach/charge is required; standalone desk holders can ignore wireless charge.

### Cited Findings
- **Pro:** “attaches, pairs, and charges magnetically on the side of your iPad”; Other Features: “Magnetically attaches, pairs and charges” — [Support 120123](https://support.apple.com/en-us/120123).
- **USB-C:** “pairs and charges via a USB-C Charge Cable”; “magnetically attaches to the side of iPad for **storage**”; feature matrix: wireless pairing and charging **not** supported — [Support 121318](https://support.apple.com/en-us/121318); [apple.com/apple-pencil](https://www.apple.com/apple-pencil/); [shop](https://www.apple.com/shop/product/muwa3am/a/apple-pencil-usb-c).
- **Gen2:** “pairs, charges, and stores magnetically” — [Support 111889](https://support.apple.com/en-us/111889).
- **Gen1:** no side-of-iPad magnetic charge; “Magnetically attached **cap**” only — [Support 111920](https://support.apple.com/en-us/111920).
- Pair/charge USB-C procedure: slide open end, connect USB-C charge cable to Pencil and to iPad (or adapter) — [iPad User Guide](https://support.apple.com/guide/ipad/pair-and-charge-apple-pencil-usb-c-ipadc3d88218/ipados).
- Community confirmation that USB-C magnets are hold-only / no battery widget from edge attach — [r/ipad](https://www.reddit.com/r/ipad/comments/1cultml/does_usbc_pencil_attach_to_2024_pro_magnetically/) (measured/user report, low confidence).
- Printables sleeve designed to stay on while Pencil remains magnetically attached to Magic Keyboard / Folio / Smart Folio, with tip-protecting cavity; separate shorter STL for USB-C length — [Printables 1793197](https://www.printables.com/model/1793197-apple-pencil-sleeve-2nd-generation-pro-usb-c) (designer claim).

### Inferences
- **On-iPad docks / case Pencil loops:** preserve a continuous **flat-to-flat** couple between Pencil flat and iPad edge. Any sleeve wall over the flat face that adds thickness or ferrous content risks **weak attach** and, for Pro/Gen2, **blocked wireless charge**.
- **USB-C on-iPad storage docks** still need magnet alignment/retention, but **must also leave the sliding USB-C end operable** for actual charging (see USB-C cap section).
- **Duo / phone docks:** no Apple-documented Pencil edge magnets on Duo; treat Pencil storage as a **mechanical** problem (clip, pocket, cradle), not MagSafe-aligned Pencil charging.
- Length envelopes for side-rail clips: Pro/Gen2 **166 mm**, USB-C **155 mm**, Gen1 **175.7 mm** tip-to-cap — Apple Support tech-specs (see lineup notes). A single “one size” rail often fails USB-C (short) vs Gen1 (long).

### Gaps
- Apple does **not** publish Pencil magnet pitch, flat-face chord width, attach force, or keepout drawings in public ADG excerpts reviewed for this note.
- Accessory Design Guidelines PDF was scanned for Pencil **accessory** chapters: **no dedicated Pencil holder/dock chapter** found; Pencil appears mainly under **screen overlays** (below).

---

## Best practices for 3D-printed Pencil sleeves/clips without demagnetizing or blocking charge

### Takeaway
PLA/PETG/TPU themselves do **not** demagnetize Pencil/iPad magnets; the practical failure mode is **intervening thickness / ferrous hardware** over the flat charge face, or covering double-tap/squeeze zones. Third-party grip makers explicitly say **remove grips before magnetic charging** Pro/Gen2. ADG only constrains **screen overlays** for Pencil performance (≤ **0.095 mm**), not barrel sleeves.

### Cited Findings
- **Apple ADG (official):** Screen overlays must not degrade Multi-Touch, **Apple Pencil**, or sensors; should not exceed **0.095 mm** thickness to support Apple Pencil; non-glossy overlays may accelerate tip wear; relative permittivity guidance 3.1–3.2 — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) (Section 7 Screen Overlays; scrape of first ~100 pages). **No Pencil sleeve/clip dimensional chapter** located in that scrape.
- UPPERCASE NimbleGrip (fits 8.8–9.2 mm styluses; Pro/USB-C/Gen1/Gen2): “Apple Pencil Pro/Gen 2 **cannot be charged with any case or grip installed**. Simply remove the grip before charging…”; leave ~½ in exposed for double-tap on Pro/Gen2 — [gouppercase.com/nimblegrip](https://gouppercase.com/products/nimblegrip).
- Paperlike Pencil Grips marketing: claims grips “won’t interfere” with magnetic charging on Gen2 / related models — [Paperlike](https://paperlike.com/products/pencil-grips) (vendor claim; conflicts with UPPERCASE “remove grip” guidance).
- Many silicone grips are sold as “Support Magnetic Charging” with cutouts / thin flats (e.g. YINVA listings) — [Amazon example](https://www.amazon.com/Ergonomic-Designed-Generation-YINVA-Compatible/dp/B09L7XKL9K) (marketing, low confidence).
- NimbleGrip 2 “Tap-n-Charge” cutout exposes touch surface for magnetic charging — [UPPERCASE NimbleGrip 2](https://gouppercase.com/products/nimblegrip-2-ergonomic-grip-with-tap-n-charge-for-apple-pencil) (vendor claim).
- Printables tip-guard sleeve: PETG recommended; 5 fit variants for printer tolerance; must still magnetically attach with Apple cases; USB-C gets unique shorter files — [Printables 1793197](https://www.printables.com/model/1793197-apple-pencil-sleeve-2nd-generation-pro-usb-c).
- Tip crush / impact: same Printables model exists specifically because tip + sensors are vulnerable when Pencil is perched on iPad edge — [Printables 1793197](https://www.printables.com/model/1793197-apple-pencil-sleeve-2nd-generation-pro-usb-c); related “saves your tip” holders — [Printables 413978](https://www.printables.com/model/413978-apple-pencil-holder-that-saves-your-tip/comments).

### Inferences (practical design rules for printables)
1. **Magnetic charge (Pro/Gen2):** Prefer **open C-clip / flat cutout** over full cylindrical sleeve if the Pencil must charge on-device. If a full sleeve is required, document “remove for charge” like UPPERCASE.
2. **USB-C storage magnets:** Flat cutout still helps retention strength; charge path is the **sliding end**, not the magnets.
3. **Materials:** Non-ferromagnetic plastics (PLA, PETG, TPU) are fine. Avoid steel springs, ferrous screws, or thick metal clips **between** Pencil flat and iPad edge. Embedded neodymium in a *standalone* holder is fine; on-iPad, extra magnets can fight Apple’s array—test.
4. **“Demagnetizing”:** Normal 3D-printed sleeves do not demagnetize. Blocking charge ≠ demagnetizing.
5. **Find My / haptics / squeeze (Pro):** Irrelevant to passive storage geometry. For *in-use grips*, leave squeeze/double-tap zones free; Find My needs no published RF cutout for holders.
6. **Roll-away:** Gen1 is fully round—add flats/hex. Pro/Gen2/USB-C have a flat face but still roll; anti-roll geometry helps desk stands.
7. **Tip crush:** Prefer tip-up storage, tip cavities with clearance, or soft stops—do not jam the tip into a hard blind hole.

### Gaps
- No Apple-published barrel sleeve keepouts, dielectric limits for grips, or “maximum non-ferrous thickness over charge face.”
- Conflicting third-party claims (Paperlike “won’t interfere” vs UPPERCASE “remove to charge”)—**measure charge current / Batteries widget** on any candidate sleeve; do not trust marketing alone.

---

## Tip spare storage dimensions

### Takeaway
Apple sells a universal **Tips – 4 pack** (`MX763AM/A`, $19) for all four current Pencils but **publishes no tip OD, length, or thread**. Spare cavities must be sized from **calipers or low-confidence third-party numbers**; treat printed tip boxes as provisional until measured.

### Cited Findings
- Official tips: compatible with Pro, Gen2, USB-C, Gen1; box contains four tips — [Apple Pencil Tips 4-pack](https://www.apple.com/shop/product/mx763am/a/apple-pencil-tips-4-pack).
- Gen1 ships with an extra tip in-box — [Support 111920](https://support.apple.com/en-us/111920).
- Serial number for Pro/Gen2/USB-C is under the removable tip — [Support 109031](https://support.apple.com/en-us/109031) (confirms unscrew interface; no thread specs).
- **Measured / vendor (low confidence):**
  - Third-party Amazon tip listing: “**0.8 mm** diameter, **2 mm** length” (writing tip portion claim) — [Amazon B09S631ZK7](https://www.amazon.com/Upgraded-Precise-Control-Replacement-Compatible/dp/B09S631ZK7).
  - Staples product copy: “Approximately **0.04 inches (1 mm)** in diameter” — [Staples listing](https://www.staples.com/apple-replacement-tips-for-apple-pencil-pro-1st-2nd-generation-white-4-pack-mx763am-a/product_IM1S43941).
  - Gridfinity tip holder: holds **9 tips**; no cavity mm in description — [Thangs 843976](https://thangs.com/designer/azcoov/3d-model/Gridfinity%20Apple%20Pencil%20Tip%20Holder%201x1x1.-843976).
  - Etsy tip travel box (overall box ~65 × 20 mm depth claim; not tip cavity) — [Etsy listing](https://www.etsy.com/listing/1783973920/apple-ipad-pencil-tip-storage-and-travel).
  - MakerWorld tip storage box exists without published cavity IDs in scrape — [MakerWorld 587531](https://makerworld.com/nl/models/587531-apple-pencil-tip-storage-box).

### Inferences
- One tip SKU across the lineup ⇒ **one cavity size** can serve all current Pens once measured.
- Writing-nib OD (~0.8–1 mm) is **not** the storage envelope; the plastic tip body/shoulder is larger—**caliper the official tip** before locking a printable cavity.
- Thread pitch/major diameter remain undocumented; do not design threaded tip replicas from Apple docs alone.

### Gaps
- **No Apple-official tip dimensions** (OD, length, thread).
- No trustworthy public caliper dataset found in this pass; Amazon/Staples figures describe the writing point, not the full spare body.

---

## Third-party measured holder IDs (Pro vs USB-C) and diameter conflicts

### Takeaway
**Apple-official:** all four current Pencils share **8.9 mm (0.35 in) diameter**; lengths differ (Pro/Gen2 166 mm, USB-C 155 mm, Gen1 175.7 mm). **There is no Apple-stated Pro-vs-USB-C diameter conflict.** Conflicts come from **secondary sites** (Wikipedia/AppleInsider ~7.4 mm / 0.29 in for USB-C) and from **printer-tolerance holder IDs** (≈9.0–9.5 mm). Design from Apple’s **8.9 mm** + clearance; verify USB-C with a **shorter** axial envelope.

### Cited Findings

**Apple-official diameters / lengths**
- Pro: Ø **8.9 mm**, L **166 mm** — [Support 120123](https://support.apple.com/en-us/120123).
- USB-C: Ø **8.9 mm**, L **155 mm** — [Support 121318](https://support.apple.com/en-us/121318); [shop](https://www.apple.com/shop/product/muwa3am/a/apple-pencil-usb-c).
- Gen2: Ø **8.9 mm**, L **166 mm** — [Support 111889](https://support.apple.com/en-us/111889).
- Gen1: Ø **8.9 mm**, L **175.7 mm** tip-to-cap — [Support 111920](https://support.apple.com/en-us/111920).

**Contradicting secondary diameter claims (do not use for CAD)**
- Wikipedia: USB-C diameter **0.29 in (7.4 mm)** — [Wikipedia · Apple Pencil](https://en.wikipedia.org/wiki/Apple_Pencil); contradicted by Apple **8.9 mm**.
- AppleInsider comparison text: USB-C “At **0.29 inches**, its diameter…” — [AppleInsider](https://appleinsider.com/inside/apple-pencil/vs/ultimate-showdown-new-apple-pencil-usb-c-vs-old-apple-pencils); contradicted by Apple.

**Third-party holder / grip IDs (measured or stated; low confidence)**
- UPPERCASE NimbleGrip: fits styluses **8.8–9.2 mm**; lists Pro/USB-C/Gen1/Gen2 — [NimbleGrip](https://gouppercase.com/products/nimblegrip).
- MakerWorld SKÅDIS holder (Oct 2026): “Apple Pencil Pro or others with diameter **&lt;9.5 mm**”; warns printer tolerances affect fit — [MakerWorld 3423180](https://makerworld.com/en/models/3423180-skadis-apple-pencil-pro-holder-minimalist-design).
- Printables RAM-mount stylus holder: author’s stylus **9.5 mm** OD (believed slightly smaller than Apple Pencil); PETG may still fit Pencil — [Printables 207822](https://www.printables.com/model/207822-ram-mount-stylus-apple-pencil-holder?lang=cs).
- Reddit shrink-tube advice: Pencil ~**8.9 mm** → buy **9 mm or 10 mm** heat-shrink — [r/ipad](https://www.reddit.com/r/ipad/comments/l5g00q/had_a_problem_with_the_apple_pencil_being_too/).
- Printables sleeve: “5 fits” for printer variance; USB-C **unique shorter files** (length conflict, not diameter) — [Printables 1793197](https://www.printables.com/model/1793197-apple-pencil-sleeve-2nd-generation-pro-usb-c).
- Walmart/Amazon clip listings: “touch pens below **9 mm** diameter” marketed for Gen1/2 — [Walmart example](https://www.walmart.ca/en/ip/MasteelfCA-Stylus-Pen-Holder-Compatible-for-Apple-Pencil-1-2-Silicone-Touch-Pen-Slot/56KEH48HHILX).

### Inferences
- **Pro vs USB-C:** same official OD; **do not** fork diameter for Pro vs USB-C. Fork **length** (155 vs 166 mm) and **charge UX** (magnetic vs sliding USB-C).
- Practical printable **ID starting points** (third-party consensus, not Apple): ~**9.0–9.2 mm** slip fit; ~**9.3–9.5 mm** loose/drop-in; always print a clearance coupon.
- Gen1 needs extra axial room for **removable Lightning cap** travel/storage; USB-C needs **sliding end** clearance (not a free cap).
- Still-sold lineup (Apple shop select): Pro, USB-C, plus links to Gen1 and Gen2 — [Select Apple Pencil](https://www.apple.com/shop/select-apple-pencil).

### Gaps
- Few Printables/MakerWorld pages publish **exact CAD ID** (e.g. “ID = 9.15 mm”); most state “&lt;9.5 mm” or sell multi-fit variants.
- Flat-face chord / D-section dimensions unpublished—round-hole holders ignore clocking; magnetic docks need flat orientation features.

---

## USB-C sliding end / Gen1 cap travel (accessory pitfall)

### Takeaway
USB-C Pencil charges only after **sliding open the end cover** and connecting USB-C; full-length closed sleeves or sealed end caps that trap that slide will block charging. Gen1 uses a **removable** Lightning cap (different failure mode: lost-cap pockets).

### Cited Findings
- Pair/charge steps explicitly: “**Slide open** the end of Apple Pencil and connect it to the USB-C charge cable…” — [iPad User Guide](https://support.apple.com/guide/ipad/pair-and-charge-apple-pencil-usb-c-ipadc3d88218/ipados).
- Shop copy: pairs and charges via USB-C Charge Cable; magnetically attaches for storage — [shop MUWA3](https://www.apple.com/shop/product/muwa3am/a/apple-pencil-usb-c).
- Third-party USB-C sleeve marketed with pocket so you can charge “without losing the cap” — [UPPERCASE NimbleSleeve](https://gouppercase.com/products/nimblesleeve-silicone-protective-sleeve-apple-pencil-usb-c) (implies sliding cover is a retention problem).
- Gen1: magnetically attached **cap** over Lightning; length measured tip-to-cap — [Support 111920](https://support.apple.com/en-us/111920).

### Inferences
- Holder IDs that fit the barrel can still fail if they **collar the sliding end**. Leave ≥ one end open, or provide a slot aligned with the slide.
- Duo docks storing USB-C Pencil must allow cable charge somewhere (pocket USB-C, pass-through, or remove-to-charge).

### Gaps
- Apple does not publish slide travel (mm) or end-cap outer length beyond overall Pencil length.

---

## Design-pitfall checklist (synthesis)

| Pitfall | Official basis | Practical note |
|--------|----------------|----------------|
| Blocking magnetic **charge** | Pro/Gen2 charge only via side magnets | Flat cutout / remove sleeve; USB-C magnets don’t charge |
| Blocking magnetic **attach** | Pro/Gen2/USB-C store on iPad edge | Keep flat face free of thick/ferrous material |
| Tip crush | Tip is replaceable wear item; sensors behind tip | Tip cavity / tip-up storage |
| Roll-away | Gen1 round; others mostly round + flat | Anti-roll flats/hex on desk stands |
| USB-C end travel | Must slide open to charge | Don’t trap sliding cover |
| Find My / haptics / squeeze | Pro-only features | Irrelevant to passive holders; free zones only for in-use grips |
| Duo Pencil model mix-up | Duo = USB-C only | Don’t design Duo accessories for Pencil Pro |
| Diameter fork Pro vs USB-C | Apple: both 8.9 mm | Fork **length** and charge UX, not OD |
| Screen protector kills Pencil | ADG ≤0.095 mm for Pencil | Duo/iPad case overlays must respect ADG if Pencil used |
| Secondary 7.4 mm USB-C OD | Contradicts Apple | Ignore for CAD |

---

## Source confidence legend

- **Apple-official:** Support tech-specs, shop, Duo specs/Newsroom, ADG PDF.
- **Secondary press:** Mac Observer, AppleInsider, Wikipedia — use only when flagged as conflicting or timing color.
- **Measured / maker (low confidence):** Printables, MakerWorld, UPPERCASE, Amazon/Staples tip copy, Reddit.
