# Work Log

## 2026-08-11 — SORA IRB submission drafts

- **What we did:** Reviewed the local protocol, RFK letter, MAPS clinic script, clinic email template, and federal guidance; drafted an editable IRB packet and clinic data instrument. Revised the central dataset to contain only clinic row ID, sex, age at onset in months, Dpre, and Dpost. Clinics retain the ID mapping and all source dates/clinical details.
- **Command / executable:** `irb_submission/build_irb_packet.py`; WSL Pandoc DOCX-to-Markdown conversion.
- **Outputs:** `irb_submission/SORA_IRB_Submission_Packet_v1.0.md`, `irb_submission/SORA_Data_Collection_Instrument_v1.0.md`, and corresponding `.docx` drafts.
- **Results:** Working Markdown sources and editable Word drafts created. The packet includes protocol, statistical analysis plan, privacy/security plan, waiver language, collection instrument, COI disclosure, references, and submission checklist.
- **Next steps:** PI/statistician/privacy officer should resolve bracketed institutional fields, determine the applicable IRB/HIPAA pathway, complete the simulation-based power calculation, and approve the public-release process.

## 2026-08-11 — Electronic clinic submission clarified

- **What we did:** Revised the protocol and instrument to require electronic Excel/CSV upload and explicitly prohibit paper, scanned, photographed, faxed, handwritten, or email-body submissions. Created a validated Excel template with five approved columns.
- **Command / executable:** `irb_submission/build_electronic_template.mjs`.
- **Outputs:** `outputs/sora_irb/SORA_Electronic_Data_Submission_Template_v1.0.xlsx` and updated Markdown/Word drafts.
- **Results:** Electronic workflow is now explicit; the workbook passed structural inspection, formula-error scanning, and visual review of both sheets.
- **Next steps:** Replace the secure-upload-portal placeholder with the chosen service before submission.

## 2026-08-11 — Consolidated IRB submission bundle

- **What we did:** Consolidated the master protocol and electronic instrument into one directory and added editable clinic recruitment, waiver, privacy/attestation, funding/COI, investigator/site, external-items, and submission-checklist documents.
- **Command / executable:** File assembly plus Markdown drafting.
- **Outputs:** `irb_submission/IRB_SUBMISSION_BUNDLE/` containing ten numbered submission files.
- **Results:** All locally preparable IRB materials are in one directory; externally issued CVs, training records, institutional forms, agreements, and final IRB determinations are itemized separately.
- **Next steps:** Resolve bracketed placeholders and add institution-issued documents before submission.
