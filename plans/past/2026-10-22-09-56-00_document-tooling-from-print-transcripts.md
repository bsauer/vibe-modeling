---
plan_id: 2026-10-22-09-56-00_document-tooling-from-print-transcripts
title: Document tooling knowledge from print transcripts
summary: Capture reusable Snapmaker U1, Snapmaker Orca, and SnapSpeed PLA facts from recent print sessions into references/tooling/.
status: past
created_at: 2026-10-22-09-56-00
---

# Document tooling knowledge from print transcripts

Sources (agent transcripts):

- [iPhone Duo plate trim](ca6aa2d4-451f-4406-9bf4-6d5baa660a69)
- [Duo stand Orca review](ab7b0a54-df61-425e-adf0-49fc83433f37)

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Create `references/tooling/` layout and index.
  - [x] 1.1 Add `references/tooling/README.md` with category map and provenance rules.
  - [x] 1.2 Document Snapmaker U1 printer facts.
  - [x] 1.3 Document Snapmaker Orca slicer facts (3MF portability, scarf enum, paint workflows).
  - [x] 1.4 Document Snapmaker PLA SnapSpeed filament facts.
  - [x] 1.5 Add generic notes only where transcripts support them (bed-edge clearance, nozzle/time tradeoffs).
- [x] 2. Wire host indexes and leave design-specific change lists as design-owned.
  - [x] 2.1 Index tooling refs in `AGENTS.md` and `README.md`.
  - [x] 2.2 Cross-link the Duo stand change list to the reusable tooling notes.
  - [x] 2.3 Journal the checkpoint; do not invent CAD/CAD-app content the transcripts lack.
- [x] 3. Verification.
  - [x] 3.1 Confirm no duplicate authoritative settings tables conflict with the design change list (tooling refs stay generic; design file stays design-specific).
  - [x] 3.2 Confirm CAD-application category is indexed as empty/future only.
