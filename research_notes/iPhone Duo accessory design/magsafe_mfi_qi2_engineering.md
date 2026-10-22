# MagSafe, MFi, and Qi2 engineering documentation for accessory design

Research date: 2026-10-22. Primary sources preferred. Figure dimensions below were read from Apple’s public PDF drawings (not OCR-invented); where a number appears only in a drawing caption description, it is attributed to that figure.

## What public MagSafe / MagSafe Duo charger / Qi2 mechanical or magnetic specs exist?

### Takeaway
Apple publishes substantial MagSafe *Attach* mechanical/magnetic requirements in the free Accessory Design Guidelines PDF (updated 2026-09-21), including magnet-ring diameters, polarity cross-sections, pull-force targets, clearance/keep-in rules, and enclosure-spline envelopes. MagSafe Duo Charger documentation is consumer power/use guidance plus teardowns; full Duo mechanical CAD is not in that public MagSafe Attach chapter. WPC publishes Qi2/Qi2 25W marketing and certification summaries; the latest full Qi specification (v2.3) is members-only, with an older public download package available.

### Cited Findings
- Apple Developer Accessories hub offers a free PDF **Accessory Design Guidelines for Apple Devices**, updated **September 21, 2026**, plus device dimensional drawings — [Apple Developer Accessories](https://developer.apple.com/accessories/); [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Chapter **42 MagSafe Attach** (PDF pp. 270–288) defines MagSafe Case Magnet Array, MagSafe Accessory Magnet Array, enclosure geometry, and verification procedures — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Chapter **22 Apple MagSafe Charger Mounts** (PDF p. 223) covers stands/docks that hold an *Apple MagSafe Charger* (not necessarily integrating a charger coil), pointing keep-in regions to Dimensional Drawings — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Chapter **37 Device Power (Inductive)** requires Qi transmitters to use a Qi Certified subsystem or be Qi Certified to Power Class 0 Spec Version **2.0 or later**, and recommends **version 2.2 or later**; MagSafe and Qi device support lists are published in that chapter — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- MagSafe Charger consumer power: up to **25W** peak on listed recent iPhones with charger P/Ns A3502/A3503/A2580/A3250 and ≥30W / 15V·2A adapters; older A2140 path up to **15W**; iPhone Air **20W**; iPhone 16/16 Pro **22.5W** — [Apple Support HT211829 / 105047](https://support.apple.com/en-us/HT211829) (published 2026-09-18).
- MagSafe Duo Charger (discontinued): up to **14W** iPhone peak (12W on mini), negotiates up to **9V·3A**, dual-device needs ≥15W adapter; Watch side is Apple Watch inductive (not MagSafe phone array) — [Apple Support 111812](https://support.apple.com/en-us/111812); discontinued Sept 2023 per secondary summary — [Wikipedia MagSafe (wireless charger)](https://en.wikipedia.org/wiki/MagSafe_(wireless_charger)).
- Forbes review (secondary product dimensions): MagSafe Duo ~**3.0 × 6.5 in** open, ~**3 in** square × **0.5 in** folded — [Forbes MagSafe Duo review](https://www.forbes.com/sites/bradmoon/2022/02/21/review-apple-magsafe-duo-charger/).
- FCC A2458 “two coil charger” filings exist (images/manuals/RF reports cited by secondary press); this research did not retrieve exhibit drawings — [iMore FCC approval note](https://www.imore.com/magsafe-duo-charger-gets-fcc-approval-ahead-imminent-release).
- WPC: Qi v2.0 (2023) / Qi v2.2.1 branded **Qi2 25W** launched **July 2025**; public page states Qi2 magnetic attachment and ~0→50% in ~30 minutes at 25W marketing claim — [WPC Qi Wireless charging](https://www.wirelesspowerconsortium.com/standards/qi-wireless-charging/); [Qi2 25W news release PDF](https://www.wirelesspowerconsortium.com/media/wvsmia32/qi2-25w-news-release-v72.pdf).
- WPC: “latest Qi Specification version **v2.3** is available for WPC Members only”; a “latest publicly available” zip is linked; test/compliance books are members-only — [Download the Qi Specifications](https://www.wirelesspowerconsortium.com/knowledge-base/qi-specification/download-the-qi-specifications/).
- iPhone Duo (Apple primary): supports MagSafe wireless charging and **Qi2 25W** or Qi-certified chargers; official cases MagSafe/Qi2 25W/Qi-compatible; wireless ~50% in ~30 minutes with MagSafe or Qi2 — [apple.com/iphone-duo](https://www.apple.com/iphone-duo/); [Apple Newsroom 2026-09-09](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/).
- MacRumors (secondary): Duo MagSafe up to **25W**, also Qi2 25W third-party — [MacRumors 2026-09-09](https://www.macrumors.com/2026/09/09/iphone-duo-supports-magsafe-charging/).
- Measured/community MagSafe *charger puck* OD ~**55.9 mm** (Reddit caliper claim; not Apple) — [r/MagSafe dimensions thread](https://www.reddit.com/r/MagSafe/comments/mbsf40/could_anyone_provide_me_the_dimension/).
- iFixit/X-ray coverage of MagSafe charger shows circular magnet array + Qi coil alignment role; no official diameter table in that writeup — [iDownloadBlog on iFixit MagSafe teardown](https://www.idownloadblog.com/2020/10/23/magsafe-ifixit-teardown/).

### Inferences
- For magnet-array geometry and accessory envelopes, Apple’s public MagSafe Attach chapter is the authoritative open source—not an NDA-only MFi package alone.
- MagSafe Duo Charger mechanical reverse-engineering is sparse in primary Apple docs; treat review/FCC/teardown numbers as non-authoritative for production CAD.
- Qi2 magnetic geometry is intended to interoperate with MagSafe-class magnetic alignment, but Apple’s MagSafe Attach drawings remain the concrete public mechanical reference for MagSafe-branded attach.

### Gaps
- Exact numerical coordinates from Dimensional Drawings “keep-in” packages for MagSafe Charger mounts were not downloaded in this pass (portal link only).
- MagSafe Duo FCC exhibit mechanical drawings not retrieved.
- Full WPC Qi v2.2.1 / v2.3 magnet/coil keepout tables not accessible without WPC membership (member-gated).
- Accessory Design Guidelines dated 2026-09-21 device lists for MagSafe/Qi **do not include “iPhone Duo”** by name in the extracted text—Duo-specific MagSafe placement drawings may lag consumer marketing.

## What does MFi cover for cases vs chargers vs stands?

### Takeaway
MFi is Apple’s licensed-technology program for accessories that use named MFi technologies/components (iAP2, Lightning, HomeKit, Find My, authentication coprocessors, etc.). Pure protective cases without MFi components are explicitly *outside* MFi; MagSafe mechanical attach guidance lives in the public Accessory Design Guidelines. Active MagSafe *chargers* that use Apple’s licensed MagSafe charging path are commonly marketed as “Made for MagSafe” under Apple’s licensing ecosystem; passive mounts that only cradle an Apple MagSafe puck are guided by Chapter 22, not as MFi electronics.

### Cited Findings
- MFi FAQ: program covers third-party hardware using **MFi licensed technology** to connect electronically; technology table lists AirPlay audio, CarPlay, Find My, HomeKit, iAP2, DockKit, Game Controller, Hearing Aid, WAC, etc., plus components (auth coprocessors, Lightning, Watch Fast Charger Module, …) — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- MFi FAQ: **not** part of MFi includes USB-C charging accessories (without MFi tech), standard Bluetooth profiles, BLE (with HomeKit/Hearing Aid exceptions), headphone-jack accessories without MFi tech, and **“Cases that don't integrate MFi components (e.g., protective cases and folios)”** — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- Who does not need to join: developers of **non-electronic accessories** such as protective cases; Apple points them to accessory design guidelines — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- Royalty/fee details for licensed accessories: “only available under NDA” after license approval; program fee **USD $99**/year — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- Apple Developer Accessories “Get Started” product types distinguish **MagSafe Attach accessory**, **MagSafe charger**, case subtypes **MagSafe Attach / MagSafe case module / Non-electronic**, and separately routes some paths to MFi — [developer.apple.com/accessories](https://developer.apple.com/accessories/).
- Cases claiming MagSafe or Qi wireless power **2.0+** shall integrate MagSafe Case Magnet Array and must not have rear card pockets — Guidelines §5.1.4 — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Wikipedia (secondary): Apple licenses MagSafe; officially licensed third-party products called “Made for MagSafe”; early launch Belkin exclusive MagSafe charging license narrative — [Wikipedia MagSafe (wireless charger)](https://en.wikipedia.org/wiki/MagSafe_(wireless_charger)).
- Macworld (secondary market framing): “MagSafe compatible” ≠ “Made for MagSafe”; magnets alone do not equal licensed MagSafe charging — [Macworld](https://www.macworld.com/article/334301/buyer-beware-magsafe-compatible-is-not-the-same-as-made-for-magsafe.html).
- Apple MagSafe Charger Mounts chapter: mounts hold/position Apple MagSafe Charger; for integrating wireless charging see Device Power (Inductive) — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) §22.

### Inferences
- **Cases (passive magnets):** design/test against public MagSafe Attach case rules; MFi enrollment not required solely for magnets/enclosure if no MFi component.
- **Chargers (active WPT):** need **Qi certification** per Apple guidelines; “Made for MagSafe” / MagSafe-branded high-power MagSafe path involves Apple licensing beyond the public PDF (details NDA).
- **Stands/mounts:** (a) puck-holder mounts → §22 MagSafe Charger Mounts; (b) integrated inductive stand → Qi + MagSafe Accessory Magnet Array / clearance; (c) StandBy mounts → §23 (landscape, charging, ≥30° tilt recommendation, Qi 2.0+ or MagSafe Accessory Magnet Array).

### Gaps
- Public MFi FAQ technology table on the scraped page does **not** explicitly list “MagSafe” as a row; Made-for-MagSafe program mechanics beyond marketing/secondary sources remain partly opaque without MFi portal access.
- Exact badge rules for printing “MagSafe” / “Made for MagSafe” on packaging were not found in a public Apple legal page in this pass.

## Are there public magnet ring diameters, pull force, coil keepouts, or only proprietary MFi packages?

### Takeaway
Public numbers exist in Apple’s Accessory Design Guidelines MagSafe Attach chapter (and figures). They are not exclusively locked in MFi NDA packages. Coil keepouts for MagSafe *attach accessories* are framed as clearance/enclosure-spline rules around the magnet-array center; full Qi coil electromagnetic keepouts remain primarily in WPC member specs.

### Cited Findings — MagSafe Case Magnet Array (public)
- Cases: uniform thickness **≤2.1 mm** (Apple recommends **2.0 mm**); must enclose device; firm attach without relying on magnets; no other back magnets; work with Apple MagSafe Charger and FineWoven Wallet — Guidelines §42.1.1 — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Self-alignment: MagSafe accessories shall self-align within **1.55 mm** radial maximum — §42.1.2 / §42.2.2 — same PDF.
- Case magnets: **N45SH NdFeB**, epoxy coating **8–16 µm**; Br **13.2–13.6 kGs**, Hcb min **12.75 kOe**, Hcj min **20.50 kOe**, BHmax **43–46 MGOe**; surface gauss **≤0.215 T** interior/exterior — Table 42-1 / §42.1.2.1 — same PDF.
- Pull force (case with accessory such as Apple MagSafe Charger): nominal target **1000–1300 gf** normal to case back — §42.1.2.3 — same PDF.
- Figure 42-2 (case array dimensions, PDF p. 273): outer Ø **54.10 mm**, inner Ø **46.00 mm**; datum B center within **±0.30 mm** of integrated product center; orientation magnet width **6.00 mm**, vertical span from center **31.18 mm** to **50.49 mm** (height **19.31 mm**) — figure read from [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) p. 273.
- Figure 42-3 (ring polarity cross-section, p. 274): magnet thickness **0.55 mm**; cross-section width **4.05 mm**; outer/inner pole widths **1.150 mm** each; non-magnetized gap **2.800 mm** with |Bz| **<80 mT**; depth toward device **0.55±0.05 mm**; toward accessory max **0.85 mm** — same PDF.
- Figure 42-4 (orientation magnet polarity, p. 274): **6.00 mm** wide, **0.55 mm** thick; three segments (~**1.167 mm**) with outer N / middle S toward device — same PDF.
- Recommended magnet-array vendors listed publicly: Baotou INST, Ningbo Sanhuan Magsound, Quadrant Solutions — §42 — same PDF.

### Cited Findings — MagSafe Accessory Magnet Array (public)
- Configurations: Magnet Ring, Extended Magnet Ring (higher force esp. iPhone Air), optional Orientation Magnet — §42.2 — same PDF.
- Accessory magnets: **N48H NdFeB**, NiCuNi plating **7–13 µm**; Br **13.7–14.1 kGs**; BHmax **45–48 MGOe**; surface flux density **≤0.215 T** — Table 42-2 — same PDF.
- Clearance / keep-in (§42.2.2.1): magnetic attach surface shall **not exceed 30 mm** from magnet-ring center toward device top edge for supported orientations; if any orientation, **≤30 mm radius**; maintain **6 mm** clearance for any part past the 30 mm keep-in; stay within MagSafe Accessory Enclosure Geometry — same PDF.
- Accessory pull force Table 42-3: **650–1510 gf** when accessory attached to device — same PDF.
- Figure 42-7 (accessory magnet ring, p. 278): outer Ø **54.10 mm**, inner Ø **46.00 mm**; datum B within **±0.30 mm** of device center; segment angular layout with **45°** intervals / **22.50°** offset; max opening **8.25 mm**; **2× 10.00°** max array magnet gap — same PDF.
- Enclosure geometry §42.3 / Figure (p. 284): max-material spline; transition near **Y≈27.2–30.0 mm**, **Z** up to ~**0.92 mm**, **2.00°** draft — same PDF.
- DC shield: low-carbon steel (1010/DT4 or similar), Ni plating **5–10 µm**, Bsat **≥2.0 T** — §42.2.2.7 — same PDF.

### Cited Findings — Qi / third-party measured (not Apple MagSafe Attach)
- Qi full magnet/coil specs: latest v2.3 member-only; public older package exists; test books member-only — [WPC download page](https://www.wirelesspowerconsortium.com/knowledge-base/qi-specification/download-the-qi-specifications/).
- Aftermarket MagSafe *steel rings* commonly sold as **56×46×1 mm** (ferromagnetic plate for stick-on rings; not Apple spec) — e.g. [TotalElement product listing](https://totalelement.com/products/56-x-46-x-1mm-steel-ring-for-magsafe-phone-accessories-42-pack).
- Supplier blog claims MagSafe magnet OD **54 mm** / ID **46 mm** (aligns with Apple figure OD/ID) — [Fullzen](https://www.fullzenmagnets.com/news/what-size-is-magsafe-magnet/) (secondary).
- Reddit claim of MagSafe case pull **800–1100 gf** and N45 (differs from current Apple case target 1000–1300 gf / N45SH) — [r/MagSafe](https://www.reddit.com/r/MagSafe/comments/1vgk3q2/magnet_strength_of_magsafe_ring_in_phone_case/) — treat as unverified vs Guidelines.

### Inferences
- A designer can legally *read* Apple’s public MagSafe Attach magnet diameters, grades, forces, and keep-ins without MFi; compliance for commercial MagSafe-branded claims and MagSafe charging electronics is a separate licensing/certification question.
- “Coil keepout” in Apple MagSafe Attach language is largely **accessory clearance + enclosure spline + MagSafe Battery Pack interference checks**, not a published Qi winding geometry.

### Gaps
- Individual discrete magnet arc lengths for every segment are only fully specified in figures; this note captures key Ø and polarity values from figures 42-2/42-3/42-4/42-7 but not every Extended Ring / orientation figure dimension.
- Official Apple coil OD / Tx–Rx gap for MagSafe Charger electronics not published in MagSafe Attach chapter.
- iPhone Duo magnet-array absolute placement on folded vs unfolded halves: not in Guidelines device list as of 2026-09-21 extract.

## How do Qi2 and MagSafe relate for 2026 iPhones?

### Takeaway
Qi2’s Magnetic Power Profile is the industry standard built on MagSafe-class magnetic alignment. Apple MagSafe remains Apple’s proprietary branding/ecosystem (including MagSafe Attach accessories and Apple MagSafe Charger power negotiation). For 2026 devices including iPhone Duo, Apple publicly states MagSafe *and* Qi2 25W / Qi-certified charging support; Accessory Guidelines require MagSafe Case Magnet Array for MagSafe *or* Qi wireless power 2.0+ case claims, and Qi certification for inductive transmitters.

### Cited Findings
- WPC: Qi2 brought magnetic attachment + 15W; Qi2 25W (Qi v2.2.1, July 2025) ~70% more power; certification via authorized labs; logo only for Qi Certified products — [WPC Qi page](https://www.wirelesspowerconsortium.com/standards/qi-wireless-charging/); [Qi2 25W release](https://www.wirelesspowerconsortium.com/media/wvsmia32/qi2-25w-news-release-v72.pdf).
- Wikipedia (secondary synthesis): MagSafe first gen ≤15W / Qi ≤7.5W; later MagSafe ≤25W with Qi2 ≤15W then revised MagSafe Charger with Qi2 25W (2025); Qi2 based on MagSafe — [Wikipedia MagSafe (wireless charger)](https://en.wikipedia.org/wiki/MagSafe_(wireless_charger)).
- Apple MagSafe Charger support lists peak MagSafe watts by iPhone generation and charger P/N; distinguishes MagSafe vs non-MagSafe Qi devices — [Apple Support](https://support.apple.com/en-us/HT211829).
- Apple Guidelines §5.1.4: MagSafe **or** Qi wireless power **2.0 or later** cases shall integrate MagSafe Case Magnet Array — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- Apple Guidelines §37.1: Qi transmitters shall be Qi Certified (v2.0+; should support v2.2+) — same PDF.
- iPhone Duo: MagSafe + Qi2 25W / Qi-certified — [apple.com/iphone-duo](https://www.apple.com/iphone-duo/); [Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/).
- Wired (secondary explainer): Qi2 headline is Magnetic Power Profile based on Apple MagSafe — [WIRED What Is Qi2](https://www.wired.com/story/what-is-qi2-wireless-charging/).

### Inferences
- Mechanically, designing to Apple MagSafe Case/Accessory magnet arrays is the practical path for Qi2-MPP-style snap alignment on iPhones.
- Electrically/protocol-wise, third-party *chargers* need WPC Qi certification for Qi/Qi2 logos and Apple’s inductive-power shall-requirements; MagSafe-branded max power and NFC accessory features may still require Apple MagSafe licensing beyond Qi2.

### Gaps
- Whether iPhone Duo MagSafe array is on the outer back only, and how fold angle affects mount stability, is not specified in the Guidelines extract (secondary reporting notes unfolded Duo tipping MagSafe stands — [MacRumors related headline](https://www.macrumors.com/2026/10/21/iphone-duo-magsafe-charging/) — not verified here).
- Exact protocol differences MagSafe 25W vs Qi2 25W on Duo (negotiation IDs, authentication) are not public in Apple Support text.

## What can a 3D-printed accessory designer legally/practically design without MFi vs what requires certification?

### Takeaway
Without MFi, a maker can practically design pure mechanical MagSafe *puck mounts*, passive magnetic stands/wallets following public MagSafe Attach geometry, and non-electronic cases that follow Guidelines—while avoiding MagSafe trademark/badge misuse and medical-device interference claims. Active wireless chargers need Qi (and often regulatory EMC/FCC) certification; MagSafe-branded charging modules / Made for MagSafe need Apple licensing. “Compatible with MagSafe chargers” as descriptive language is common for magnet-only products; official MagSafe logos/badges are not free.

### Cited Findings
- Non-electronic cases / no MFi components: MFi not required — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- Individuals creating accessories for personal use: MFi FAQ says individuals need not join; recommends hobbyist solutions for serial — [mfi.apple.com FAQs](https://mfi.apple.com/en/faqs.html).
- Public MagSafe Attach dimensions/forces/clearance enable modeling magnet pockets and accessory envelopes — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) §42.
- MagSafe Charger Mounts (§22): hold Apple MagSafe Charger; maintain clearance; keep charger secure; keep-ins in Dimensional Drawings — same PDF.
- Integrating wireless charging: Device Power (Inductive) → Qi Certified — same PDF §37.
- StandBy mounts: may be MagSafe Charger mounts; if implementing wireless power use Qi 2.0+ **or** MagSafe Accessory Magnet Array — §23 — same PDF.
- Apple Support magnets/medical: keep wireless chargers / magnets away from implanted devices (typical manufacturer guidance ≥6 in / 15 cm, ≥12 in / 30 cm for wireless chargers) — [support.apple.com/109025](https://support.apple.com/en-us/109025).
- Market practice: “MagSafe compatible” often magnets-only vs “Made for MagSafe” licensed — [Macworld](https://www.macworld.com/article/334301/buyer-beware-magsafe-compatible-is-not-the-same-as-made-for-magsafe.html).
- Cases claiming MagSafe/Qi2: must integrate MagSafe Case Magnet Array; thickness ≤2.1 mm over array; no card pockets — Guidelines §5.1.4 / §42.1 — [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).
- iPhone Duo official cases use built-in magnets aligned for MagSafe/Qi2 25W — [Apple Newsroom](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/).

### Inferences — practical design matrix
| Accessory type | Typical without MFi? | Still need |
| --- | --- | --- |
| 3D-printed stand holding Apple/third-party MagSafe *puck* | Yes (mechanical §22) | Clearance, stability, trademark care |
| Passive MagSafe wallet/mount with magnet array | Yes for MFi; follow §42.2 | Pull-force/compass risk; MagSafe logo rules |
| MagSafe-compatible phone case (magnets only) | Yes for MFi if non-electronic | §42.1 geometry; Qi/MagSafe claim truthfulness |
| Qi2/MagSafe wireless charger product | No for full MagSafe licensing; Qi cert required | WPC Qi cert + EMC/FCC + possibly MagSafe license |
| MagSafe NFC accessory / Find My wallet features | Likely MFi/related Apple programs | NDA specs |

### Gaps
- This note is **not legal advice**; trademark enforcement (“MagSafe”) and false-advertising risk for “Made for MagSafe” claims were not researched via Apple Trademark List primary pages.
- Duo-specific dimensional drawings for case envelopes were not obtained; foldable hinge magnet arrays for *closure* (Newsroom) are distinct from MagSafe charging array and need separate mechanical study.
- Regulatory: FCC Part 15 / wireless power product certification paths not fully mapped beyond Guidelines EMC pointers.

## Source index (drawings / PDFs / portals)

| Resource | Access | Notes |
| --- | --- | --- |
| [Accessory Design Guidelines PDF](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) | Public | MagSafe Attach §42, MagSafe Charger Mounts §22, StandBy §23, Inductive Power §37; dated 2026-09-21 |
| [Apple Developer Accessories](https://developer.apple.com/accessories/) | Public | Guidelines + dimensional drawings portal; MagSafe Attach vs MagSafe charger product types |
| [Dimensional Drawings](https://developer.apple.com/accessories/dimensional-drawings/) | Public portal | Keep-ins for MagSafe Charger mounts (not fetched in-depth here) |
| [mfi.apple.com](https://mfi.apple.com/) / [FAQs](https://mfi.apple.com/en/faqs.html) | Public FAQ; rest gated | Program scope; NDA for royalties/manufacturers list |
| [Apple MagSafe Charger support](https://support.apple.com/en-us/HT211829) | Public | Power classes / adapter requirements |
| [MagSafe Duo support](https://support.apple.com/en-us/111812) | Public | Duo charger power/use (product discontinued) |
| [WPC Qi standard](https://www.wirelesspowerconsortium.com/standards/qi-wireless-charging/) | Public summary | Qi2 / Qi2 25W marketing |
| [WPC Qi specs download](https://www.wirelesspowerconsortium.com/knowledge-base/qi-specification/download-the-qi-specifications/) | Mixed | v2.3 members-only; older public zip; test books members-only |
| [Qi2 25W news release PDF](https://www.wirelesspowerconsortium.com/media/wvsmia32/qi2-25w-news-release-v72.pdf) | Public | July 23, 2025 launch statement |
| [Qi Certified Products DB](https://jpsapi.wirelesspowerconsortium.com/products/qi) | Public search | Certification lookup |
| [apple.com/iphone-duo](https://www.apple.com/iphone-duo/) / [Newsroom Duo](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/) | Public | Duo MagSafe + Qi2 25W claims |
| FCC MagSafe Duo A2458 | Public filings (not pulled) | Secondary press only in this note |
| iFixit / ChargerLAB teardowns | Measured/secondary | Magnet layout visuals; limited official dimensions |
