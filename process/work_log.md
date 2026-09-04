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

## 2026-08-11 — Closed statistical and operational defaults

- **What we did:** Advanced the protocol to Version 1.2 and fixed the analysis choices: 60-day reflected Gaussian kernel, 30/90/120-day sensitivity bandwidths, leave-one-site-out reference estimation, fully defined 1–7-day scan statistic, 100,000 Monte Carlo replicates with seed 20260811, Mantel-Haenszel aggregate comparison, no imputation, leave-one-site-out reporting, and a precision rationale for 300 records. Added seven-year retention, quarterly access review, 24-hour incident reporting, secure-transfer defaults, expert-gated row-level release, and sponsor-independence terms.
- **Command / executable:** Targeted `apply_patch` edits and Pandoc export from the canonical Markdown.
- **Outputs:** Updated protocol Markdown/DOCX and synchronized recruitment, waiver, privacy, funding/COI, and external-items documents in `irb_submission/IRB_SUBMISSION_BUNDLE`.
- **Results:** Methodological choices no longer depend on later statistician selection or observed outcomes; only institution-, personnel-, funding-, and site-specific facts remain for completion.
- **Next steps:** Obtain institutional/site determinations, identify the actual secure systems and responsible officials in activation records, complete personnel/COI/funding fields, and have the PI and analyst sign the frozen plan before database lock.

## 2026-08-12 — Google Docs IRB protocol output

- **What we did:** Transferred the canonical Version 1.2 main IRB submission document into the user-specified blank Google Doc and applied native title, heading, bulleted-list, numbered-list, and shaded table-row formatting.
- **Command / executable:** Google Drive `get_document`, `batch_update_document`, document-text readback, and PDF/HTML export checks.
- **Outputs:** `https://docs.google.com/document/d/18cDu3U1KKrFIALAnOxeDpXjO32OK43QHsfSmX5kiOvk`
- **Results:** Connector readback confirmed the correct document ID/title/tab, 38,284 document characters, the complete section sequence through References, and native heading/list structure. PDF and HTML exports completed successfully; local raster inspection of the exported PDF was unavailable.
- **Next steps:** Complete the bracketed PI, institution, IRB, funding, and conflict-of-interest fields before submission.

## 2026-08-12 — CHD SORA data-resource study definition

- **What we did:** Created a separate executive summary defining the proposed CHD-sponsored, Brian Hooker-led multisite SORA data-resource study. Specified first-10-site activation, complete site ascertainment, three SORA change categories, optional documented ASD support level, minimal row-level fields, site screening counts, descriptive outputs, versioned releases, and public/controlled-access data pathways.
- **Command / executable:** Targeted repository search and `apply_patch` authoring.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md`.
- **Results:** The CHD study is now defined independently from the existing MAPS analytic protocol; no existing protocol was overwritten.
- **Next steps:** Confirm the three-category wording, Brian Hooker's exact credentials, CHD legal entity and infrastructure, reviewing IRB, recruitment/data-cutoff dates, and disclosure-access model before producing the detailed IRB packet.

## 2026-08-12 — Corrected CHD SORA categories

- **What we did:** Corrected the CHD executive summary after an erroneous interpretation of the three SORA categories as ASD diagnostic domains.
- **Command / executable:** Targeted `apply_patch` edit.
- **Outputs:** Updated Version 0.2 of `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md`.
- **Results:** The three authoritative categories are now acquisition of a new pathological behavior, loss of an existing behavior or skill, and change in sensory sensitivity; corresponding dataset indicators and descriptive outputs were corrected.
- **Next steps:** Use only these three category definitions when creating the CHD IRB packet and electronic instrument.

## 2026-08-12 — ASD support-level rule

- **What we did:** Removed the mixed/by-domain ASD-level category and specified collection of the highest documented ASD support level.
- **Command / executable:** Targeted `apply_patch` edit.
- **Outputs:** Updated Version 0.3 of the CHD study executive summary.
- **Results:** Allowed values are 1, 2, 3, or not documented; clinic staff never infer a level.
- **Next steps:** Carry this exact rule into the data dictionary and electronic instrument.

## 2026-08-12 — Seven-day SORA category fields

- **What we did:** Replaced the three general category indicators with three parent-observed Day 0–6 fields and specified Yes/No/Not documented coding.
- **Command / executable:** Targeted `apply_patch` edit.
- **Outputs:** Updated Version 0.4 of the CHD study executive summary.
- **Results:** At least one category must be Yes; No requires adequate negative documentation; missing or ambiguous documentation is Not documented; the exact Day 0 onset requirement remains unchanged.
- **Next steps:** Carry the field names, window, and validation rules into the CHD data dictionary and electronic collection instrument.

## 2026-08-12 — Closed CHD executive-summary ambiguities

- **What we did:** Added the 0–60-month onset range, clarified retrospective ascertainment locking, added a Day 0/Day 4 example, specified recruitment shortfall and withdrawal rules, defined sex values, retained vaccination-unknown cases under a three-state rule, added `dpost_status`, clarified 24-month-of-age counts, and removed selected cumulative Dpre windows from the initial data-resource publication.
- **Command / executable:** Targeted `apply_patch` edit and consistency checks.
- **Outputs:** Updated Version 0.5 of the CHD study executive summary.
- **Results:** Vaccination missingness and post-onset follow-up now have explicit machine-readable treatment; the initial publication remains descriptive and does not embed a timing-window hypothesis.
- **Next steps:** Carry Version 0.5 into the CHD data dictionary, workbook, and IRB packet after the remaining organization-specific facts are confirmed.

## 2026-08-12 — CHD summary consistency nits

- **What we did:** Removed the assumption that exactly 10 sites activate from the record-enrollment section and clarified that vaccination-history-unknown records are an eligible/transmitted subset rather than exclusions.
- **Command / executable:** Targeted `apply_patch` edit.
- **Outputs:** Updated Version 0.6 of the CHD study executive summary.
- **Results:** The enrollment language now matches the permitted two-to-ten-site outcome, and screening-flow reporting cannot be misread as excluding vaccination-unknown cases.
- **Next steps:** Use Version 0.6 as the planning definition for the CHD IRB packet.

## 2026-08-12 — Rebuilt CHD IRB punchlist

- **What we did:** Replaced the abbreviated TBD list with a gated punchlist separating CHD-supplied facts, study-team protocol/attachment work, IPAK-EDU information and determinations, per-clinic activation records, and post-collection disclosure/access approvals.
- **Command / executable:** Visual inspection of the supplied OHRP database screenshot and targeted `apply_patch` edit.
- **Outputs:** Updated Version 0.11 of `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md`.
- **Results:** Recorded IPAK-EDU LLC IRB #1, IRB00014237, St. Clair Shores, OHRP/FDA, Active as shown on 12 August 2026; distinguished genuine external pending items from packet materials and study decisions that can be completed now.
- **Next steps:** Obtain CHD/IPAK organizational facts, close protocol decisions B1–B8, and draft the instruments/SOPs and IRB packet listed in B9–B21.

## 2026-08-12 — Credited existing IRB drafting in punchlist

- **What we did:** Inventoried the existing protocol, electronic workbook, collection instructions, recruitment materials, waiver, privacy/attestation, funding/COI, and personnel documents against punchlist items B2–B21 and C9.
- **Command / executable:** Recursive file inventory and targeted content search; `apply_patch` status update.
- **Outputs:** Updated Version 0.11 CHD executive-summary punchlist.
- **Results:** Items with existing substantial or partial source drafts are now labeled accordingly; only genuinely new rules/SOPs or CHD/IPAK/site-specific facts remain described as new or pending.
- **Next steps:** Adapt the existing source materials into a clean CHD packet rather than recreating them.
## 2026-08-12 — Added clinic activation incentive model

- **What we did:** Revised the CHD SORA executive summary to use a 30-calendar-day recruitment period, activation of up to the first 10 fully qualified clinics, and payment of up to $5,000 per activated clinic for approved work and deliverables. Made payment independent of eligible-case count, vaccination timing, findings, and publication; preserved payment eligibility for a valid zero-case submission; and prohibited automatic redistribution of unused site-payment funds.
- **Command / executable:** Manual `apply_patch` edit; `git diff --check` validation.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.12.
- **Results:** The recruitment incentive is tied to timely completion of activation and study work rather than producing qualifying cases.
- **Next steps:** CHD must confirm the clinic-payment budget, fair-value justification, agreement milestones, and final payment schedule for the IRB packet.
## 2026-08-12 — Fixed flat clinic payment

- **What we did:** Changed clinic compensation from “up to $5,000” to a flat $5,000 institutional payment after satisfactory completion of the required work and deliverables, including full payment for a compliant zero-case submission.
- **Command / executable:** Manual `apply_patch` edit; `git diff --check` validation.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.13.
- **Results:** Payment amount no longer varies by effort estimate, eligible-case count, vaccination timing, findings, or number of clinics activated.
- **Next steps:** Define contractual completion criteria and treatment of a clinic that withdraws or submits incomplete work.
## 2026-08-12 — Added minimum ASD source population and payment completion controls

- **What we did:** Required each clinic to document at least 500 unique patients with an ASD diagnosis in its locked retrospective source population. Clarified that activation, an email, or an unsupported zero-case claim does not earn the flat site payment; payment requires complete ascertainment, required datasets/counts and attestation, query resolution, and acceptance.
- **Command / executable:** Manual `apply_patch` edit; `git diff --check` validation.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.14.
- **Results:** The site threshold is based on the predeclared ASD source population, while compensation remains independent of how many SORA cases a clinic classifies.
- **Next steps:** Define the exact documentary evidence for the 500-patient threshold and objective submission-acceptance checklist in the clinic agreement.
## 2026-08-12 — Redesigned SORA study as a clinic-distributed parent survey

- **What we did:** Rebuilt the executive summary from the former clinic chart-abstraction model into a clinic-distributed, parent-completed electronic survey. Added neutral invitation framing, progressive question display and breakoff measurement, coded email/recontact architecture, parent-reported SORA and vaccination timing, clinic campaign requirements, and flat $5,000 compensation for verified campaign completion.
- **Command / executable:** Full `apply_patch` document replacement followed by targeted `rg` consistency searches and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.15.
- **Results:** The design now scales without clinic chart abstraction or patient-list transfer. Clinics must have at least 500 ASD patients and distribute one approved invitation plus two reminders to the complete eligible population. Payment is independent of responses and findings. The proposed regulatory request is now survey exemption 45 CFR 46.104(d)(2), subject to IPAK-EDU's determination, with a minimal-risk alternative.
- **Next steps:** Select the survey platform and privacy architecture; close eligibility, consent/disclosure, duplicate, campaign, and retention rules; then rebuild the full IRB packet and instruments from the revised punchlist.
## 2026-08-12 — Added independent-replication roadmap

- **What we did:** Added the scientific rationale and global replication sequence to the parent-survey executive summary: initial CHD feasibility implementation, independent academic replication, potential NIH-funded confirmation, and separately approved international replications.
- **Command / executable:** Manual `apply_patch` edit; targeted consistency review and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.16.
- **Results:** The document explains how the initial minimal-risk collection generates feasibility evidence and a reusable method while expressly stating that future institutions are not committed and each replication requires separate governance, ethics, privacy, and funding review.
- **Next steps:** Build the formal replication package and prespecification template after the survey and analysis plan are finalized.
## 2026-08-12 — Replaced absolute dates with direct interval reporting

- **What we did:** Revised the parent-survey design so it collects no birth, onset, or vaccination calendar dates. Parents report exact Dpre/Dpost intervals when known or structured ranges otherwise, together with information source, precision, and confidence. Onset remains a recognizable Day 0, while age at onset is reported with units and precision rather than derived from dates.
- **Command / executable:** Manual `apply_patch` edit; targeted date-language review and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.17.
- **Results:** The design reduces identification risk and parent date-recall burden while preserving exact intervals where available and honest interval censoring elsewhere.
- **Next steps:** Finalize the precise onset-age ranges, interval response UI, validation rules, and interval-censored descriptive/statistical methods in the survey and SAP.
## 2026-08-12 — Implemented design-review safeguards and minimum-four enrollment

- **What we did:** Implemented the approved external-review recommendations: clinic-branded recruitment; explicit vaccination-purpose consent; discrete Day 0 and same-day non-ordering rules; justified 500-contactable-ASD-patient threshold; contact-table access limited to recontact/custodian roles; generic university replication; future separate record validation; and pre-lock outcome blinding with independent first-report verification. Added an initial 30-day clinic-enrollment period that automatically extends only when fewer than four clinics activate, ending at the fourth activation or Day 90, with a maximum of 10 clinics. Fully activated clinics may begin campaigns early while substantive results remain sequestered.
- **Command / executable:** Manual `apply_patch` revisions; targeted legacy/consistency searches and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.18.
- **Results:** Clinic-enrollment duration is governed by a prospective count rule rather than outcomes, and early data collection cannot inform selection of later clinics. The study no longer depends on incomplete purpose disclosure or routine PI access to contact identifiers.
- **Next steps:** Convert the fixed principles into the clinic campaign SOP, consent, restricted-dashboard specification, access matrix, data-lock SOP, and formal SAP.
## 2026-08-12 — Fixed campaign schedule, Day 0 screen, and study lock

- **What we did:** Corrected the survey's Day 0 item to distinguish a discrete onset day from gradual change. Fixed each clinic campaign at invitation Day 0, reminders Days 7 and 21, and survey closure Day 35. Added a 14-day post-closure clarification period and an outcome-independent study lock 30 days after the last activated clinic closes its survey.
- **Command / executable:** Manual `apply_patch` edits followed by targeted consistency searches and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.19.
- **Results:** Only respondents answering Yes to the discrete-onset screen enter the SORA timing pathway. Campaign and lock timing cannot change based on response volume, SORA yield, missingness, or timing results.
- **Next steps:** Implement the fixed schedule in the clinic campaign SOP, survey logic, clarification workflow, and formal data-lock procedure.
## 2026-08-12 — Removed parent email and recontact linkage

- **What we did:** Redesigned Version 0.20 as an anonymous-response survey: removed parent email, contact permission, identity mapping, recontact role, clarification messaging, and mapping retention. Added in-survey validation, a final review page, respondent corrections before submission, a withdraw/delete control, disclosed retention of post-consent partial responses, and no retention of pre-consent health answers. Expanded clinic recruitment legal-basis and anonymous-platform metadata requirements.
- **Command / executable:** Manual `apply_patch` revisions; full contact-language and consistency scans; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.20.
- **Results:** Removal of linkable contact data substantially simplifies privacy and strengthens the potential adult-survey exemption argument, while preserving breakoff measurement. The design now prospectively limits early data to a labeled pilot-feasibility report if fewer than four clinics activate by Day 90.
- **Next steps:** Obtain IPAK-EDU's child-subject/exemption determination; finalize clinic HIPAA/legal recruitment pathways, denominator and duplicate rules, executable SORA algorithm, survey/SAP, vendor configuration, and retention schedule.
## 2026-08-12 — Added developmental-pattern and time-since-onset measures

- **What we did:** Added an all-respondent developmental-pattern question distinguishing early atypical/delayed development, plateau, sudden drop, gradual decline, other, and uncertainty. Added broad time-since-onset/change categories to characterize recall conditions. Clarified that clinics invite their complete defined ASD distribution population and that the pattern distribution is a composition/measurement check, not proof of complete response.
- **Command / executable:** Manual `apply_patch` edit; targeted consistency review and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.22.
- **Results:** The survey can describe non-SORA developmental patterns and assess timing completeness by recall horizon without collecting calendar dates. Any external comparison must use prospectively specified, sufficiently comparable definitions and populations.
- **Next steps:** Cognitively test the parent-facing pattern labels and finalize the broad elapsed-time categories and any defensible external benchmark in the survey/SAP.
## 2026-08-12 — Expanded clinic invitations beyond ASD-diagnosed patients

- **What we did:** Corrected the recruitment population so participating autism diagnosis/treatment clinics invite every contactable parent or guardian in their complete defined patient population, including children evaluated but not diagnosed with ASD. Retained 500 ASD-diagnosed patients as a separate clinic-capacity threshold. Limited non-ASD respondents to recruitment, screening, developmental-pattern, and missingness summaries rather than the SORA timing resource.
- **Command / executable:** Manual `apply_patch` edit; targeted population-language review and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.23.
- **Results:** Distribution is no longer conditioned on ASD diagnosis or suspected regression, improving recruitment-composition assessment and preventing clinics from excluding evaluated children without ASD.
- **Next steps:** Define the clinic's complete patient-population boundaries and the limited survey branch for respondents reporting no or unknown ASD diagnosis.
## 2026-08-12 — Corrected synopsis inference language

- **What we did:** Replaced the causal “pile up within 2 days” statement with a neutral statement that third parties may evaluate the observed temporal pattern against a prespecified null hypothesis while accounting for the survey's limitations.
- **Command / executable:** Manual `apply_patch` edit; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.24.
- **Results:** The synopsis now matches the descriptive initial-study scope and leaves later hypothesis testing to separately specified third-party analyses.
- **Next steps:** Any later analysis must define and justify its null model prospectively rather than treating a uniform timing distribution as automatic.
## 2026-08-12 — Added measurement-quality and competing-event safeguards

- **What we did:** Added a mechanical 30-day/later-evaluation persistence rule, Day 0 confidence, a short structured competing acute-event module, feasibility-yield simulations, recall-horizon and record-source stratification, detailed clinic contact-coverage metrics, privacy-minimizing duplicate questions, separated Dpost follow-up states, prespecified interval-censoring requirements, and early disclosure-risk review.
- **Command / executable:** Manual `apply_patch` edits; targeted content and contradiction review; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.25.
- **Results:** The initial study remains an unlinked descriptive feasibility/data-resource survey while capturing contextual acute events and measurement quality without adding record uploads or a causal hypothesis test.
- **Next steps:** Finalize the competing-event window, executable duplicate tree, feasibility simulation inputs, survey wording through cognitive testing, and the named interval-censored software/package in the SAP.
## 2026-08-12 — Corrected sub-24-hour Dpre and Dpost coding

- **What we did:** Removed the erroneous prohibition on same-day Dpost and replaced calendar-day counting with elapsed 24-hour intervals. Defined `Dpre = 0` as onset after vaccination by less than 24 hours and `Dpost = 0` as vaccination after onset by less than 24 hours. Unknown within-day order remains unknown.
- **Command / executable:** Manual `apply_patch` edit; targeted Dpre/Dpost terminology scan and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.26.
- **Results:** Sub-day temporal proximity is preserved rather than discarded, including onset two hours after vaccination.
- **Next steps:** Use identical elapsed-time definitions and worked examples in the survey, codebook, validation tests, and SAP.
## 2026-08-13 — Resolved age boundary and seven-day window wording

- **What we did:** Corrected “withdrawn” to “withdraw,” defined every `_within_7d` field as Day 0 through Day 6 inclusive, and replaced the ambiguous 60-month/day cutoff with onset before the child's fifth birthday.
- **Command / executable:** Manual `apply_patch` edit; targeted terminology review and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.27.
- **Results:** The survey implementation no longer has an off-by-one ambiguity, and age eligibility no longer depends on a leap-year-sensitive universal day maximum.
- **Next steps:** Put the same definitions into the survey, codebook, validation tests, and analytic derivation specification.

## 2026-08-13 — Added required contact linkage and embedded record validation

- **What we did:** Redesigned the study from a directly unlinked exempt-survey concept to a coded minimal-risk parent survey requiring email, with a separately authorized, randomly selected record-validation substudy. Added segregated contact/research/validation stores, outcome-blinded random sampling, dual record abstraction and adjudication, a target of at least 100 completed vaccination-record comparisons if achievable, explicit validation-selection and missing-record reporting, separate survey and validation locks, withdrawal rules, expanded security controls, and corresponding IRB-packet punchlist items.
- **Command / executable:** Manual `apply_patch` edits; targeted obsolete-language and contradiction scans with `rg`; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.28.
- **Results:** The design can directly estimate agreement between parent-reported vaccination timing and obtainable documentary evidence instead of relying only on an unverifiable recall assumption. Because responses remain linkable and validation may involve identifiable child records, exemption is no longer the primary requested pathway; the packet will request the appropriate minimal-risk review with adult consent, parental permission, and record authorization as applicable.
- **Next steps:** Obtain IPAK-EDU feedback on the minimal-risk/Subpart D pathway; finalize the validation sampling and stopping plan, authorization form, abstraction manual, retention schedule, vendor architecture, and named validation personnel.

## 2026-08-13 — Adopted staged validation sample

- **What we did:** Replaced the aspirational 100-record validation target with a staged design: 20 usable vaccination-record comparisons as the minimum feasibility threshold and 60 as the operational target if obtainable. Required invitations to continue under outcome-independent stopping rules and prohibited a cohort-wide quantitative disagreement estimate if fewer than 20 usable comparisons are obtained.
- **Command / executable:** Manual `apply_patch` edit; targeted terminology scan; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.29.
- **Results:** The validation burden is reduced while preserving a credible precision target; stopping cannot depend on whether early comparisons agree with parent reports.
- **Next steps:** Prespecify invitation batches, expected authorization/retrieval rates, exact confidence intervals, and the final outcome-independent exhaustion rule in the validation manual and SAP.

## 2026-08-13 — Added onset-anchor controls and follow-up research roadmap

- **What we did:** Added a consent-safe clinic-branded Start page, an optional categorical decline-reason path subject to IRB approval, structured onset reconstruction and timing-anchor questions before vaccination items, vaccination-anchor measurement, onset-evidence tiers, primary blinded and secondary unblinded validation review, and prespecified measurement-quality sensitivity strata. Expanded the roadmap to include a separately approved random-sample nonresponder callback study, independent replication, a population-based record study, and prospective pediatric sentinel surveillance.
- **Command / executable:** Manual `apply_patch` edits; targeted terminology and consistency review; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.30.
- **Results:** The present study more directly measures recall quality and anchoring without adding unrestricted main-survey narratives or clinic callbacks to the current protocol. Later designs are clearly separated so they do not expand the present IRB submission or imply that validation eliminates selection bias.
- **Next steps:** Convert the new fields into exact parent-facing items; obtain IPAK approval for decline-reason retention; freeze evidence-tier, redaction, subgroup, and blinded/unblinded adjudication rules before outcome access.

## 2026-08-13 — Made the day-level measurement gap the scientific rationale

- **What we did:** Added a dedicated scientific-rationale section distinguishing broad vaccine/ASD research from the narrower SORA timing question. Documented the proposed combination of discrete Day 0, directional sub-24-hour/day-level intervals, exact-versus-ranged reporting, recall anchors, evidence tiers, blinded assessment, and random record validation. Explained why positive, null, or diffuse findings would add knowledge and reserved the absolute novelty claim pending a reproducible literature review.
- **Command / executable:** Targeted primary-literature search; manual `apply_patch` edit; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.31.
- **Results:** The summary now states a clear knowledge gap and proportional scientific justification for collecting the data without claiming that temporal proximity establishes causation.
- **Next steps:** Build the protocol literature table and reproducible search appendix and confirm the novelty language before formal IRB submission.

## 2026-08-13 — Added selection-bias framework and drafted complete parent survey

- **What we did:** Added a dedicated executive-summary section describing whole-population clinic distribution, funnel measurement, neutral ordering, causal-belief and vaccination-plan stratification, validation, and residual selection limitations. Added pre-survey causal-attribution and post-onset vaccination-decision domains. Created a complete electronic parent-survey draft with landing and consent gates, eligibility, broad developmental pattern, SORA Day 0/category rules, onset anchors, Dpre/Dpost, acute events, causal beliefs, subsequent vaccination decisions, review, limited branches, validation follow-up requirements, automated checks, paradata, and implementation punchlist.
- **Command / executable:** Manual `apply_patch` authoring; targeted cross-document terminology review; Markdown structure scan; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.32 and new `irb_submission/CHD_SORA_DATA_RESOURCE/02_Parent_Survey_Instrument.md` Version 0.1.
- **Results:** The study now measures prior causal attribution, vaccination anchoring, and continued/changed vaccination without treating those post-event variables as unbiased controls. The IRB has a concrete instrument to review rather than only a list of intended domains.
- **Next steps:** Conduct cognitive and timed usability testing; resolve the listed IRB/vendor/legal decisions; create the separate validation authorization and abstraction manual; freeze the machine-readable codebook and branching tests.

## 2026-08-13 — Added prespecified selection-bias interpretation

- **What we did:** Added the precise inferential statement governing comparisons across prior-attribution, onset-anchor, subsequent-vaccination, recall-source, and evidence-quality groups, including the limited inference from recipients who never select Start.
- **Command / executable:** Manual `apply_patch` edit; targeted wording check; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.33.
- **Results:** The summary now states that consistent subgroup timing would weaken explanations based solely on pre-existing vaccine attribution or differential reporting, while preserving the residual that unobserved nonresponder outcomes remain unknown.
- **Next steps:** Carry the same prespecified language into the protocol and SAP without strengthening it after outcome access.

## 2026-08-13 — Synchronized Google Docs executive summary

- **What we did:** Replaced the full body of the existing `CHD Executive Summary` Google Doc with local Executive Summary Version 0.33, reapplied title/heading and bullet structure, removed Markdown emphasis markers, corrected transferred punctuation encoding, and verified the version plus the new selection-bias, prespecified-interpretation, causal-attribution, and punchlist sections by connector readback.
- **Command / executable:** Google Drive/Docs authenticated metadata, full-text, and `batchUpdate` operations; local Markdown chunked read; post-write targeted readback.
- **Outputs:** Google Doc `1qhRWQAOWZXvrLvq_IXWlsUD9pdAdoYorDyulSGoH1I0` updated in place.
- **Results:** The Google Doc now contains the current Version 0.33 content instead of Version 0.20; the single-tab topology and document identity were preserved.
- **Next steps:** Treat the local Markdown as the authoritative working source and resynchronize the Google Doc after future approved version changes.

## 2026-08-13 — Locked the requested IRB review pathway

- **What we did:** Replaced generic minimal-risk language with a specific request for expedited IRB review under 45 CFR 46.110, proposed Category 7 for the survey and Category 5 for validation records, a 45 CFR 46.404 minimal-risk child finding, adult consent and parental permission, possible waiver of signed documentation under 45 CFR 46.117(c), and an assent determination under 45 CFR 46.408(a). Clarified that exemption is not the primary request and that record authorization is the default rather than a HIPAA waiver.
- **Command / executable:** Manual `apply_patch` edit; targeted regulatory-language scan; `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.34. The Google Doc remains at Version 0.33 and was intentionally not synchronized.
- **Results:** The review pathway is now a fixed design decision rather than a generic or ambiguous TBD, while preserving IPAK-EDU's authority to make the final category and Subpart D determinations.
- **Next steps:** Use the same requested-pathway language in the formal protocol, cover application, consent/permission materials, and validation authorization.

## 2026-08-13 — Added IPAK IRB website to executive summary

- **What we did:** Added the supplied IPAK Institutional Review Board website to the Reviewing IRB entry and incremented the Markdown executive summary from Version 0.34 to Version 0.35.
- **Command / executable:** Website verification followed by manual `apply_patch` edit and `git diff --check`.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/00_CHD_SORA_Study_Executive_Summary.md` Version 0.35.
- **Results:** The executive summary now provides a direct link to the identified reviewing IRB. The Google Doc was intentionally not changed.
- **Next steps:** Confirm the IRB's exact legal/operator name and submission details for punchlist item C2 before formal submission.

## 2026-08-13 — Completed IPAK Form 1 intake draft

- **What we did:** Filled the IPAK Form 1 content controls from Executive Summary Version 0.35 while preserving the source Word template. Populated the title, PI, provisional CHD affiliation, human-study type, study description, specific aims, proposed duration, participant population, funding/budget status, and repeated header fields. Marked unavailable contact, address, timing, legal-entity, and funding details as TBD or confirm.
- **Command / executable:** Task-local OOXML content-control patch; Microsoft Word PDF export; four-page raster inspection; package/control and section verification.
- **Outputs:** `irb_submission/CHD_SORA_DATA_RESOURCE/ipakirb-form-1_filled.docx`.
- **Results:** All 15 intended controls were populated; the original form remains unchanged. The four rendered pages were reviewed with no clipping or overlap in the completed intake form. The source template's contents page already contains broken bookmarks for absent Parts B and C; this pre-existing condition was preserved.
- **Next steps:** User/PI should replace every TBD or bracketed confirmation, confirm the proposed 12-month duration, and verify the funding/budget language before submission.

## 2026-08-18 — Reframed SORA timing hypothesis around two clocks

- **What we did:** Revised the v2 study overview and parent survey to compare chronological age at onset with time since the child's actual most recent pre-onset vaccination. Added birth date, sex recorded at birth, routine/early/delayed/catch-up visit timing, and source/confidence for the preceding vaccination date; retained post-onset schedule change only as a descriptive diagnostic.
- **Command / executable:** Manual `apply_patch` edits; targeted `rg` consistency scan; `git diff --check`.
- **Outputs:** `protocol/v2/SORA_study_v2.md` Version 2.2 and `protocol/v2/parent_survey_v2.md` Version 1.2.
- **Results:** The former interval-uniformity null was replaced by an age-anchored null versus vaccination-event-time alternative using actual vaccination dates. No post-onset vaccination identity or timing is collected for the primary comparison.
- **Next steps:** Specify the flexible age model, primary post-vaccination risk window, identifiability threshold for vaccination-age variation, missing-date rules, and record-verified sensitivity analysis in the statistical analysis plan before main-study enrollment.

## 2026-08-18 — Adopted three-prong SORA temporal analysis plan

- **What we did:** Replaced the model-based two-clock primary analysis with three prespecified components: non-overlapping three-day vaccination-relative lag histograms, parent-onset counts by chronological age, and a primary stratified permutation test of Day 0–2 synchronization. Updated the survey planning instrument to collect geography at onset and vaccination, retain the actual most recent pre-onset vaccination details, and remove the preceding-visit module.
- **Command / executable:** Manual `apply_patch` edits; targeted repository and consistency searches; `git diff --check`.
- **Outputs:** `protocol/v2/SORA_study_v2.md` Version 2.3 and `protocol/v2/parent_survey_v2.md` Version 1.3.
- **Results:** The planning documents now distinguish the two descriptive plots from the confirmatory permutation test, require parent-observed onset rather than diagnosis timing, and collect the fields needed for visit-, clinic-, schedule-, and geographic stratification without collecting post-onset vaccination timing.
- **Next steps:** Before REDCap implementation, freeze the permutation strata and sparse-stratum rules, exact-date eligibility, number of permutations, visit-category derivation, multiplicity plan, and public-versus-controlled geography fields.

## 2026-08-18 — Replaced Priority 1 with executable null-validation tasks

- **What we did:** Replaced the obsolete interval-uniformity punchlist item with sequential Items 1A--1E covering the synchronization estimand, candidate permutation procedures, simulation validation, frozen analysis specification, and survey-variable sufficiency.
- **Command / executable:** Manual `apply_patch` edit and `git diff --check`.
- **Outputs:** Updated `protocol/v2/study_punchlist.md`.
- **Results:** Priority 1 now has explicit completion criteria and must be closed before work begins on Priority 2.
- **Next steps:** Complete Item 1A by locking the primary estimand, Day 0--2 statistic, eligibility rules, exclusions, and interpretation boundary.

## 2026-08-18 — Added optional controlled secondary-research sharing

- **What we did:** Added an end-of-survey Yes/No permission for controlled sharing of coded records, including collected calendar dates, with separately approved IRB-reviewed or equivalent research projects. Added the controlled-reuse feature and governance conditions to the study overview.
- **Command / executable:** HHS/OHRP and HIPAA research guidance review; manual `apply_patch` edits; `git diff --check`.
- **Outputs:** `protocol/v2/SORA_study_v2.md` Version 2.4 and `protocol/v2/parent_survey_v2.md` Version 1.4.
- **Results:** Exact-date research reuse is limited to affirmatively consented records under project-specific access review and a data-use agreement; the public file continues to use protected relative timing, and declining does not affect primary-study participation or compensation.
- **Next steps:** Have the reviewing IRB/privacy counsel approve the final permission language, withdrawal model, retention period, data-access committee authority, minimum-necessary rules, and data-use agreement before deployment.

## 2026-08-19 — Made direct parent-reported interval primary

- **What we did:** Revised Method 3 so the parent's direct vaccination-to-onset interval supplies the primary Day 0--2 classification, while a separate-timing subset supports the candidate permutation analysis. Replaced vague confidence labels with maximum plausible error in days and separate evidence-source questions for onset, the reported interval, and vaccination date.
- **Command / executable:** Manual `apply_patch` edits; cross-document terminology scan; `git diff --check`.
- **Outputs:** `protocol/v2/SORA_study_v2.md` Version 2.5, `protocol/v2/parent_survey_v2.md` Version 1.5, and updated Priority Items 1A, 1E, and 2 in `protocol/v2/study_punchlist.md`.
- **Results:** Calendar vaccination dates are optional for the full-sample lag analysis but remain available for reconstruction, validation, chronological-age calculations, and permutation-subset eligibility. Confidence is now expressed as analyzable error bounds rather than qualitative labels.
- **Next steps:** Cognitively test whether parents understand maximum plausible error and plus-or-minus wording; complete Item 1A eligibility and contradiction rules, then validate candidate permutation procedures under Item 1C.

## 2026-08-20 — Added schedule-spaced lag rationale and Day 90 contrast

- **What we did:** Extended the required three-day vaccination-to-onset lag histogram through Day 179 and added a prespecified secondary Day 0--2 versus Day 90--92 count contrast calibrated by the same permutation null. Added the rationale that an age-driven 18-month onset peak can generate both near-zero and approximately 90-day lags depending on whether the last vaccination occurred near 18 or 15 months.
- **Command / executable:** Manual `apply_patch` edits; targeted consistency scan; `git diff --check`.
- **Outputs:** `protocol/v2/SORA_study_v2.md` Version 2.6 and updated Priority Items 1A and 1D in `protocol/v2/study_punchlist.md`.
- **Results:** The protocol no longer hides longer schedule-spaced peaks or assumes Day 0 and Day 90 counts must be equal; their expected difference will be generated empirically by the validated permutation procedure.
- **Next steps:** Include the Day 0--2 and Day 90--92 counts and contrast in the null simulations, then freeze their eligibility and multiplicity treatment under Items 1C and 1D.
## 2026-08-20 — Squarespace screening/research prototype

- **What we did:** Created a one-page HTML prototype that scores 20 M-CHAT-R responses locally and allow-lists only four consented research variables for transmission.
- **Command / executable:** Open `protocol/v2/sora_mchat_squarespace_prototype.html` in a browser; configure its `data-endpoint` before deployment.
- **Outputs:** `protocol/v2/sora_mchat_squarespace_prototype.html`.
- **Results:** The prototype separates browser-only screening answers from the research payload, displays the screening result after submission, and retains placeholder item text pending M-CHAT-R permission.
- **Next steps:** After written permission, insert the exact authorized instrument text and copyright notice; connect and test the approved collection endpoint and verify its CSV field output before public use.

## 2026-08-26 — v4_SPARK: simple survey package modeled on the Airtable SOA form

- **What we did:** Built a SPARK Research Match version of the public Airtable "Parent Survey on Sudden-Onset Autism" — same core items and interval codes, with a neutral intro, a `change_type` gate that routes gradual-onset families into a comparison arm, attribution/hypothesis-exposure moved after all timing items, pediatrician visit split into with/without shots plus a `visit_novax_interval` mirror of `vax_interval`, and `date_evidence`/`record_upload_ok` stratifiers.
- **Outputs:** `protocol/v4_SPARK/spark_parent_survey_v1.md`, `spark_survey_redcap_dictionary.csv` (32 fields; generated by `make_dictionary.py`), `spark_signal_analysis_plan.md`, `spark_signal_analysis.py`, `spark_research_match_application.md`.
- **Results:** Analysis script validated on synthetic data: recovers injected Day 0–2 RR≈3 (p=0.01, n≈150 confirmatory) and returns RR≈1 on null and on the non-vaccinating-visit control.
- **Next steps:** Name an institutional PI (needed for SFARI Base / RDA / IRB); confirm with SPARK whether the survey is hosted on their platform or REDCap; decide the coarsened public-file terms; pre-register plan on OSF; submit to the Participant Access Committee (next deadline Sep 30).

## 2026-08-30 — Reviewed prediction specification against n=270 export

- **What we did:** Compared `prespecified_predictions.md` with the latest 270-row SOA2 grid export, checked field-adoption counts and lag labels, and reviewed whether the three hypotheses and decision rules identify the claimed mechanisms.
- **Command / executable:** Read-only pandas/scipy summaries of `C:\Users\stk\Downloads\SOA2-Grid view.csv`; manual specification review.
- **Outputs:** `protocol/v4_SPARK/predictions_specification_review_n270.md`.
- **Results:** The data show reported early-lag clustering and day-5/day-7 heaping, but the authoritative vaccine-type field has only one response, so the primary SHOT/NOSHOT contrast is not yet testable. The hypothesis table is too mutually exclusive for mechanisms that can coexist, and rejecting its flat/perfect-recall null does not identify vaccination. H-vax already applies only to a subgroup; non-vaccine biological triggers should be specified as a separate prospective mechanism rather than treated as a refutation.
- **Next steps:** Preserve the original prediction file; label any revisions post-n=270, align lag bins to planned windows, freeze exposure and narrative-coding rules, add structured non-vaccine acute-exposure definitions if those predictions will be tested, and confirm on a held-out later tranche or neutral recruitment channel.

## 2026-08-30 — Versioned predictions and drafted prospective v2

- **What we did:** Archived the amended three-hypothesis table as v1 and drafted v2 around a prespecified statistical SHOT-versus-certain-NOSHOT early-window contrast.
- **Command / executable:** Manual `apply_patch`; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v1.md` and `protocol/v4_SPARK/prespecified_predictions_v2.md`.
- **Results:** V2 reserves Airtable records 46–318 as exploratory, begins prospective confirmation at record 319, defines early as same-day-after through day 5 and reference as days 6–59, requires a significant SHOT/NOSHOT difference with confidence intervals and minimum valid group sizes, and explicitly shows why 95% early pooled or 95% in both groups does not support a vaccine-specific association.
- **Next steps:** Review and revise the v2 draft before freezing its hash; ensure the live form keeps authoritative certain-NOSHOT status and exactly recoverable lag bins; do not use the n=270 cohort to confirm v2 predictions.

## 2026-08-30 — Replaced infeasible no-shot primary test with verified SCCS v3

- **What we did:** Marked v2 superseded and drafted v3 around complete verified vaccination histories, independently supported PARENT onset dates, exact exposure-opportunity denominators, and a self-controlled case-series model.
- **Command / executable:** Manual `apply_patch`; targeted terminology scan; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v3.md`; status update in `prespecified_predictions_v2.md`.
- **Results:** The primary null now predicts event counts proportional to adjusted eligible person-time; the vaccine-associated alternative predicts an IRR above 1 in days 0–5. Certain-NOSHOT visits and raw-recall diagnostics are secondary, not required gates. V3 explicitly requires complete histories and an event-dependent-exposure method, so the current last-visit-only raw export cannot supply a confirmatory SCCS result.
- **Next steps:** Select and cite the event-dependent SCCS implementation, freeze risk/washout windows and age/calendar adjustment, implement simulations, finalize verification/adjudication rules, and hash the plan before linking confirmatory onset outcomes to vaccine dates.

## 2026-08-30 — Drafted verified-survey primary lag test as v4

- **What we did:** Marked v3 superseded as the primary plan and translated the proposed seven survey predictions into an analysis of respondent-verified and document-verified survey fields.
- **Command / executable:** Manual `apply_patch`; targeted denominator scan; `git diff --check`; primary-method literature check.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v4.md`; status update in `prespecified_predictions_v3.md`.
- **Results:** V4 makes the exactly recoverable days 0–5 versus days 6–59 comparison primary, with a 1:9 count null, per-day RR, exact binomial test, and age/schedule-stratified permutation robustness test. No-shot visits and full-history SCCS are secondary. The remaining year, weekday/day, and age-shape predictions are operationalized but correctly labeled diagnostic where they do not identify vaccine timing.
- **Next steps:** Finalize the verification readback, approve or replace the draft RR=2 no-material-effect margin, operationalize age-shape tolerances, freeze the permutation algorithm, simulate calibration/power/selection scenarios, and hash v4 before confirmatory analysis.

## 2026-08-30 — Fixed RR=2 and randomization procedure in v5

- **What we did:** Marked v4 superseded and drafted v5 with a fixed material-effect threshold, exact primary test, reproducible Monte Carlo randomization check, and survey-supported age-alignment sensitivities.
- **Command / executable:** Manual `apply_patch`; targeted denominator/procedure scan; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v5.md`; status update in `prespecified_predictions_v4.md`.
- **Results:** MV requires verified per-day RR ≥2, p<0.05, and a CI excluding 1; M0 against a material effect requires the upper CI below 2. The fixed Monte Carlo procedure uses 100,000 uniform 0–59 lag assignments with seed 20260830 and must reproduce the exact binomial p-value. V5 explains that 60-day shot spacing avoids overlap but does not prove flatness when onset and vaccination are both age-structured.
- **Next steps:** Freeze the verification protocol and age-shape rules, implement exact/Monte Carlo tests, simulate flat/RR/age-alignment/selection cases, and hash the final version before confirmatory analysis.

## 2026-08-30 — Applied v5 exploratory test to latest n=270 raw export

- **What we did:** Applied the exact v5 0–5 versus 6–59 test without Monte Carlo to the latest Downloads export, both strictly using the new authoritative field and exploratorily using the older vaccination-checklist proxy; ran the prespecified age sensitivities.
- **Command / executable:** Read-only pandas/scipy analysis of `C:\Users\stk\Downloads\SOA2-Grid view.csv` (SHA-256 `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`).
- **Outputs:** `protocol/v4_SPARK/predictions_v5_exploratory_application_n270.md`.
- **Results:** The authoritative field has only one raw eligible row and is undecidable. The older checklist proxy gives E=36, R=8, N=44, early fraction 81.8%, per-day RR=40.5 (exact 95% CI 18.5–100.9), one-sided p=7.82e-29. Excluding onset ages 17–19 gives E=30, R=6, RR=45.0. Results are an extreme exploratory signal but cannot meet v5 confirmation without verification.
- **Next steps:** Freeze and conduct the respondent verification readback, obtain document verification where possible, preserve corrections, and rerun the identical exact test by verification tier; Monte Carlo is optional code validation.

## 2026-08-30 — Clarified the v5 vaccination-at-visit field

- **What we did:** Corrected the v5 application report and specification to use the existing `What happened?` → `Vaccination(s)` field for binary vaccination-at-visit status rather than treating it as a proxy for the later vaccine-type field.
- **Command / executable:** Manual `apply_patch`; no recalculation required.
- **Outputs:** Updated `protocol/v4_SPARK/prespecified_predictions_v5.md` and `predictions_v5_exploratory_application_n270.md`.
- **Results:** The reported E=36, R=8, RR=40.5 result already used the correct existing vaccination field. The limitation is lack of verification readback/document replication, not absence of an authoritative binary vaccination field.
- **Next steps:** Verify the existing field during recontact and rerun the unchanged v5 exact analysis.

## 2026-08-30 — Scored v5 matrix under assumed verification

- **What we did:** Created a Yes/No/Indeterminate H-null versus H-vax matrix for P1–P7 and, at the user's instruction, rescored the overall result assuming every retained survey value is verified and correct.
- **Command / executable:** Exact/descriptive summaries of the unchanged n=270 Downloads export; manual matrix drafting.
- **Outputs:** `protocol/v4_SPARK/predictions_v5_results_matrix_n270.md`.
- **Results:** Under the counterfactual verified-data assumption, H-null=No and H-vax=Yes overall. P7 is decisive: E=36, R=8, RR=40.5 (95% CI 18.5–100.9), p=7.82e-29, versus null expected counts approximately 4.4 and 39.6. P1 and P6 remain structurally indeterminate; several secondary rows are non-discriminating.
- **Next steps:** Keep the assumed-verification label distinct from actual verification status; operationalize P6 symmetry before using it in a real frozen analysis.

## 2026-08-30 — Corrected v5 prediction hierarchy

- **What we did:** Corrected §7 so P1–P7 are identified as the seven core prespecified predictions rather than being grouped under “Secondary predictions.”
- **Command / executable:** Manual `apply_patch`.
- **Outputs:** Updated `protocol/v4_SPARK/prespecified_predictions_v5.md` and `predictions_v5_results_matrix_n270.md`.
- **Results:** P7 is now explicitly the primary statistical decision test; P1–P6 are core supporting predictions that must all be reported and can strengthen, weaken, or qualify P7.
- **Next steps:** Preserve this hierarchy in the frozen version and analysis output.

## 2026-08-30 — Created v6 with explicit predictions for every P1–P7 test

- **What we did:** Marked v5 superseded and created one authoritative table stating the H-null prediction, H-vax prediction, statistic/decision rule, and role for every P1–P7 row.
- **Command / executable:** Manual `apply_patch`; targeted P1–P7 scan; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v6.md`.
- **Results:** P7 now explicitly contrasts null E/R=1/9 and RR=1 with H-vax RR≥2. P1–P3 contain exposure-specific calendar predictions; P4 is identified as potentially non-discriminating; P5 has fixed adjacent-month ratios; and P6 has a draft ±6-month, 20% asymmetry statistic.
- **Next steps:** Review the substantive validity of each H-vax prediction—especially the P2/P3 visit-calendar direction and P6 threshold—then simulate and freeze v6 prospectively.

## 2026-08-30 — Created mutually exclusive v7 predictions and matrix

- **What we did:** Replaced overlapping H-null/H-vax cells with mutually exclusive null, vaccine, and indeterminate regions for every P1–P7 test; redesigned P4 as a VAX-versus-NEVER modal-age comparison.
- **Command / executable:** Manual `apply_patch`; mutual-exclusivity scan; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v7.md` and `predictions_v7_results_matrix_n270.md`; v6 marked superseded.
- **Results:** Only `(Yes, No)`, `(No, Yes)`, and `(Indeterminate, Indeterminate)` are allowed. Under assumed verification, P1–P6 are indeterminate because NEVER/named-day cells are inadequate or the calendar model is unfrozen; P7 is `(No, Yes)` with RR=40.5 and the overall exercise conclusion is H-null=No, H-vax=Yes.
- **Next steps:** Approve or replace draft P1–P6 equivalence/effect margins, freeze the P2/P3 calendar model, simulate operating characteristics, and implement a state-pair validator before freezing v7.

## 2026-08-30 — Applied final paired v7 rules to n=270 assumed-verified data

- **What we did:** Reapplied P1–P7 after consolidating affirmative vaccination evidence for VAX and retaining the paired Yes/No, No/Yes, or Indeterminate/Indeterminate rule.
- **Command / executable:** Read-only pandas/scipy summaries of the latest 270-row Downloads export; manual results-matrix update.
- **Outputs:** Updated `protocol/v4_SPARK/predictions_v7_results_matrix_n270.md`.
- **Results:** VAX=185, NEVER=3, unknown=82. P1 shows the visible 2019/2020/2021 dip (all: 5/1/10; VAX: 5/1/5) but remains formally indeterminate because only 2 NEVER records are dated. P2 and age-shape P4–P6 point descriptively in the H-vax direction but are also comparator-limited. P7 remains No/Yes: E=36, R=8, RR=40.5, p=7.82e-29. Overall assumed-verification result is H-null=No, H-vax=Yes.
- **Next steps:** Obtain enough NEVER observations for P1–P6 comparisons; finalize draft margins and calendar model before freezing v7.
## 2026-08-30 — Replace comparator-dependent v7 with pooled v8 predictions

- **What we did:** Audited v7, confirmed that it explicitly reintroduced VAX-versus-NEVER interactions into P1–P6, marked v7 superseded, and drafted v8 without those comparisons. Reorganized v8 so each prediction, measurement, window, statistic, cutoff, and paired decision rule is explained in plain English before the summary table.
- **Command / executable:** Manual Markdown review and `apply_patch`; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v8.md`; status correction in `protocol/v4_SPARK/prespecified_predictions_v7.md`.
- **Results:** P1–P6 now use the pooled eligible verified survey records. P7 alone uses confirmed vaccination-at-last-visit records. Every row retains only Yes/No, No/Yes, or Indeterminate/Indeterminate scoring.
- **Next steps:** Approve or revise the draft P1–P6 thresholds and freeze their interval/bootstrap procedures before treating v8 as confirmatory; then apply the frozen v8 rules to the n=270 export.

## 2026-08-30 — Simplify v9 to one mutually exclusive result

- **What we did:** Marked v8 superseded and created v9 with one result per prediction instead of redundant H-null and H-vax result columns.
- **Command / executable:** Version copy followed by manual `apply_patch`; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v9.md`; status correction in `prespecified_predictions_v8.md`.
- **Results:** Each row can now be only `Null`, `Vaccine`, or `Indeterminate`. Separate Null and Vaccine decision regions remain explicit, preventing a mere failure of the null rule from being treated automatically as vaccine evidence.
- **Next steps:** Approve or revise the draft P1–P6 thresholds and freeze their interval procedures before applying v9 to the n=270 export.

## 2026-08-30 — Apply v9 to the n=270 assumed-verified export

- **What we did:** Applied the single-state v9 rules to the unchanged latest Downloads export without a VAX-versus-NEVER comparison.
- **Command / executable:** Read-only pandas/scipy summaries; SHA-256 verification; manual `apply_patch` of the results table.
- **Outputs:** `protocol/v4_SPARK/predictions_v9_results_matrix_n270.md`.
- **Results:** Vaccine: P1, P2, P7. Null: none. Indeterminate: P3–P6. P4–P6 have Vaccine-region point estimates but remain formally indeterminate because v9 requires still-unfrozen bootstrap/directional procedures. The v9 overall exercise result is Vaccine favored because primary P7 is Vaccine ($E=36$, $R=8$, $RR=40.5$, $p=7.82e-29$).
- **Next steps:** Freeze P3's simultaneous procedure and P4–P6 bootstrap/direction rules, then rerun those four classifications without changing their thresholds in response to the results.

## 2026-08-30 — Require separate VAX and NEVER tables in v10

- **What we did:** Marked v9 superseded and created v10 requiring two independently scored tables for every dataset, without restoring a mandatory VAX-minus-NEVER interaction test.
- **Command / executable:** Version copy followed by manual `apply_patch`; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/prespecified_predictions_v10.md`; status correction in `prespecified_predictions_v9.md`.
- **Results:** The prespecified fair-test direction is VAX rows only Vaccine/Indeterminate, with VAX P7 Vaccine, and NEVER rows only Null/Indeterminate. A Vaccine-pattern result in NEVER is explicitly a specificity contradiction, not evidence that a vaccine caused an unvaccinated case. NEVER P7 is a negative-control analysis after verified non-vaccination wellness visits.
- **Next steps:** Apply both v10 tables to the current export, while reporting that the current NEVER group is extremely sparse and therefore likely indeterminate.

## 2026-08-30 — Correct invalid no-vaccine-visit remainder

- **What we did:** Audited the proposed subtraction of vaccination visits from all visit-relative records and rejected it because blank/unknown `What happened?` responses had been implicitly treated as no vaccination.
- **Command / executable:** Read-only row-level PowerShell review of nonblank `What happened?` values without `Vaccination(s)`; `apply_patch` correction to the v9 result note.
- **Outputs:** Corrected `protocol/v4_SPARK/predictions_v9_results_matrix_n270.md`.
- **Results:** Of 17 nonblank rows lacking `Vaccination(s)`, 10 say `Don't remember what happened`. Only three detailed apparent non-vaccination visits have usable P7-window lags; E=0 and R=3. The earlier 89/54 subtraction is invalid and must not be described as a verified no-vaccine control.
- **Next steps:** Preserve unknown as unknown. Use only affirmatively verified no-vaccination visits in the v10 negative-control table and score the current sparse cell Indeterminate.

## 2026-08-30 — Updated v10 tables for 289 responses

- **What we did:** Read the 13:10:55 Downloads export, audited the 19 additional IDs 319–337, and calculated separate VAX and NEVER tables under the continuing assumed-verification exercise. Kept missing vaccination status and visit contents unknown.
- **Command / executable:** Read-only PowerShell CSV/hash checks and inline Python CSV/SciPy exact-binomial summaries. Bundled Python lacked SciPy; used installed system Python for the statistical calculations. Manual `apply_patch` results report; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/predictions_v10_results_matrix_n289.md`. Input SHA-256 `c3d8c507dbd3bc1dbffd3ec796a4907f3b06e268306b581eb7ccc6eacf40e01b`.
- **Results:** VAX=204, NEVER=3, unknown=82. VAX P2/P7 meet Vaccine criteria; other VAX rows and every NEVER row are Indeterminate. P7 combined E=43/R=12, RR=32.25 (95% exact interval 16.71–67.18), p=1.278e-32; additional batch alone E=7/R=4, RR=15.75, p=2.290e-5. VAX P1 now 5/2/5, p=0.1811; earlier pooled P1 must not be substituted into the VAX table.
- **Next steps:** Complete the unresolved v10 statistical procedures before prospective use; obtain adequately informative NEVER/no-shot controls and actual record verification. The current signal is conditional on the flat-lag model and does not establish VAX/NEVER specificity.

## 2026-08-30 — Check 14:58 export, 303 responses

- **What we did:** Audited unchanged CSV columns and 14 additional IDs 338–351; recalculated the two v10 tables with the existing mappings and assumed-verification exercise.
- **Command / executable:** Read-only PowerShell and inline Python CSV/SciPy exact-binomial summaries; `apply_patch` report and log; `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/predictions_v10_results_matrix_n303.md`; input hash `4d7288a6f591330cb26f73838768b4c45f0e20d8464ced54c5d96f7b025679a6`.
- **Results:** VAX=217, NEVER=4, unknown=82. Combined P7 E=50/R=13, RR=34.62, exact interval 18.53–69.46, p=2.738e-38. New batch E=7/R=1. P2/P7 remain Vaccine; other VAX rows and all NEVER rows Indeterminate. No broad developmental-trajectory field yet.
- **Next steps:** Correct #350's invalid onset year (excluded from year analysis without changing source); clarify #349's vaccination-at-visit omission versus recent vaccination before classifying that visit. Do not turn missing checklist selections into confirmed no-shot visits.

## 2026-08-30 — Onset-age histogram with CDC reference, n=322

- **What we did:** Plotted monthly parent-onset ages from the 21:20 export and aligned selected CDC 2025 routine-dose age ranges beneath the histogram. Checked USA/VAX-only peak counts and preserved older ages in a separate panel.
- **Command / executable:** `python outputs/onset_age_n322/plot_onset_age.py`; matplotlib PNG visual inspection; CDC schedule-note lookup; `git diff --check`. Bundled Python lacked matplotlib, so installed system Python was used.
- **Outputs:** `outputs/onset_age_n322/onset_age_cdc_reference.png`, `summary.json`, `findings.md`, and `docs/executables.md`.
- **Results:** 322 rows; 321 plotted after excluding #84's implausible 2,212 months without correction. Highest counts: 18 months=47, 15=31, 12=24, 24=20. Top three peaks remain in USA/VAX subset (33/22/17). Partial descriptive overlap with CDC ranges, not a schedule-alignment significance test or causal finding.
- **Next steps:** Verify #84's onset age and actual vaccination dates; match historical/geographic schedules before formal schedule-alignment analysis.

## 2026-08-30 — Monthly 2–20-month histogram zoom

- **What we did:** Confirmed unchanged 322-row input hash and plotted the requested crop with one-month bins; compared 2/4/6/12/15/18-month counts against both immediately adjacent months.
- **Command / executable:** `python outputs/onset_age_n322/plot_onset_age_zoom.py`; PNG visual inspection.
- **Outputs:** `outputs/onset_age_n322/onset_age_2_to_20.png`.
- **Results:** 232 reports in the cropped view. Local peaks at 6, 12, 15, and 18 months, but not at 2 or 4. The infant local peak is 3 months (14 reports), versus 2 months (10) and 4 months (8). Comparisons are descriptive, not significance tests.
- **Next steps:** Use actual exposure dates and age-precision information for a formal timing test rather than equating reference ages with observed vaccinations.

## 2026-08-30 — General autism intake banner

- **What we did:** Generated a replacement text-free parent-and-child cover for the broadened Parent Survey of Autism and Early Development, with navy/teal styling and no sudden-onset or vaccine imagery.
- **Command / executable:** Built-in image generation, visual review, workspace copy; generation prompt retained beside asset.
- **Outputs:** `outputs/autism_intake_banner/parent_autism_early_development_v1.png` and `generation_notes.md`.
- **Results:** New image ready for manual upload. Existing source artwork and live Airtable form are unchanged.
- **Next steps:** Upload the image and adjust the Airtable cover crop to keep faces visible; retain the survey title as native text below the cover.

## 2026-08-31 — Existing-study dataset add-on request v2

- **What we did:** Preserved the existing generic data request and created v2 with explicit available-data scope, no case floor, optional documented vaccination-deferral details, and clarified visit/vaccination timing. Kept it separate from the survey/v10 protocol.
- **Command / executable:** Targeted document read, `apply_patch`, and `git diff --check`.
- **Outputs:** `protocol/generic/autism_study_data_requests_v2.md`.
- **Results:** Request retains four figure types, explicit unknown categories, comparison within visit type, and optional source-population aggregates. No mandated new primary analysis or predetermined result. Source request unchanged.
- **Next steps:** Review/send the v2 request to the existing-study investigators; report unavailable fields and sparse cells transparently.

## 2026-08-31 — Read-only review of hand-edited dataset request v2

- **What we did:** Read both generic request files and reviewed the hand-edited v2 without changing either document.
- **Command / executable:** PowerShell document read and targeted line-number scan.
- **Outputs:** Review feedback only; this work-log entry.
- **Results:** Main remaining ambiguity is selecting a pre-onset encounter while also requesting same-day encounters after onset. Minor wording issues: `noted` versus `first noticed`, and equating existing retrospective data with post-hoc analysis. These are refinements to the inherited draft, not evidence that the user's edits broke it.
- **Next steps:** Clarify encounter selection and analysis-timing wording before external use; optional removal of internal survey/protocol reference.

## 2026-08-31 — Apply approved dataset-request refinements

- **What we did:** Applied the four approved review fixes in v3, preserving the hand-edited v2 under the repository versioning rule.
- **Command / executable:** Targeted document reads, `apply_patch`, and `git diff --check`.
- **Outputs:** `protocol/generic/autism_study_data_requests_v3.md`.
- **Results:** Clarified preceding-encounter selection, same-day ordering and figure counts; changed onset to first noticed; clarified disclosure of analysis timing; removed the internal survey-reference sentence. No new sample-size floor or required primary analysis.
- **Next steps:** Use v3 for the external data request.

## 2026-08-31 — Dataset request v4: regression denominators

- **What we did:** Created v4 with available source-population, assessed-child, qualifying-regression, exact-day, and document-supported-day counts; preserved v3.
- **Command / executable:** Targeted reads, `apply_patch`, and diff verification.
- **Outputs:** `protocol/generic/autism_study_data_requests_v4.md`.
- **Results:** Added a participant-flow table and explicit percentage denominators; separated regression eligibility from date precision, nonresponse from absence, and child counts from parent counts. No new sample-size floor or requirement to collect unavailable data.
- **Next steps:** Use v4 for the external data request.

## 2026-08-31 — Dataset request v5: date-precision comparison

- **What we did:** Added the agreed available-data comparison of vaccination-before-onset and recent pediatric visits between exact-day and non-exact-day regression cases; preserved v4.
- **Command / executable:** Targeted reads, `apply_patch`, and diff verification.
- **Outputs:** `protocol/generic/autism_study_data_requests_v5.md`.
- **Results:** Explicit unknown/uncertain categories prevent unsupported classification from imprecise onset dates. All other request content retained.
- **Next steps:** Agreed drafting complete; use v5 for the external data request.

## 2026-09-01 — Latest Airtable survey export quality-control review

- **What we did:** Read-only review of the newest Downloads export for hostile notes, duplicate/rapid submissions, repeated emails, internal contradictions, implausible dates/ages, and public-note privacy risks.
- **Command / executable:** Python standard-library CSV scans and targeted record comparisons; no source records changed.
- **Outputs:** Review findings only; source `C:\Users\stk\Downloads\SOA2-Grid view.csv` (377 rows; SHA-256 `79F1A4515DE95228E8F43E54C9BDA084604F7AE028150B380122C888094469C4`).
- **Results:** No explicit trolling text or exact duplicate row found. Records 162/172 are a likely duplicate of the same child. Several same-email groups appear to contain multiple children, especially 264–267. Records 84, 342, 361, and 381 contain strong numeric/date errors; 353, 368, and 393 conflict on never-vaccinated status. Public Notes contain contact/identity risks in records 116, 132, 141, 400, and 420. Records 408–410 form a weak no-email time cluster but differ materially and are not evidence of fraud by themselves.
- **Next steps:** Quarantine—not delete—likely duplicate 172 pending confirmation; contact respondents where possible to correct errors/conflicts; decide a documented family-cluster rule; redact public identifiers from Notes; retain an auditable QC flag column.

## 2026-09-02 — U.S. autism prevalence and vaccine-schedule trend visualization

- **What we did:** Built a two-panel in-conversation chart of CDC ADDM identified autism prevalence and a derived count of distinct routine vaccine series recommended by age 24 months.
- **Command / executable:** CDC web-source review, targeted HTML/D3 authoring with `apply_patch`, and visualization render validation.
- **Outputs:** `C:\Users\stk\.codex\visualizations\2026\08\30\01a05316-48ad-73c0-b511-357ba360e101\us-autism-vaccine-schedule-trends.html`.
- **Results:** Autism panel uses the official 2000–2022 ADDM values. Schedule panel counts vaccine series rather than doses or antigens and excludes maternal, risk-based, catch-up, and repeat annual recommendations; it is descriptive and not a causal comparison.
- **Next steps:** If used publicly, independently audit each historical schedule milestone and retain the metric definition and ascertainment caveat in the caption.

## 2026-09-02 — Updated Airtable export response review

- **What we did:** Read-only review of the newest Downloads export for response counts, adoption of the new intake funnel, onset/visit timing, vaccination-field completeness, documentation availability, and rapid-submission similarity.
- **Command / executable:** PowerShell `Import-Csv` summaries plus a Python standard-library CSV consistency scan; no source records changed.
- **Outputs:** Findings only; source `C:\Users\stk\Downloads\SOA2-Grid view.csv` (391 rows; three already marked `Gamed`).
- **Results:** Of 388 unflagged rows, 27 contain the new developmental-pattern field and two enter the abrupt/dateable branch. The newly added `vax given?` column is still blank in this export, so its live capture is not yet empirically verified. Among older classified vaccination records with known 0–59-day visit timing, 79 fall at days 0–5 and 26 at days 6–59; only three confirmed-NOSHOT records populate those two windows. No high-similarity pair was found among no-email submissions made within five minutes after excluding flagged rows.
- **Next steps:** Confirm the next abrupt/dateable submission populates `vax given?`; continue reporting VAX timing descriptively while treating the NOSHOT comparison and new funnel proportions as immature.

## 2026-09-03 — Refresh live Airtable survey transcription

- **What we did:** Read the live Airtable form, exercised its developmental-pattern, regression-speed, and vaccine-confirmation branches without submitting, counted all respondent-facing questions, and replaced the outdated sudden-onset-only Markdown transcription.
- **Command / executable:** Read-only Chrome form inspection, targeted `apply_patch`, question-heading count, and `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/airtable_form_current.md` updated to v3.0 (live).
- **Results:** Verified 29 distinct questions; ordinary path 13, mixed or slow/uncertain regression path 14, abrupt/dateable regression path 28 without the vaccine-product checklist and 29 with it. Documented one live inconsistency: the checklist shown after a confirmed `Yes` still offers contradictory no-vaccine/unknown-vaccine options.
- **Next steps:** Remove the two contradictory options from the conditional vaccine-product checklist, then verify the branch again.

## 2026-09-03 — Verify corrected vaccine-product branch

- **What we did:** Rechecked the live abrupt/dateable regression path after the Airtable correction and updated the live Markdown transcription.
- **Command / executable:** Read-only Chrome branch inspection, targeted `apply_patch`, question-count check, and `git diff --check`.
- **Outputs:** `protocol/v4_SPARK/airtable_form_current.md` updated to v3.1 (live).
- **Results:** The required `Yes` / confirmed `No` / `I don't remember` confirmation remains. The `Yes` branch now lists vaccine products plus `Vaccines were given, but I don't remember which ones`; the two contradictory no-vaccine/unknown-vaccine product-list choices are gone. Total remains 29 distinct questions.
- **Next steps:** No form correction required for this branch.
# Work log

## 2026-09-04 — Regenerated live Airtable form transcription

- **What we did:** Re-read the published Airtable survey across its ordinary, sudden-onset, no-prior-visit, prior-visit, and vaccine-product branches; regenerated `protocol/v4_SPARK/airtable_form_current.md` as v3.2.
- **Command / executable:** Live browser inspection plus `apply_patch` and `git diff`.
- **Outputs:** `protocol/v4_SPARK/airtable_form_current.md`.
- **Results:** Documented 30 distinct questions, added genetic testing, updated current email and well-child wording, corrected branch counts, and recorded that the published form still excludes `Mixed` plus rapid/dateable regression despite the editor configuration screenshot.
- **Next steps:** Re-save/publish the section visibility rule and re-test `Mixed` plus rapid/dateable regression; then update the branching note if the published behavior changes.

## 2026-09-04 — Latest public export 0–5 versus 6–89 timing statistic

- **What we did:** Analyzed the newest public export, `C:\Users\stk\Downloads\SOA2-Public view.csv` (408 rows), using the post-well-child-visit interval field.
- **Command / executable:** PowerShell `Import-Csv` for field/value auditing and Python/Scipy for the conditional-binomial tail and rate-ratio confidence interval.
- **Outputs:** No new artifact; read-only calculation.
- **Results:** Excluding same-day-before-visit, blank, unknown, no-prior-visit, and post-day-89 responses, days 0–5 contained 171 reports and days 6–89 contained 95. The per-day rate ratio was 25.20 (95% log-rate CI 19.61–32.38); exact one-sided conditional-binomial p = 1.15e-130. The export's `90 to 120` bin prevents isolating day 90 exactly.
- **Next steps:** If exact 6–90 reporting is required, split day 90 from the 90–120 response bin in future exports or report the clean prespecified 6–89 comparison.

## 2026-09-04 — Parent autism survey promotional graphic

- **What we did:** Generated a broad, cause-neutral promotional graphic inviting parents of autistic children under age 20 with all developmental histories.
- **Command / executable:** Built-in image generation.
- **Outputs:** `outputs/autism_intake_banner/autism-parent-survey-promo-v1.png`.
- **Results:** Created a wide social-media graphic with exact survey invitation copy, inclusive parent-child artwork, and no vaccine or sudden-onset framing.
- **Next steps:** Add the live survey URL or a QR code in the publishing platform when deploying the graphic.
