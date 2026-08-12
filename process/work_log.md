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

## 2026-08-11 — Pandoc Word conversion of main IRB packet

- **What we did:** Converted the current submission-bundle Markdown source directly to DOCX with Pandoc.
- **Command / executable:** `wsl pandoc irb_submission/IRB_SUBMISSION_BUNDLE/01_SORA_IRB_Submission_Packet.md --from=gfm --to=docx`.
- **Outputs:** `irb_submission/IRB_SUBMISSION_BUNDLE/01_SORA_IRB_Submission_Packet.docx`.
- **Results:** Structural validation found 125 paragraphs, 7 tables, and 39 headings; the exemption language, moving-window analysis, and references 1–7 are present. Microsoft Word PDF export timed out, so visual PDF QA was not completed.
- **Next steps:** Open in Word for a final pagination check before formal submission.

## 2026-08-11 — Multisite enrollment and site-code revision

- **What we did:** Updated the submission bundle for at least 300 eligible records from at least five clinics and added a nonidentifying `site_code` to the transmitted dataset. Added site-stratified, leave-one-site-out, and cluster-aware analyses; revised privacy, waiver, recruitment, attestation, personnel, and instrument language.
- **Command / executable:** `irb_submission/build_electronic_template.mjs`; Pandoc conversion of the edited master Markdown.
- **Outputs:** Updated `IRB_SUBMISSION_BUNDLE/01_SORA_IRB_Submission_Packet.md`, its DOCX, supporting Markdown files, and six-column Excel template.
- **Results:** Workbook contains 400 entry rows and six validated columns, passed structural/error checks, and both sheets passed visual review.
- **Next steps:** Statistician should finalize the simulation-based minimum sample size and cluster model before data collection.

## 2026-08-11 — Panel-response redesign and unvaccinated reference

- **What we did:** Revised the IRB protocol in place following the three-reviewer panel. Removed the uniform-onset assumption; added unvaccinated-before-onset SORA cases as an empirical age-at-onset reference; made Dpost optional/secondary; added a seven-field patient dataset and four low-burden aggregate vaccination-status-through-24-month counts; strengthened site-engagement, HIPAA, public-release, onset, compensation, and preregistration language.
- **Command / executable:** Targeted Markdown patches; `irb_submission/build_electronic_template.mjs`; Pandoc conversion from the current bundle Markdown.
- **Outputs:** Updated main Markdown/DOCX, supporting bundle documents, and `03_SORA_Electronic_Data_Submission_Template.xlsx` with Data Entry, Instructions, and Site Summary sheets.
- **Results:** Workbook passed structural/error checks and visual review on all three sheets. Dpre timing scans are explicitly exploratory unless the statistician approves a defensible null model before database lock.
- **Next steps:** Statistician must finalize the age-distribution test, any scan null/randomization method, pooling across sites, and power simulation before IRB approval.

## 2026-08-11 — Cross-fitted age-at-onset reference

- **What we did:** Replaced the uniform within-vaccination-interval model and the underpowered unvaccinated-only histogram with a smooth, site-cross-fitted curve of age at parent-recognized SORA onset among all qualifying cases. Retained unvaccinated-before-onset cases as a supplementary comparison, preserved the inclusive Dpre histogram, and changed onset age from completed months to whole days throughout the packet.
- **Command / executable:** Targeted Markdown patches; `irb_submission/build_electronic_template.mjs`; Pandoc conversion from the canonical bundle Markdown.
- **Outputs:** Protocol Version 1.1 in Markdown/DOCX, updated waiver and clinic documents, and regenerated seven-column electronic workbook.
- **Results:** Workbook passed structural/error checks and visual review on all three sheets; consistency search and `git diff --check` passed.
- **Next steps:** The statistician must prespecify the smooth model, bandwidth, site cross-fitting, inferential calibration, site heterogeneity handling, and simulation-based operating characteristics before database lock.
