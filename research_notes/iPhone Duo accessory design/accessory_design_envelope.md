# iPhone Duo accessory design envelope (stands, docks, plates, mounts)

**Research date:** 2026-10-22 (late October 2026; retail phone launches 2026-10-23)  
**Scope:** Practical CAD envelopes for bare Duo and Apple’s two official cases (iPhone Duo Case; iPhone Duo Folio with Kickstand).  
**Naming trap:** Do not confuse Apple **iPhone Duo** (book-style foldable phone) with Apple **MagSafe Duo** (legacy dual MagSafe desk charger for phone + Watch). Many Printables/MakerWorld hits titled “MagSafe Duo” are for the charger, not the phone.

**Confidence legend used below:**  
- **Apple-official** — published on apple.com product/spec pages  
- **Measured** — caliper/scale/observation on physical hardware (often case-only before phone delivery)  
- **Derived / third-party estimate** — case-vendor or retailer arithmetic from published phone dims  
- **Anecdotal / low** — video hands-on, single reviewer, or uncorroborated community claims  

**Technical drawings / STEP / caliper datasets found:** No Apple STEP/IGES or Accessory Design Guidelines dimensional package for iPhone Duo itself was located. Apple Developer offers MagSafe Charger dimensional drawings (charger, not phone). Best available envelopes are Apple published H×W×D plus early Folio-only physical reviews and visualization mockups that explicitly disclaim precision accessory use.

---

## Folded vs unfolded accessory use cases (pocket stand vs book-mode vs landscape kickstand)

### Takeaway
Design accessories as **three distinct poses**: closed outer-display use (pocket / StandBy), book-open inner display (desk / media), and landscape propped (Folio kickstand or phone self-stand). MagSafe docks that only work in one pose will fail common unfolded desk use.

### Cited Findings
- Apple describes posable use: outer display when closed; large inner display when open; angle for movies; stand for hands-free video/calls — [Apple iPhone Duo product page](https://www.apple.com/iphone-duo/)
- Official size/weight (Apple-official): closed **117.8 × 84.1 × 11.3 mm**, open **117.8 × 164.6 × 5.2 mm**, **254 g** — [Apple iPhone Duo Technical Specifications](https://www.apple.com/iphone-duo/specs/)
- FoldifyCase restates the same Apple dims and notes height is constant because the device opens book-style along the long edge (width nearly doubles; thickness roughly halves) — [FoldifyCase: iPhone Duo Dimensions & Specs](https://www.foldifycase.com/blogs/news/iphone-duo-confirmed-specs-case-fit-2026)
- Apple Folio with Kickstand: integrated kickstand for “a range of angles” for reading, viewing, or FaceTime; kickstand snaps back when unused — [Apple Folio product page](https://www.apple.com/shop/product/mkr64zm/a/iphone-duo-folio-with-kickstand-taupe)
- Folio (case-only Measured): kickstand opens to **about 90°**; Apple markets landscape propped viewing; portrait orientation of Folio alone looked nearly upright and less stable before phone install — [iPhone Mania Folio review (JP)](https://iphone-mania.jp/iphone18-607603/)
- MacRumors (2026-10-21): upright MagSafe stands can tip when Duo is **unfolded** due to asymmetric mass; safest upright MagSafe use is **closed**; flat chargers avoid the rotation issue; wider stands with a ledge recommended for open use — [MacRumors: Duo tips over on MagSafe stands when unfolded](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/)
- MakerWorld “iPhone Duo MagSafe Desk Charging Stand” claims support for Duo **folded or open** in either orientation (designer claim; not independent metrology) — [MakerWorld model 3395379](https://makerworld.com/en/models/3395379-iphone-duo-magsafe-desk-charging-stand)

### Inferences
- **Pocket / closed accessories** should envelope ≈84.1 × 117.8 mm footprint and ≥11.3 mm stack (plus case), with MagSafe on the camera half only.
- **Book-mode docks** need either a mechanical ledge or a much wider base; magnetic-only upright mounts sized for slab iPhones are insufficient when open.
- **Landscape kickstand** is Folio’s primary differentiator; third-party stands should treat Folio-with-kickstand-open as a separate envelope (stand leaf + MagSafe cavity behind the leaf).

### Gaps
- No published Apple angle table for Folio kickstand detent positions (only “range of angles”).
- No retail-phone caliper confirmation of closed/open envelopes until after 2026-10-23 (FoldifyCase states they will caliper a retail unit then).
- Phone self-stand / tent / Flex-mode MagSafe contact while partially open remains unconfirmed by Apple.

---

## Official case added thickness/width and kickstand protrusion (Duo Case vs Folio with Kickstand)

### Takeaway
Apple publishes **no on-device thickness add** for either official case. Best CAD practice: model **bare phone** from Apple specs, treat **Duo Case** as thin two-piece PC shells with adhesive (hinge exposed, sides covered), and treat **Folio** as magnetically attached TechWoven plates (~58 g Measured) that cover the outer display when closed, leave sides exposed, and add a kickstand leaf that reaches ~90° with MagSafe recess behind it.

### Cited Findings

#### Bare phone (Apple-official baseline)
- Closed: 117.8 × 84.1 × 11.3 mm; open: 117.8 × 164.6 × 5.2 mm; 254 g — [Apple specs](https://www.apple.com/iphone-duo/specs/)

#### iPhone Duo Case ($79, polycarbonate two-piece)
- Apple: two-part, thin/light, wraps both sides front-to-back; MagSafe/Qi2/Qi charging through case; polycarbonate with matte coating; colors Navy Blue / Sand — [Apple Duo Case](https://www.apple.com/shop/product/mkr84zm/a/iphone-duo-case-navy-blue)
- MacRumors: adhesive strips along inside edges; protects camera-side back and outer-display frame; **no inner-display protection when unfolded**; hinge left unobstructed so device can close flat — [MacRumors adhesive article](https://www.macrumors.com/2026/10/16/iphone-duo-case-adhesive/); [Macworld cases roundup](https://www.macworld.com/article/3239288/best-iphone-duo-cases-slim-protective-and-kickstand-options.html)
- Hands-on video: MagSafe ring visible under magnetic paper **only on camera half**; upper (cover-display) half has no magnets; large shared cutout for side button + Camera Control; adhesive needed because halves are very thin when phone is open — [YouTube first-look transcript via search](https://www.youtube.com/watch?v=-2qEsrthOuo)
- **Thickness add:** Apple unpublished. FoldifyCase engineering estimate: ~1 mm wall per half → about **+2 mm closed** → ~**13.3 mm** pocket stack for a slim two-face case (Derived; not measured on Apple’s case) — [FoldifyCase](https://www.foldifycase.com/blogs/news/iphone-duo-confirmed-specs-case-fit-2026)
- **Weight add:** Apple unpublished for Duo Case; video reviewers claim “incredibly light” but no corroborated gram figure found in text sources for this note set.

#### iPhone Duo Folio with Kickstand ($129, TechWoven)
- Apple: TechWoven; thin/light; kickstand snaps closed; MagSafe/Qi2/Qi charging **on the outside or behind the open kickstand** — [Apple Folio](https://www.apple.com/shop/product/mkr64zm/a/iphone-duo-folio-with-kickstand-taupe)
- MacRumors / PhoneArena: Folio attaches **magnetically** (no adhesive); covers front display when closed; magnets allow folding cover back to use outer display; **does not protect sides** — [MacRumors](https://www.macrumors.com/2026/10/16/iphone-duo-case-adhesive/); [PhoneArena](https://www.phonearena.com/news/Apples-new-79-iPhone-Duo-case-requires-actual-glue-to-stay-on-your-phone_id184121)
- Mac Otakara: Folio magnets mate to magnets in Duo rear **and** outer-display side; cover open wakes outer display — [Mac Otakara](https://www.macotakara.jp/iphone/entry-51788.html)
- iPhone Mania (Measured, Folio alone, 2026-10-18):
  - Weight **58 g** → phone+Folio ≈ **312 g** (~+23%)
  - Two plates joined by flexible sheet that deploys as a book-spine cover when opening
  - Soft raised lining inside; MagSafe ring visible; **no linear MagSafe “bar” magnets** as on some slab cases
  - Kickstand ~**90°** max observed; MagSafe-shaped recess on stand underside
  - **No side coverage**; **no** Apple strap lugs
  - Legacy MagSafe power banks / stands **attach magnetically** but **overhang ~15 mm** past Folio edge (Measured on Folio alone)
  — [iPhone Mania Folio review](https://iphone-mania.jp/iphone18-607603/)
- Retailer packaging / listing dims (low confidence as **on-phone** envelope; likely package or product-as-shipped):
  - T-Mobile: Weight **0.353 lb** (~160 g — conflicts with 58 g scale; likely includes packaging), Length **7.24 in**, Height **6.1 in**, Width **0.57 in** (~14.5 mm) — [T-Mobile Folio listing](https://www.t-mobile.com/accessory/apple-folio-with-kickstand-for-iphone-duo?sku=195951382364)
  - Beyond the Box PH: Weight **0.16 kg**, Length **18.40 cm**, Height **15.50 cm**, Width **1.45 cm** — [Beyond the Box](https://beyondthebox.ph/pages/folio-kickstand-for-iphone-duo)
- Rokform: notes a 2 mm shell on each face can add ~**4 mm** to closed stack (~35% on 11.3 mm); OtterBox Lumen Series for Duo listed at **0.46 in / 11.75 mm** case thickness alone (third-party case, not Apple Folio) — [Rokform foldable cases article](https://www.rokform.com/blogs/rokform-blog/foldable-iphone-cases)

### Inferences
| Config | Suggested CAD starting envelope | Confidence |
| --- | --- | --- |
| Bare closed | 84.1 × 117.8 × 11.3 mm + camera bump allowance | Apple-official (bump height unpublished) |
| Bare open | 164.6 × 117.8 × 5.2 mm | Apple-official |
| Duo Case closed | Bare + ~1–2 mm per face (estimate **~13–15 mm** stack); sides framed; hinge gap clear | Derived / unverified |
| Folio closed | Bare + Folio plate stack; outer display covered; sides exposed; magnetic attach | Structure Measured; thickness mm gap |
| Folio kickstand open | Add stand leaf to ~90°; reserve MagSafe cavity **behind** leaf; watch accessory overhang past short edge (~15 mm seen with slab MagSafe banks) | Measured Folio-only |
| Width add | Duo Case may add small rim beyond 84.1 mm; Folio side exposure → width add mainly from plate edges, not full side walls | Qualitative |

### Gaps
- **No published mm thickness** for Duo Case or Folio on/off phone (Apple-official gap).
- **Kickstand closed protrusion** (how far the stowed stand stands proud of the Folio back) not measured in mm in sources found.
- **Kickstand open footprint** (depth of propped phone+Folio on a desk) not published.
- T-Mobile **0.353 lb** vs iPhone Mania **58 g** conflict: treat retailer weight as packaging-contaminated unless re-verified.
- Camera plateau height / MagSafe center offsets from edges: no Apple drawing; mockups approximate from photos only.
- No STEP/CAD of official cases found.

---

## MagSafe alignment folded vs unfolded; dual-face charging quirks

### Takeaway
MagSafe lives on **one half only** (camera / non-cover-display side). Reliable charging/accessory geometry is **closed, ring-down**. Unfolded MagSafe works electrically but upright mounts often fail mechanically due to cantilevered mass. Folio explicitly supports charging **behind the open kickstand**. There is no Apple claim of MagSafe on both outer faces.

### Cited Findings
- Apple specs: MagSafe up to **25W**; Qi2 up to **25W**; magnet array, alignment magnet, Accessory ID NFC, magnetometer; 50% in ~30 min with MagSafe + ≥35W adapter — [Apple specs](https://www.apple.com/iphone-duo/specs/)
- AppleInsider: MagSafe is on the **non-screen side under the camera** (not both halves) — [AppleInsider](https://appleinsider.com/articles/26/09/09/contrary-to-early-rumors-iphone-duo-does-have-magsafe-charging)
- MacRumors: ring on one half; unfolded upright MagSafe can tip; anti-rotation magnet exists but some chargers ignore it; horizontal MagSafe charging reportedly OK (The Verge demo cited); recommend closed for upright stands — [MacRumors](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/)
- Apple Folio copy: charge with case on via MagSafe/Qi2/Qi **on the outside or behind the open kickstand** — [Apple Folio](https://www.apple.com/shop/product/mkr64zm/a/iphone-duo-folio-with-kickstand-taupe)
- iPhone Mania: MagSafe puck snaps to Folio; MagSafe-shaped recess under kickstand; charging speed with phone not yet verified (case arrived before phone) — [iPhone Mania](https://iphone-mania.jp/iphone18-607603/)
- Hands-on Duo Case: MagSafe ring only in camera-half piece; Anker MagGo / ESR CryoBoost docks work; slab MagSafe power banks attach but **stick out** due to Duo’s short/wide footprint — [YouTube first-look](https://www.youtube.com/watch?v=-2qEsrthOuo)
- FoldifyCase MagSafe guidance for cases: “magnet transparency, not magnet addition” — keep phone’s 25W array aligned rather than adding competing magnets (as Samsung cases often do) — [FoldifyCase](https://www.foldifycase.com/blogs/news/iphone-duo-confirmed-specs-case-fit-2026)

#### MagSafe puck OD / thickness for dock bore design (not phone-specific)
- ChargerLAB Measured Apple **25W MagSafe** (A2580): panel diameter ≈ **55.38–55.5 mm**, thickness ≈ **4.45–4.53 mm**, woven cable ~2.35 mm OD — [ChargerLAB 25W review](https://www.chargerlab.com/review-of-apple-25w-magsafe-charger); [ChargerLAB teardown](https://www.chargerlab.com/teardown-of-apple-25w-magsafe-charger-hk-a2580)
- Reddit community (older **15W** A2140 era, lower confidence): OD ≈ **55.9 mm**, thickness ≈ **5.5 mm**, inner metal ≈ **48.4 mm** — [r/MagSafe thread](https://www.reddit.com/r/MagSafe/comments/mbsf40/could_anyone_provide_me_the_dimension/)
- MakerWorld Duo phone stand: 25W braided puck “slightly smaller and thinner” than pre-2024 15W rubber-cord puck — separate print profiles — [MakerWorld 3395379](https://makerworld.com/en/models/3395379-iphone-duo-magsafe-desk-charging-stand)
- Apple Developer: downloadable MagSafe Charger dimensional drawings (prefer over Reddit for production) — [Apple Developer dimensional drawings](https://developer.apple.com/accessories/dimensional-drawings/)

### Inferences
- Dock bore: design for **~55.5 mm OD / ~4.5 mm thick** 25W puck with clearance for woven cable exit; optionally dual-profile for legacy ~56 × 5.5 mm 15W puck.
- MagSafe plate/mount center should be referenced to the **camera half** only; do not assume center-of-open-book symmetry.
- Dual-face charging in the sense of “charge either outer face” is **not** supported by sources; Folio’s “outside or behind kickstand” still targets the same camera-side magnet stack through different case paths.
- For open portrait MagSafe: magnets must hold cantilevered second half (~half of 254 g plus case); many upright pucks will not—add a ledge.

### Gaps
- Exact MagSafe ring center coordinates relative to camera island / USB-C / edges: unpublished.
- Coil-to-coil gap / max case thickness for full 25W on Duo: unpublished.
- Whether Folio + kickstand-open + MagSafe behind stand maintains full 25W under load: untested in Folio-before-phone reviews.
- Dual MagSafe coils (one per half): not present per AppleInsider / hands-on case magnet mapping.

---

## Common third-party case/stand design pitfalls for foldables (hinge crush, display pressure, magnet interference)

### Takeaway
Highest-risk failure modes for Duo accessories: **hinge crush / grit trapping**, **inner Nano-texture contact when closed**, **side-button Touch ID occlusion**, **competing MagSafe magnets**, **asymmetric MagSafe tip-over when open**, and **slab-MagSafe accessory overhang** on the short/wide closed footprint.

### Cited Findings
- FoldifyCase design brief for Duo:
  - Thin walls / weight discipline (254 g base)
  - **Open chamfered power-button cutout** required (Touch ID in side button; covering breaks unlock)
  - **Nothing touching inner panel** when closed (Nano-texture coated; raised bezels, zero contact)
  - Magnet transparency vs adding magnets
  - Hinge still needs case attention despite IP68 (ingress rating ≠ grit-free hinge mechanism)
  - Galaxy Z Fold cases **will not fit** (all three axes differ)
  — [FoldifyCase](https://www.foldifycase.com/blogs/news/iphone-duo-confirmed-specs-case-fit-2026)
- Rokform:
  - Soft hinge bridges can deform and create **pressure at fold line**
  - Material on **both panels doubles** closed thickness impact
  - Moving hinge covers add bulk; open hinge leaves mechanism exposed
  - iFixit Galaxy Z Fold8 hinge grit grinding cited as category lesson
  — [Rokform](https://www.rokform.com/blogs/rokform-blog/foldable-iphone-cases)
- Smartish guide (partly pre-fit / marketing-adjacent; confidence mixed):
  - Two-piece cases must not press hinge or prevent flat close
  - Camera bevel clearance estimate **1.5–2.0 mm** (from leak-era analysis; verify on retail)
  - MagSafe alignment critical on split cases; accessory must not press hinge or cover display
  — [Smartish Duo case guide](https://smartish.com/blogs/news/iphone-duo-case-guide-how-to-protect-apples-foldable-without-the-bulk)
- Macworld: Apple Duo Case leaves hinge “unobstructed/exposed”; adhesive two-piece harder to swap than magnetic Folio — [Macworld](https://www.macworld.com/article/3239288/best-iphone-duo-cases-slim-protective-and-kickstand-options.html)
- MacRumors MagSafe tip-over when unfolded — [MacRumors](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/)
- iPhone Mania: slab MagSafe accessories overhang ~15 mm on Folio short edge — [iPhone Mania](https://iphone-mania.jp/iphone18-607603/)
- Ghostek / FoldifyCase echo Apple dims and note no single-shell “regular phone case” pattern works — [Ghostek](https://ghostek.com/blogs/articles/does-iphone-duo-need-a-special-case)

### Inferences
CAD checklist for claimed Duo compatibility:
1. Clear hinge swing; no hard stop that forces inner glass contact.
2. Closed stack clearance for inner display coating.
3. Side-button Touch ID open cutout (not covered silicone).
4. MagSafe keep-out / pass-through only on camera half; avoid steel plates that shift coil.
5. Open-mode MagSafe stands need ledge or dual support points.
6. Short closed height (~117.8 mm) vs tall slab MagSafe wallets/banks → redesign footprint.
7. Folio-compatible mounts must tolerate side exposure and optional cover-over-display.

### Gaps
- No Apple Accessory Design Guidelines chapter for iPhone Duo located in this pass.
- Quantitative max clamp force / hinge crush load not published.
- Reddit r/iPhoneFold caliper threads: not systematically harvested here; treat any single Reddit numbers as low confidence unless corroborated.

---

## Open CAD / Printables / MakerWorld models claiming iPhone Duo dimensions (quality cross-check)

### Takeaway
Useful **visualization mockups** exist on MakerWorld based on Apple’s published overall dims, but authors **explicitly forbid** using them for precision case/mount design. Printables search is dominated by **MagSafe Duo charger** stands (wrong product). No trusted STEP/caliper accessory reference for retail Duo hardware was found as of 2026-10-22.

### Cited Findings

#### Correct product (foldable iPhone Duo) — mockups
- MakerWorld size mockups open+folded: uses Apple **164.6 × 117.8 × 5.2** open / **84.1 × 117.8 × 11.3** folded; camera/details approximated from imagery; **“should NOT be used to design cases… mounts, accessories, precision-fit components”** — [MakerWorld 3285874](https://makerworld.com/en/models/3285874-iphone-duo-size-dimension-mockups-open-folded)
- MakerWorld folding mockup: print-in-place hinge; author corrected earlier profile that was **~2.25 mm too narrow** when folded — [MakerWorld 3286427](https://makerworld.com/en/models/3286427-iphone-duo-folding-mockup)
- Printables-listed “Print-in-Place Folding iPhone Duo Mockup”: Apple overall dims only; features from photos; **not appropriate for designing cases or accessories** — [3dgo / Printables mirror](https://3dgo.app/models/printables/1842837)
- MakerWorld ergonomic mockup: closed width listed **84.6 mm** (vs Apple 84.1); hinge adds ~**0.5 mm**; camera projection estimated **3.2 mm**; AI-assisted; not precision — [3dgo / MakerWorld 3287054](https://3dgo.app/models/makerworld/3287054)
- MakerWorld MagSafe desk stand for **phone** Duo + MagSafe puck: dual 15W/25W profiles; claims folded/open support — [MakerWorld 3395379](https://makerworld.com/en/models/3395379-iphone-duo-magsafe-desk-charging-stand)

#### Wrong product (MagSafe Duo charger) — do not use for iPhone Duo envelopes
- Printables: Stitch TEC MagSafe Duo Charger Stand — [Printables 383203](https://www.printables.com/model/383203-magsafe-duo-charger-stand-for-iphone-apple-watch-v)
- Printables: RoyBa MagSafe Duo Stand (StandBy) — [Printables 589547](https://www.printables.com/model/589547-magsafe-duo-stand-standby-mode)
- Printables: rojoPrint Apple Duo Charger StandBy stand — [Printables 930090](https://www.printables.com/model/930090-apple-duo-charger-stand-for-standby-mode)

#### Official CAD drawings
- Apple MagSafe Charger dimensional drawings available; **iPhone Duo device drawings not found** in Developer accessories list during this research — [Apple Developer dimensional drawings](https://developer.apple.com/accessories/dimensional-drawings/)

### Inferences
- Safe use of community models: pocket feel, rough stand height studies, MagSafe puck bore experiments.
- Unsafe use: case lips, camera cutouts, hinge bridges, MagSafe ring plates requiring ±0.2 mm fit.
- Prefer Apple published H×W×D + post-launch caliper campaigns (FoldifyCase commitment) over any STL “iPhone Duo” claim.

### Gaps
- No verified STEP of Duo or official cases.
- No community caliper CSV/dataset of retail Duo as of research date (launch eve).
- MakerWorld MagSafe phone-stand model lacks published bore tolerances / MagSafe center offsets in the scraped description.

---

## Quick reference table for CAD (as of 2026-10-22)

| Item | Value | Class |
| --- | --- | --- |
| Phone closed H×W×D | 117.8 × 84.1 × 11.3 mm | Apple-official |
| Phone open H×W×D | 117.8 × 164.6 × 5.2 mm | Apple-official |
| Phone mass | 254 g | Apple-official |
| MagSafe / Qi2 | up to 25W; single camera-half array | Apple-official + AppleInsider |
| Duo Case | 2-pc PC + adhesive; MagSafe in camera half; hinge open | Apple-official + Measured hands-on |
| Folio mass | 58 g | Measured (iPhone Mania) |
| Folio kickstand | ~90° max observed; MagSafe behind open stand | Measured + Apple-official charging claim |
| Slim 2-face case closed estimate | ~13.3 mm (@1 mm/face) | Derived (FoldifyCase) |
| MagSafe 25W puck | Ø≈55.4–55.5 mm, t≈4.45–4.53 mm | Measured (ChargerLAB) |
| MagSafe 15W puck (legacy) | Ø≈55.9 mm, t≈5.5 mm | Community Measured |
| Apple STEP of Duo | Not found | Gap |
| Retail Duo calipers | Not yet (launch 2026-10-23) | Gap |
