# Apple Pencil mechanical envelopes, tip geometry, magnet attach, and Accessory Design Guidelines (late October 2026)

Research as-of: 2026-10-22. Focus: Apple Pencil Pro and Apple Pencil (USB-C); Gen1/Gen2 included because both remain sold and share tip / magnet commons with current models. NDA/MFi-gated content is marked inaccessible rather than invented.

Models still listed for sale on Apple’s Pencil overview as of this research: Pencil Pro ($129), Pencil (USB-C) ($79), Pencil (2nd generation) ($129), Pencil (1st generation) ($99). — [Apple Pencil overview](https://www.apple.com/apple-pencil/)

---

## Does Accessory Design Guidelines PDF cover Pencil mounts / tip / magnet keepouts?

### Takeaway
Public Accessory Design Guidelines (Release R31, updated 2026-09-21) mention Apple Pencil only for screen-overlay performance and tip wear—not Pencil body mounts, tip threads, or Pencil-side magnet keepouts. Useful Pencil-related geometry lives on **iPad** dimensional drawings (device-side magnet / flux keep-outs), not on a Pencil drawing package.

### Cited Findings
- Accessory Design Guidelines for Apple Devices is publicly downloadable; page states updated September 21, 2026. — [Accessories – Apple Developer](https://developer.apple.com/accessories/); [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- Guidelines address physical compatibility with iPhone, iPad, Apple Watch, AirPods, Apple TV, Apple Vision Pro, and Mac; some accessory interaction aspects “may require access to the Apple MFi Program and the Accessory Interface Specification.” — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- Screen overlays shall not degrade Multi-Touch, Apple Pencil, or sensors; should not exceed 0.095 mm thickness to support Apple Pencil; non-glossy surfaces may accelerate Apple Pencil tip wear. — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) §7 Screen Overlays
- Accessory trackpads shall not degrade Multi-Touch or Apple Pencil performance. — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) §15.1.3
- Grep of the R31 PDF text found no dedicated chapters for Apple Pencil mounts, Pencil tip dimensions, Pencil magnet arrays, or Pencil holder clearances (only overlay/trackpad coexistence mentions above). — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- MagSafe / Qi magnetic-attach and flux-clearance rules in the Guidelines apply to MagSafe/Qi accessories, not to Apple Pencil side-mount charging. — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- iPad Pro 13-inch (M5) dimensional drawings include magnet detail, polarity tables, and magnetic-flux keep-outs (e.g., “MAGNETIC FLUX KEEP-OUT 3MM THICK… MAXIMUM 0.25mT IN CROSS-HATCHED REGION”; “MAXIMUM 5mT IN HATCHED REGION”; keep-out zones extending above/below product thickness). These are **device-side** accessory constraints for cases/covers near the long-edge magnet array used with Pencil. — [iPad Pro 13-inch (M5) dimensional drawing PDF](https://developer.apple.com/download/files/accessories/dimensional-drawings/ipad-pro-13-inch-m5.pdf)
- Apple Support pairing guidance: center Pencil Pro / Gen2 on the magnetic connector; if pairing fails, remove cases/covers from the iPad and retry—evidence that third-party cases can block magnetic attach/pairing. — [If you can't pair Apple Pencil with your iPad](https://support.apple.com/en-us/HT205236)

### Inferences
- For designing iPad cases/stands that preserve side-mount Pencil attach/charge, use the matching **iPad** dimensional drawing magnet/flux keep-outs, not the Guidelines’ MagSafe chapters.
- For designing Pencil holders/docks/tip cases, the public Guidelines do not supply Pencil mechanical envelopes; caliper measurement or MFi/NDA specs would be required for certified accessory work.

### Gaps
- Full Magnet Detail callouts on iPad drawings are proprietary CAD sheets; OCR/snippets give flux limits and some coordinates but not a clean, complete public “Pencil docking envelope” table for every iPad. Treat drawing PDFs as primary when designing around a specific iPad SKU.
- Whether MFi Accessory Interface Specification adds Pencil magnet/tip specs is **NDA/gated**—not verified in this research.

---

## Are there public dimensional drawings for any Pencil?

### Takeaway
No. Apple’s public Dimensional Drawings catalog lists iPads, iPhones, Watches, AirPods, MagSafe chargers, Vision Pro, etc., but **no Apple Pencil model**. Official public geometry for Pencils is limited to tech-spec length × diameter × weight.

### Cited Findings
- Dimensional Drawings download index (as fetched 2026-10-22) includes many iPad/iPhone/Watch/AirPods/MagSafe/Vision Pro entries; none named Apple Pencil, Pencil Pro, or Pencil USB-C. — [Download Dimensional Drawings](https://developer.apple.com/accessories/dimensional-drawings/)
- Guidelines §1.1: dimensional drawings are at developer.apple.com/accessories/dimensional-drawings/ and may contain keep-out/keep-in regions for antennas, connectors, controls, sensors, cameras, touchscreens, speakers, etc.—still device-centric, not Pencil products. — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- Official overall envelopes (Apple Support tech specs):
  - **Pencil Pro:** Length 166 mm (6.53 in); Diameter 8.9 mm (0.35 in); Weight 19.15 g (0.68 oz). — [Apple Pencil Pro – Tech Specs](https://support.apple.com/en-us/120123)
  - **Pencil (USB-C):** Length 155 mm (6.10 in); Diameter 8.9 mm (0.35 in); Weight 20.5 g (0.72 oz). — [Apple Pencil (USB-C) – Tech Specs](https://support.apple.com/en-us/121318)
  - **Pencil (2nd generation):** Length 166 mm (6.53 in); Diameter 8.9 mm (0.35 in); Weight 18.2 g (0.64 oz). — [Apple Pencil (2nd generation) – Tech Specs](https://support.apple.com/en-us/111889)
  - **Pencil (1st generation):** Length 175.7 mm (6.92 in) tip-to-cap; Diameter 8.9 mm (0.35 in); Weight 20.7 g (0.73 oz). — [Apple Pencil (1st generation) – Tech Specs](https://support.apple.com/en-us/111920)
- FCC filings exist (photos, not dimensional CAD): Pencil Pro model A2538 / FCC ID BCGA2538 (external/internal photos available); Pencil (USB-C) model A3085 / FCC ID BCGA3085. Schematics/block diagrams often long-term confidential. — [fccid.io BCGA2538](https://fccid.io/BCGA2538); [fccid.io BCGA3085](https://fccid.io/BCGA3085)
- Wikipedia lists USB-C Pencil diameter as 0.29 in (7.4 mm) in one table while Apple Support/store list 8.9 mm—**conflict; prefer Apple**. — contradicted by [Apple Pencil (USB-C) – Tech Specs](https://support.apple.com/en-us/121318); Wikipedia page was seen in search snippets only.

### Inferences
- Treat 8.9 mm diameter and model lengths above as the only Apple-authoritative overall cylinder envelopes for holder bore sizing (before clearance).
- FCC external photos can show flat-face presence and USB-C slider visually but are not a substitute for caliper drawings.

### Gaps
- No public Apple DXF/PDF of Pencil body, tip, flat face, magnet array, or USB-C slider travel.
- iFixit teardowns (Gen1 and related coverage) repeat Apple’s 8.9 × length numbers and show tip screw-off qualitatively; they do not publish a full caliper table for flat width, tip OD, or thread. — [Apple Pencil Teardown – iFixit](https://www.ifixit.com/Teardown/Apple+Pencil+Teardown/52955)

---

## Tip outer diameter, length, thread, and replacement kit specs

### Takeaway
Apple documents tip **compatibility and replacement procedure**, not tip OD, tip length, or thread designation. One official 4-pack tip SKU fits Pro, Gen2, USB-C, and Gen1. Community sources confirm screw-on female tip / male metal prong, with a paper-thin body-to-tip gap when seated correctly—but no reliable published caliper OD/thread pitch was found.

### Cited Findings
- Apple sells “Apple Pencil Tips – 4 pack” (current store listing MX763AM/A; legacy MLUN2AM/A packaging still referenced in retail). Compatible with Apple Pencil Pro, (2nd generation), (USB-C), and (1st generation). Box: four extra tips. No tip OD/length/thread published on the product page. — [Apple Pencil Tips – 4 pack](https://www.apple.com/shop/product/mx763am/a/apple-pencil-tips-4-pack)
- Retail listings give **package** dimensions (~66 × 80 × 15 mm, ~18 g), not tip geometry. — [Officeworks AMLUN2AMA](https://api.officeworks.com.au/shop/officeworks/p/apple-pencil-tips-4-pack-amlun2ama)
- Gen1 ships with an extra tip in-box. — [Apple Pencil (1st generation) – Tech Specs](https://support.apple.com/en-us/111920)
- Replacement method (iFixit / community): unscrew tip counterclockwise; screw new tip onto metal prong clockwise until snug—do not overtighten. — [iFixit Tip Replacement Guide](https://www.ifixit.com/Guide/Apple+Pencil+(1st+Generation)+Tip+Replacement/154444); [Cult of Mac – How to change your Apple Pencil tip](https://www.cultofmac.com/how-to/change-apple-pencil-tip)
- Apple Community guidance: when fitted correctly there should be a tiny gap about the thickness of a sheet of paper between tip and Pencil body; avoid sideways force on the transducer under the tip. — [Apple Community thread](https://discussions.apple.com/thread/255476298)
- Cult of Mac: tips are “dumb plastic widgets”; pressure sensing is in the shaft, not the tip; thread is inside the tip mating a male thread on the Pencil. Same tip family works across generations cited. — [Cult of Mac](https://www.cultofmac.com/how-to/change-apple-pencil-tip)
- iFixit Gen1 teardown: nib unscrews; metal insert inside tip; pressure/angle sensing deeper in the shaft (X-ray shows spring-loaded tip assembly). No published tip OD or thread callout. — [Apple Pencil Teardown – iFixit](https://www.ifixit.com/Teardown/Apple+Pencil+Teardown/52955)
- Third-party “0.78 mm longer” tip claims on marketplace listings are marketing claims, not Apple specs. — e.g. Amazon third-party listing snippets from search (not used as dimensional authority)

### Inferences
- For tip cases / spare-tip trays: design around physical tips from the official 4-pack (measure with calipers); do not invent thread as M2/x without measurement.
- Cross-model tip interchangeability (Pro / Gen2 / USB-C / Gen1) is Apple-confirmed for the official tip pack—useful for shared tip-storage accessories.

### Gaps
- **Tip outer diameter:** no Apple or well-sourced caliper value found.
- **Tip length (exposed cone + threaded barrel):** not published.
- **Thread size / pitch / major diameter:** not published by Apple; no trustworthy independent measurement with method/photos located in this pass.
- Dedicated Apple Support “how to replace tip” KB (historical HT205236 redirect) now resolves to pairing troubleshooting, not tip replacement. — [HT205236](https://support.apple.com/en-us/HT205236)

---

## Magnetic attach face flat section dimensions (Gen2 / Pro / USB-C)

### Takeaway
Apple confirms a matte finish and flat side for magnetic attach (Gen2 / Pro / USB-C) but publishes **no** flat-face width, length, or magnet-array spacing for the Pencil itself. Device-side magnet geometry is in iPad dimensional drawings. One community CAD product assumes ~7.5 mm flat width—label as unverified design assumption, not measured Apple data.

### Cited Findings
- Newsroom (USB-C intro): “matte finish and a flat side that magnetically attaches to the side of iPad for storage”; Gen2 “features a matte finish and flat side that supports magnetic pairing and charging.” — [Apple Newsroom 2023-10-17](https://www.apple.com/newsroom/2023/10/apple-introduces-new-apple-pencil-bringing-more-value-and-choice-to-the-lineup/)
- Pencil Pro: “attaches, pairs, and charges magnetically on the side of your iPad.” — [Apple Pencil Pro – Tech Specs](https://support.apple.com/en-us/120123)
- Pencil (USB-C): magnetically attaches for storage; does **not** wirelessly charge on the magnet (charges via USB-C). — [Apple Pencil (USB-C) – Tech Specs](https://support.apple.com/en-us/121318); [Apple Pencil overview](https://www.apple.com/apple-pencil/)
- Pencil (2nd generation): “Magnetically attaches and pairs” (charges magnetically on supported iPads). — [Apple Pencil (2nd generation) – Tech Specs](https://support.apple.com/en-us/111889)
- Pairing: center Apple Pencil on the magnetic connector on the long side of iPad. — [Pair and charge Apple Pencil Pro](https://support.apple.com/guide/ipad/pair-and-charge-apple-pencil-pro-ipada6b9b799/ipados); [If you can't pair…](https://support.apple.com/en-us/HT205236)
- SpeakCAD ready-made grip sleeve parameters list “width of flat on pencil (mm), matches flat-to-flat” = **7.5 mm**, with 9 mm round bore / 0.1 mm clearance for Pro/Gen2 (8.9 mm diameter, 166 mm length). Presented as editable model defaults, not a lab caliper report. — [SpeakCAD Apple Pencil Pro grip sleeve](https://speakcad.com/library/apple-pencil-pro-ergonomic-grip-sleeve-tpu)
- Reviews describe USB-C Pencil as “completely rounded except for one side” like Gen2. — [XDA Developers USB-C review](https://www.xda-developers.com/apple-pencil-usb-c-review/)

### Inferences
- Gen2, Pro, and USB-C share the same public diameter (8.9 mm) and the same conceptual flat-face magnet attach paradigm; Pro/Gen2 also charge on the rail, USB-C attaches only.
- For anti-rotation sleeves/holders, a flat feature matching the Pencil’s flat is required; **measure** flat chord width on the target Pencil before locking CAD—do not treat 7.5 mm as Apple-authoritative.

### Gaps
- Flat face width (chord), flat length along barrel, magnet count/spacing/polarity on the Pencil, and charge-coil keepout on the Pencil: **not published**.
- No iFixit/FCC exhibit with dimensioned flat-face callouts located in this research.
- Whether Pro and Gen2 flats are dimensionally identical is unconfirmed by Apple (same length/diameter suggests high likelihood but not proven).

---

## Cap / USB-C sliding cover travel for USB-C Pencil

### Takeaway
Apple documents a permanently attached sliding cap that reveals a USB-C port for pair/charge; reviews confirm magnetic detents open/closed. **No public travel distance in mm** was found.

### Cited Findings
- Apple Newsroom: “A sliding cap reveals a USB-C port, enabling customers to use a USB-C cable to connect to the new Apple Pencil for pairing and charging.” When magnetically attached for storage, it enters a sleep state. — [Apple Newsroom 2023-10-17](https://www.apple.com/newsroom/2023/10/apple-introduces-new-apple-pencil-bringing-more-value-and-choice-to-the-lineup/)
- Tech specs: Connections include USB-C Connector; length 155 mm overall (closed state implied). — [Apple Pencil (USB-C) – Tech Specs](https://support.apple.com/en-us/121318)
- AppleInsider review: pull cap; slides smoothly; magnetically snaps open; resistance then snap when closing; USB-C at the “eraser” end. No travel mm. — [AppleInsider USB-C review](https://appleinsider.com/articles/23/11/07/apple-pencil-usb-c-review-a-new-budget-option-in-a-temporarily-confusing-lineup)
- XDA: cap does not detach; slides up/down with click; subtle seam line vs Gen2. — [XDA Developers USB-C review](https://www.xda-developers.com/apple-pencil-usb-c-review/)
- MacRumors hands-on: pull bottom to reveal USB-C; cable not included. — [MacRumors hands-on](https://www.macrumors.com/2023/11/06/usb-c-apple-pencil-hands-on/)
- Gen1 uses a **magnetically attached removable cap** over Lightning (different mechanism; cap-loss risk). — [Apple Pencil (1st generation) – Tech Specs](https://support.apple.com/en-us/111920); [iFixit teardown](https://www.ifixit.com/Teardown/Apple+Pencil+Teardown/52955)

### Inferences
- Docks/holders for USB-C Pencil that leave charging possible in-cradle need free axial slide clearance at the rear for the cap + USB-C cable bend radius; without measured travel, leave generous rear clearance or design for tip-forward / rear-open access and measure on hardware.
- Overall length 155 mm is for closed state; open length = 155 mm + travel (unknown).

### Gaps
- Sliding travel (mm), open overall length, seam position from tip/rear, magnet detent force: **not published** and not found as labeled community caliper data.
- FCC BCGA3085 external photos may show open/closed states visually but were not dimension-extracted in this pass.

---

## Recommended holder clearances from Apple or best measured community data

### Takeaway
Apple publishes no Pencil holder clearance guidance. Best public practice for 3D-printed holders: start from official **8.9 mm** diameter / model length, add print-process clearance (~0.2–0.3 mm radial common in community), and optionally model the flat. Device-side magnet keep-outs matter for iPad case/stand products that must not block side-mount attach.

### Cited Findings
- Official diameters are uniformly **8.9 mm** for Pro, USB-C, Gen2, and Gen1; lengths 166 / 155 / 166 / 175.7 mm respectively (see tech-spec links above).
- Printables desk stand: circular guide **9.2 mm** for Gen2 after author found 9.5 mm “a little loose”; author notes scaling for “9-ish mm” pens. — [Printables – Apple Pencil Desk Stand by 2mc](https://www.printables.com/model/108011-apple-pencil-desk-stand)
- MakerWorld ApplePenHolder: marketed for styluses with **9 mm** diameter. — [MakerWorld ApplePenHolder](https://makerworld.com/en/models/2015618-applepenholder)
- SpeakCAD grip sleeve: 9.0 mm bore + 0.1 mm clearance parameter; optional +0.2 mm for PETG; 7.5 mm flat (unverified). — [SpeakCAD grip sleeve](https://speakcad.com/library/apple-pencil-pro-ergonomic-grip-sleeve-tpu)
- Thingiverse Gen1 case: recommends printing a tolerance test; “RECOMMENDED TOLERANCE without calibration is 0.2 mm.” — [Thingiverse plastorub case](https://www.thingiverse.com/thing:4766666)
- Apple Support: cases/covers can prevent magnetic pairing—remove them to troubleshoot—implies case designers must leave magnetic connector accessible / not heavily shielded. — [If you can't pair Apple Pencil…](https://support.apple.com/en-us/HT205236)
- iPad dimensional drawings supply magnet/flux keep-outs for accessories around the long-edge Pencil rail (device-side). — [iPad Pro 13-inch (M5) drawing](https://developer.apple.com/download/files/accessories/dimensional-drawings/ipad-pro-13-inch-m5.pdf)

### Inferences
- Practical starter clearance for rigid PLA/PETG cylindrical pockets: **~9.1–9.3 mm** ID (≈0.2–0.4 mm over 8.9 mm), then fit-test; TPU grips can use nearer 9.0–9.1 mm.
- Length pockets: use model length + tip-protection margin; Gen1 needs ~176 mm tip-to-cap envelope; USB-C needs rear slider/cable access if charging in holder.
- For Duo/iPad stands with Pencil storage **and** side-rail charging, consult the target iPad’s dimensional drawing magnet keep-outs; do not put ferrous mass or thick covers in the hatched flux keep-out without checking the PDF for that SKU.

### Gaps
- No Apple-recommended holder clearance, magnet strength for third-party Pencil docks, or Pencil-to-Pencil magnet clone guidance in public docs.
- No peer-reviewed or systematically calipered community dataset (flat width, tip OD, slider travel) located; existing numbers are isolated maker assumptions—**measure before production**.
- MFi / NDA accessory specs that might define certified Pencil magnets or docks: **inaccessible** without program membership.

---

## Quick reference – official overall envelopes (public)

| Model | Still sold (2026-10) | Length | Diameter | Weight | Magnet behavior |
| --- | --- | --- | --- | --- | --- |
| Pencil Pro | Yes | 166 mm | 8.9 mm | 19.15 g | Attach + pair + charge |
| Pencil (USB-C) | Yes | 155 mm | 8.9 mm | 20.5 g | Attach (storage/sleep); charge via USB-C |
| Pencil (2nd gen) | Yes | 166 mm | 8.9 mm | 18.2 g | Attach + pair + charge |
| Pencil (1st gen) | Yes | 175.7 mm tip-to-cap | 8.9 mm | 20.7 g | Removable magnetic **cap**; Lightning (adapter for USB-C iPads) |

Sources: [Pro](https://support.apple.com/en-us/120123), [USB-C](https://support.apple.com/en-us/121318), [Gen2](https://support.apple.com/en-us/111889), [Gen1](https://support.apple.com/en-us/111920), [overview](https://www.apple.com/apple-pencil/).

---

## Sources checklist (primary first)

| Source | Role |
| --- | --- |
| [Accessory Design Guidelines PDF R31](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) | Overlay/Pencil coexistence only |
| [Dimensional Drawings index](https://developer.apple.com/accessories/dimensional-drawings/) | Confirms no Pencil PDFs; hosts iPad magnet keep-outs |
| [iPad Pro 13" M5 drawing](https://developer.apple.com/download/files/accessories/dimensional-drawings/ipad-pro-13-inch-m5.pdf) | Device-side magnet/flux keep-outs |
| Apple Support Pencil tech specs (links above) | Length/diameter/weight |
| [Apple Pencil Tips 4-pack](https://www.apple.com/shop/product/mx763am/a/apple-pencil-tips-4-pack) | Tip kit compatibility |
| [Newsroom USB-C intro](https://www.apple.com/newsroom/2023/10/apple-introduces-new-apple-pencil-bringing-more-value-and-choice-to-the-lineup/) | Flat side + sliding cap language |
| FCC BCGA2538 / BCGA3085 | Photos/RF; not dimensional CAD |
| iFixit / Printables / SpeakCAD / reviews | Qualitative / community clearance only—label measured where authors state fit results |

**Not accessed (gated):** Apple MFi Program materials; Accessory Interface Specification; any NDA dimensional packs for Pencil.
