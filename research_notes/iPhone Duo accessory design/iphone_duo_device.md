# iPhone Duo device technical specifications (accessory design)

Research as of late October 2026. Apple announced iPhone Duo 2026-09-09; expected retail around late October 2026. Prefer Apple-confirmed figures below; label aggregator/measured/third-party claims separately.

## What are official or best-sourced folded and unfolded external dimensions (mm), thickness, weight?

### Takeaway
Apple publishes official Size and Weight for open and closed states: unfolded **117.8 × 164.6 × 5.2 mm**, folded **117.8 × 84.1 × 11.3 mm**, weight **254 g** either way. Camera-bump-inclusive thickness is not on Apple’s specs page; PhoneArena lists ~10.4 mm with bump when open (unverified method).

### Cited Findings
- **Open (Apple official):** Height 4.64 in (117.8 mm); Width 6.48 in (164.6 mm); Depth 0.21 in (5.2 mm); Weight 8.96 oz (254 g) — [Apple iPhone Duo Technical Specifications](https://www.apple.com/iphone-duo/specs/)
- **Closed (Apple official):** Height 4.64 in (117.8 mm); Width 3.31 in (84.1 mm); Depth 0.44 in (11.3 mm); Weight 8.96 oz (254 g) — [Apple iPhone Duo Technical Specifications](https://www.apple.com/iphone-duo/specs/)
- Same open/closed mm figures and 254 g repeated in secondary roundups — [MacRumors iPhone Duo roundup](https://www.macrumors.com/roundup/iphone-duo/); [The Verge](https://www.theverge.com/tech/991203/iphone-duo-foldable-news-specs-price-release-date)
- **PhoneArena (aggregator; camera bump add-on):** Unfolded 117.8 × 164.6 × 5.2 mm (~10.40 mm with camera bump / ~0.41 in); Folded 117.8 × 84.1 × 11.3 mm; Weight 254.0 g — [PhoneArena Apple iPhone Duo](https://www.phonearena.com/phones/Apple-iPhone-Duo_id12657)
- Comparison commentary (not Apple): folded thickness 11.3 mm / 254 g called thicker/heavier than typical Android book foldables — [9to5Google](https://9to5google.com/2026/09/09/iphone-duo-thicker-and-heavier-than-basically-every-android-foldable/)
- **Inner display (Apple):** marketed 7.6-inch diagonal OLED; rectangular measure 7.58 in; resolution 1878 × 2670 at 430 ppi; nano-texture finish — [Apple specs](https://www.apple.com/iphone-duo/specs/); display footnote also on [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- **Outer display (Apple):** marketed 5.4-inch; rectangular measure 5.36 in; resolution 1398 × 2034 at 460 ppi — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Both displays: ProMotion up to 120 Hz; Always-On; typical 1000 nits / HDR 1600 / outdoor peak 3000 / min 1 nit — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- **Materials (Apple):** Grade 5 titanium enclosure (mirror-polished); Ceramic Shield 2 front (outer); Ceramic Shield back; 3D-printed titanium hinge cover (micro-blasted); IP68 (6 m / 30 min IEC 60529) — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/); [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Recycled-content notes useful for finish assumptions: 85% recycled titanium enclosure; 100% recycled titanium 3D-printed hinge cover; 100% recycled aluminum internal structural frame — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Colors: Night Sky, Star White — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Model A3447 listed on US cellular/spec pages; regional variants A3719 / A3720 / A3721 — [Apple specs](https://www.apple.com/iphone-duo/specs/); [TechWalls model differences](https://www.techwalls.com/iphone-duo-model-number-a3447-a3719-a3720-a3721-differences/)
- PhoneArena inner resolution **2460×2180** conflicts with Apple’s **1878×2670** — treat PhoneArena display pixels as unreliable vs Apple — [PhoneArena](https://www.phonearena.com/phones/Apple-iPhone-Duo_id12657); contradicted by [Apple specs](https://www.apple.com/iphone-duo/specs/)

### Inferences
- Closed envelope is short/wide “passport” style: 117.8 mm tall × 84.1 mm wide × 11.3 mm thick—shorter than conventional modern iPhones, so tall MagSafe wallets/packs overhang.
- Unfolded envelope is landscape-dominant: 164.6 mm wide × 117.8 mm tall × 5.2 mm body—Apple markets this as thinnest iPhone body when open.
- For 3D-printed cradles, design two discrete envelopes (open vs closed) plus a hinge free zone; do not assume a single rectangular slab.
- PhoneArena’s ~10.4 mm open-with-bump figure is the best public bump-inclusive thickness found, but method is not documented—use only as a provisional keepout until caliper measurement or Apple ARD exists.

### Gaps
- No Apple-published camera plateau height, footprint, or X/Y offsets from edges.
- No official corner radii, glass-to-housing margins, or flat-vs-curve profiles for case walls.
- No independent lab caliper dataset cited here beyond PhoneArena’s bump note.
- Battery capacity mAh not on Apple specs (PhoneArena lists 4883 mAh—unofficial).

## Where are MagSafe/Qi2 magnets and charging faces relative to the chassis?

### Takeaway
Apple confirms MagSafe and Qi2 wireless charging up to **25W**, with magnet array, alignment magnet, Accessory Identification NFC, and magnetometer—but does **not** publish magnet ring center coordinates. Engineering consensus and hands-on reporting place the MagSafe/Qi2 charging face on the **rear (camera) half only**; upright MagSafe stands can tip when the phone is unfolded.

### Cited Findings
- Apple MagSafe / Qi2: wireless charging up to 25W each; components listed: Magnet array, Alignment magnet, Accessory Identification NFC, Magnetometer — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Wired USB-C fast charge: up to 50% in ~20 min with 60W+ adapter; wireless MagSafe: up to 50% in ~30 min with 35W+ adapter + MagSafe Charger — [Apple specs](https://www.apple.com/iphone-duo/specs/); [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- Product FAQ: supports MagSafe and Qi2 25W or Qi-certified chargers — [apple.com/iphone-duo](https://www.apple.com/iphone-duo/)
- Official cases (Duo Case two-part; Duo Folio with kickstand) stated MagSafe / Qi2 25W / Qi-compatible with magnets aligning to Duo — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- Engadget (accessory fit): inbound wireless charging magnetic coils “built into the rear panel of the device, underneath the camera”; existing MagSafe/Qi2 chargers generally work; MagSafe wallets/batteries sized for taller phones may overhang — [Engadget](https://www.engadget.com/2281471/iphone-duo-which-accessories-fit/)
- MacRumors (hands-on/demo reporting, 2026-10-21): MagSafe ring “only on one half”; unfolded upright MagSafe stands can tip from uneven weight; safest upright MagSafe use is **closed**; flat chargers avoid tip-over; landscape/horizontal MagSafe may work (Nilay Patel demo cited) — [MacRumors MagSafe tip-over](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/)
- FoldifyCase / accessory blogs: magnet array on back of one half; closed MagSafe wallets can overhang 117.8 mm height; open use is lopsided for magnetic stands—prefer kickstand/Folio for open viewing — [FoldifyCase MagSafe guide](https://www.foldifycase.com/blogs/news/iphone-duo-magsafe-what-fits-2026)
- Geometry argument (third-party, not Apple): MagSafe must be on camera-half back because the other outer face is the 5.4″ cover display; magnets centered when folded, off-center when open — [DuoCaseCo](https://duocaseco.com/blogs/news/does-the-iphone-duo-support-magsafe-yes-with-two-catches)
- Hinge closure uses an “integrated magnet array” for secure closed feel (separate from MagSafe wording in Newsroom) — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)

### Inferences
- For docks/stands: treat MagSafe attach as **closed-preferred**; if supporting open MagSafe, provide a ledge/shelf under the non-magnet half or dual-support cradle—do not hang the full 254 g from one half on a vertical puck alone.
- MagSafe coil/magnet keep-in is on the Ceramic Shield back half, near/under the camera plateau; case rear thickness and metal permeability rules from general MagSafe ARD still apply once Duo drawings appear.
- Hinge closure magnets ≠ MagSafe charging ring; do not assume MagSafe magnets span both halves.

### Gaps
- No Apple mm coordinates for MagSafe ring center, diameter, or NFC/magnetometer offsets on Duo.
- No public confirmation of MagSafe ring strength vs prior iPhones.
- Whether Qi2/MagSafe works reliably while fully open flat on a pad is demonstrated informally but not specified by Apple.
- Exact clearance between MagSafe attach zone and camera plateau glass (critical for wallet/battery design) unpublished.

## What ports, buttons, cameras, speakers, and hinge zones must accessories keep clear?

### Takeaway
Apple’s public specs diagram and Newsroom describe layout: top volume, right-side Touch ID side button + Camera Control, bottom USB-C, stereo speakers/mics, rear dual 48MP on a camera plateau, outer 12MP Center Stage, inner under-display FaceTime. No Action button / no SIM tray. Exact keepout cones and button cutout dimensions are **not** in public Duo ARDs yet—use qualitative keepouts plus general MagSafe/Camera Control guidance from other iPhone drawings until Duo PDFs ship.

### Cited Findings
- **External controls (Apple specs labels):** Volume up/down; Camera Control; Side button (Touch ID in side button); USB-C connector; built-in stereo speakers and microphones (diagram on specs page) — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Touch ID in side button for open or closed use; Camera Control present; no Action button / no mute switch (MacRumors synthesis of shipping design) — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/); [MacRumors roundup](https://www.macrumors.com/roundup/iphone-duo/)
- Volume buttons on **top**; USB-C on **bottom**; stereo speakers top and bottom; right side: Touch ID side button + Camera Control — [MacRumors roundup](https://www.macrumors.com/roundup/iphone-duo/)
- eSIM only worldwide; no physical SIM tray — [Apple specs](https://www.apple.com/iphone-duo/specs/); [Newsroom / MacRumors announce](https://www.macrumors.com/2026/09/09/apple-announces-foldable-iphone-duo/)
- **Rear cameras:** 48MP Fusion Main (26 mm, ƒ/1.6, sensor-shift OIS) + 48MP Fusion Ultra Wide (13 mm, ƒ/2.2, 120°); sapphire lens cover; True Tone flash; Dual Fusion system on camera plateau — [Apple specs](https://www.apple.com/iphone-duo/specs/); [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- **Outer front:** 12MP Center Stage, ƒ/2.2 — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- **Inner:** under-display FaceTime camera; Edge Light for video calls (footnote-tied) — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Hinge: >100 precision components; supports display center when open; carbon fiber support plates; magnetic secure closure; 3D-printed hinge cover — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- Software/use poses for accessory implication: half-folded / tent / StandBy even without charger; content avoids crease; speakers retune with pose — [MacRumors announce](https://www.macrumors.com/2026/09/09/apple-announces-foldable-iphone-duo/); [MacRumors roundup](https://www.macrumors.com/roundup/iphone-duo/)
- Engadget: mechanical car mounts may fail on new dimensions; screen protectors/cases need Duo-specific; USB-C peripherals and most wireless chargers still work — [Engadget](https://www.engadget.com/2281471/iphone-duo-which-accessories-fit/)
- Apple Pencil (USB-C) support listed for both displays (timing footnote on specs) — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- Dual batteries (one per half), managed as one — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/); [Apple specs](https://www.apple.com/iphone-duo/specs/)

### Inferences
- Case strategy: two-shell wrap (Apple’s own Duo Case pattern) or Folio; leave hinge seam free to flex; avoid clamping force on hinge cover.
- Keep clear: camera plateau + flash, outer punch/Center Stage camera, USB-C mating zone, top volume keys, right Camera Control + side button, speaker/mic ports top/bottom, full hinge spine, MagSafe rear face.
- Stands that prop tent/half-fold should provide soft contact pads on outer glass / rear only—no hard pressure on crease/hinge axis.
- Camera Control keepout geometry from other recent iPhone ARDs (e.g. iPhone 17 Pro drawings) is a temporary proxy only—verify against Duo when published.

### Gaps
- No official button X/Y dimensions, port keepout depth (e.g. 14 mm outward mating), speaker grill maps, or camera FOV cones for Duo.
- Which physical half holds USB-C relative to camera half when closed is not stated in text (diagram exists on Apple specs but was not dimensioned in scrape).
- Antenna keepout bands (ceramic fiber inserts mentioned by MacRumors) lack mm maps.
- Inner under-display camera location (center vs offset) not dimensioned.

## Are there Apple tech specs pages, ARD/PDF drawings, or only marketing pages?

### Takeaway
Apple ships a full **Technical Specifications** page plus Newsroom product pages—strong official source for overall size/weight/display/charging. Public **Accessory Design Guidelines dimensional-drawings** list (as of this research) includes iPhone 18 Pro / 17 / Air etc. but **does not list iPhone Duo**. Engadget claims manufacturers receive dimensional drawings; those appear partner/MFi-gated, not on the public download index. FCC filings exist under BCG-E9188A (A3447 parent) for RF/compliance; no public mechanical ARD extracted here.

### Cited Findings
- Official tech specs: [https://www.apple.com/iphone-duo/specs/](https://www.apple.com/iphone-duo/specs/)
- Marketing / overview: [https://www.apple.com/iphone-duo/](https://www.apple.com/iphone-duo/)
- Newsroom announce: [https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- Product Environmental Report PDF linked from specs: [iPhone_Duo_PER_Sept2026.pdf](https://www.apple.com/environment/pdf/products/iphone/iPhone_Duo_PER_Sept2026.pdf)
- Public dimensional drawings index (no iPhone Duo entry observed among listed New/current iPhones): [developer.apple.com/accessories/dimensional-drawings](https://developer.apple.com/accessories/dimensional-drawings/)
- Accessory Design Guidelines PDF exists and points to dimensional drawings for keep-outs (antennas, connectors, cameras, inductive charging, MagSafe sections)—general MagSafe rules apply across MagSafe phones, but Duo-specific sheets not found in public index — [Accessory-Design-Guidelines.pdf](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)
- Engadget: “Apple provides manufacturers with a trove of dimensional drawings” explaining case incompatibility — [Engadget](https://www.engadget.com/2281471/iphone-duo-which-accessories-fit/)
- Developer “Get ready for iPhone Duo” is **app layout / SDK**, not mechanical ARD — [developer.apple.com/iphone-duo](https://developer.apple.com/iphone-duo/)
- FCC: parent model A3447, FCC ID **BCG-E9188A**; variants A3719/A3720/A3721 → BCG-E9198A / E9203A / E9204A; described as foldable smartphone with WPT; test report dated 2026-07-23 — [FCC test report summary via fccid.ai](https://fccid.ai/m/1396489ceb5b1892cdef9af94da442acb8356f9e2d6d4dba4079ecbade61f5b3.pdf); e-label models A3447–A3721 — [FCC e-label PDF](https://fccid.ai/m/e3f4518ac87afcd6cf02f643f4301eb7bea2c83d3d13bcc23e1da1c7e14ed2c4.pdf)
- Patent literature (illustrative hinge/display concepts, **not** measured Duo CAD) e.g. US20260122799A1 — [Supracite analysis](https://read.supracite.com/articles/iphone-duo/)

### Inferences
- For immediate 3D-print accessory work: use Apple Size and Weight + qualitative MagSafe/camera/hinge keepouts; do not wait for public Duo ARD if prototyping closed MagSafe docks with soft tolerances.
- Request/check Apple Developer dimensional-drawings periodically—Duo PDF may appear after retail launch like other iPhones.
- FCC exhibits may include external photos useful for visual keepouts; expect mechanical drawings to stay confidential if present.

### Gaps
- No publicly downloadable `iphone-duo.pdf` ARD found on Apple’s dimensional-drawings page during this research (late Oct 2026).
- No FCC mechanical CAD/dimensional exhibit reviewed in detail here (RF/WPT reports identified; external photo packs not fully scraped).
- MagSafe Charger ARD exists for the charger puck, not for Duo phone magnet layout — [Apple MagSafe Charger drawing](https://developer.apple.com/download/files/accessories/dimensional-drawings/apple-magsafe-charger.pdf)

## What is still UNKNOWN / rumor vs Apple-confirmed?

### Takeaway
Post-announce (Sep 2026), core chassis dimensions, displays, materials, MagSafe/Qi2 25W support, button concept, and dual-battery architecture are **Apple-confirmed**. Still unknown for accessory CAD: MagSafe mm layout, camera plateau geometry, port/button keepout drawings, hinge free-volume, and public ARD. Pre-launch rumor numbers (e.g. 9–9.5 mm folded, 5.5″/7.8″ screens) are **obsolete** vs shipping Apple specs.

### Cited Findings — Apple-confirmed (post 2026-09-09)
- Product name iPhone Duo; first foldable iPhone; starts $1,999 / 256GB — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)
- Dimensions/weight/displays/charging/IP68/titanium/Ceramic Shield/A20 Pro/C2 modem/N1/eSIM/Touch ID side button/Camera Control/USB-C as on specs — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- MagSafe + Qi2 up to 25W; official MagSafe-compatible Duo Case and Folio — [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/)

### Cited Findings — Measured / observed (third-party; not Apple datasheet)
- MagSafe on one half; upright MagSafe tip-over when open — [MacRumors](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/)
- MagSafe coils under camera / rear panel — [Engadget](https://www.engadget.com/2281471/iphone-duo-which-accessories-fit/)
- ~10.4 mm open thickness including camera bump — [PhoneArena](https://www.phonearena.com/phones/Apple-iPhone-Duo_id12657)
- Wallet/battery overhang on short 117.8 mm back — [FoldifyCase](https://www.foldifycase.com/blogs/news/iphone-duo-magsafe-what-fits-2026); [Smartish](https://smartish.com/blogs/news/iphone-duo-magsafe-accessories-what-fits-what-doesnt-and-what-to-buy)

### Cited Findings — Obsolete rumor (pre-announce; do not use for design)
- Pre-launch thickness rumors ~9–9.5 mm folded / ~4.5–4.8 mm open; screen rumors 5.5″/7.8″ or 5.3″/7.7″ — [MacRumors pre-launch expectations](https://www.macrumors.com/2026/09/09/iphone-fold-launch-pricing-what-to-expect/) — **superseded** by Apple 11.3 / 5.2 mm and 5.4″ / 7.6″

### Cited Findings — Still unknown / unverified for CAD
- Exact MagSafe ring center offsets (mm), ring OD, NFC antenna location
- Camera plateau plan dimensions and bump height (Apple official)
- Public Duo dimensional drawings / Camera Control keepout cones
- Hinge outer radius, gap when open/closed, case clearance over hinge cover
- Which closed-face half is “bottom” for USB-C relative to camera in absolute coordinates
- Whether Apple MagSafe Wallet is officially Duo-compatible (third parties note omission from Apple wallet lists — [Smartish](https://smartish.com/blogs/news/iphone-duo-magsafe-accessories-what-fits-what-doesnt-and-what-to-buy))
- foldifycase / caliper STLs specifically for Duo chassis (searched MagSafe fit articles; no authoritative mm magnet map found)

### Inferences
- Label confidence for accessory modeling: **High** for outer envelope (Apple mm); **Medium** for MagSafe on camera half / closed charging preference (consistent third-party + geometry); **Low** for magnet/camera keepout coordinates until ARD or calipers.
- Safe first-print closed MagSafe dock: support 84.1 × 117.8 × 11.3 mm block, MagSafe puck interface on rear half, clearance for camera plateau height ≥~5 mm extra beyond 5.2 mm body (provisional), soft lips avoiding hinge spine.

### Gaps
- No foldifycase published full chassis DXF/STL with magnet centers found in this pass.
- No teardown caliper table (iFixit-style) cited for late-Oct 2026.
- FCC external photos not fully mined for dimension scales.
- Apple Pencil USB-C timing and magnetic attach (if any) for Duo unresolved for stylus cradles.

---

## Quick reference table (Apple official unless noted)

| State | Height | Width | Depth | Weight |
|-------|--------|-------|-------|--------|
| Open | 117.8 mm | 164.6 mm | 5.2 mm | 254 g |
| Closed | 117.8 mm | 84.1 mm | 11.3 mm | 254 g |
| Open + camera bump | — | — | ~10.4 mm (PhoneArena; not Apple) | 254 g |

| Display | Marketed diagonal | Rectangular measure | Resolution | ppi |
|---------|-------------------|---------------------|------------|-----|
| Inner | 7.6 in | 7.58 in | 1878 × 2670 | 430 |
| Outer | 5.4 in | 5.36 in | 1398 × 2034 | 460 |

| Wireless power | Max | Notes |
|----------------|-----|-------|
| MagSafe | 25 W | Magnet array + alignment magnet + Accy ID NFC + magnetometer |
| Qi2 | 25 W | Same face family as MagSafe; coils reported under rear camera half |

**Primary sources:** [Apple specs](https://www.apple.com/iphone-duo/specs/), [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/), [dimensional-drawings index](https://developer.apple.com/accessories/dimensional-drawings/), [MacRumors MagSafe](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/), [Engadget accessories](https://www.engadget.com/2281471/iphone-duo-which-accessories-fit/), FCC BCG-E9188A / A3447.
