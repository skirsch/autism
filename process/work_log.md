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

## 2026-09-25 — Reorganized v5 two-survey study overview

- **What we did:** Rewrote the v5 overview around a large membership-organization neutral intake, two-survey sequence, exposure-blind records selection, unprompted recall, and records validation.
- **Command / executable:** Manual Markdown revision with `apply_patch`; `rg` consistency checks and `git diff --check`.
- **Outputs:** `protocol/v5/study_overview.md` version 1.0 draft.
- **Results:** Established a firm goal of 100 usable records, retained 20 only as an interim feasibility checkpoint, stated that vaccination information cannot drive records selection, and clarified that submitted data have no revocation right while coded analytic data may be retained indefinitely. The conflicting 12-month and 18-month source-record destruction periods remain an explicit decision.
- **Next steps:** Resolve the listed design and operational decisions, beginning with the source-record destruction period and exact Survey 1-to-Survey 2 eligibility rule; then draft the two instruments.

## 2026-09-25 — Fixed v5 source-material retention period

- **What we did:** Resolved the conflicting 12-month and 18-month periods for original submitted records.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Original source materials will be securely destroyed 18 months after receipt unless the IRB or applicable law requires longer retention; coded analytic data may be retained indefinitely.
- **Next steps:** Resolve the Survey 2 invitation rule.

## 2026-09-25 — Fixed phased Survey 2 invitation strategy

- **What we did:** Defined staged Survey 2 invitations based on Survey 1 confidence that relevant records are available.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** The highest-confidence eligible group is invited first; successively lower-confidence groups are opened if fewer than 100 usable record sets have been obtained. Wave assignment and expansion cannot depend on vaccination information or interim timing results. Qualifying records received beyond 100 from an already-open wave are retained rather than discarded.
- **Next steps:** Fix the qualifying rapid-regression phenotype and the precise Survey 1 confidence categories.

## 2026-09-25 — Revised v5 eligibility and wave-assignment rule

- **What we did:** Removed the seven-day eligibility requirement and clarified the sole basis for phased Survey 2 invitations.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Qualifying children must have progressed normally and then had an identifiable date when one or both parents first noticed a clear behavior or skill change associated with the child's later autism presentation. The change need not unfold within seven days. Among eligible respondents, wave assignment depends only on Survey 1 confidence that relevant records can be produced; vaccination status is unknown and not collected in Survey 1.
- **Next steps:** Define the exact observable eligibility questions and record-confidence response groups in Survey 1.

## 2026-09-25 — Locked unprompted narrative sequence and partial capture

- **What we did:** Defined the placement, preservation, and methodological role of Survey 2's unprompted narrative.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Survey 2 will display one question at a time; the detailed 15-day narrative is completed and saved before any named-event prompt. The narrative can support onset eligibility assessment, later answers cannot overwrite it, and a submitted narrative is retained as a disclosed partial response if the parent drops out.
- **Next steps:** Draft the exact narrative prompt and prespecified narrative-based onset rubric in the Survey 2 instrument and validation manual.

## 2026-09-25 — Narrowed the v5 usable-record requirement

- **What we did:** Reduced participant documentation burden and aligned the analysis with the intended records request.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** A usable submission requires the completed 15-day narrative, parent-entered birthdate without documentary proof, and a record establishing the actual date and products at the most recent vaccination before onset. Complete vaccination histories are not required. The overview now limits the resulting design to a most-recent-vaccination timing analysis rather than full SCCS.
- **Next steps:** Define acceptable evidence and rules for no prior vaccination, unknown vaccination, and records that do not establish which visit was the most recent.

## 2026-09-25 — Added vaccine-free well-visit comparison

- **What we did:** Added retention and analysis of participants whose most recent regularly scheduled well-child visit before onset included no vaccination.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Survey 2 will ask for the visit timing, whether a vaccine was actually given, and whether an intervening vaccination occurred before onset. The analysis will plot visit-to-onset intervals even for a small group, separate survey-reported from record-confirmed controls, and exclude unknown or contaminated cases from the confirmed vaccine-free group without discarding them.
- **Next steps:** Specify the exact Survey 2 response options and choose common interval bins for vaccination and vaccine-free well-visit plots.

## 2026-09-25 — Clarified the 100-record target

- **What we did:** Defined whether vaccine-free well-visit records are included in the study target.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** The target is 100 usable records total across documented most-recent-vaccination cases and usable vaccine-free regularly scheduled well-child-visit cases; it is not 100 vaccinated cases plus controls.
- **Next steps:** Define evidence standards and common analysis bins for the two record groups.

## 2026-09-25 — Capped supplemental recruitment sources

- **What we did:** Defined the recruitment expansion allowed if the initial source does not yield 100 usable records.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** The study may add up to three approved organizations sequentially as needed. Each source must use the approved materials and will retain separate invitation, response-funnel, and record-yield reporting.
- **Next steps:** Define evidence standards and the organization activation rule.

## 2026-09-25 — Locked one-child rule and SORA terminology

- **What we did:** Finalized child selection for families with multiple autistic children and aligned the phenotype name with the study objective.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Families answer about the youngest child who developed normally and later had an identifiable onset date; if none qualify, they answer about the youngest autistic child. The overview calls the phenotype sudden-onset regressive autism while defining sudden onset as a dateable first noticeable change, without a seven-day completion criterion.
- **Next steps:** Translate the rule into exact Survey 1 branching and respondent-facing wording.

## 2026-09-25 — Made redacted narratives a public study output

- **What we did:** Fixed the disposition of Survey 2's unprompted narratives.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Each unprompted narrative will be included in the public-use dataset after trained redaction and disclosure-risk review. Redaction preserves event order, relative timing, and scientific content while removing or generalizing identifying details. Consent will disclose public narrative release and the no-revocation policy.
- **Next steps:** Create the redaction manual, reviewer workflow, and consent language.

## 2026-09-25 — Corrected the v5 retention boundary

- **What we did:** Distinguished parent-entered survey content from uploaded evidence files for retention purposes.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Parent-entered Survey 1 and Survey 2 content, including original narratives, and the associated study dataset are retained for 20 years. Uploaded videos, photographs, vaccination proof, clinical records, screenshots, messages, and other evidentiary documents are destroyed after 18 months unless longer retention is required.
- **Next steps:** Carry the same distinction into consent, storage architecture, destruction procedures, and the evidence-submission instructions.

## 2026-09-25 — Added three-reviewer two-pass onset assessment

- **What we did:** Defined independent onset review before and after reviewers see submitted evidence.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Three reviewers independently lock SORA eligibility, onset date or bounds, uncertainty interval, and supporting reasons from the narrative alone, then repeat the assessment with onset-supporting evidence. The study preserves all six assessments and reports inter-reviewer agreement, within-reviewer changes, exact three-reviewer agreement, and adjudication frequency.
- **Next steps:** Draft the reviewer rubric, masking procedure, date-tolerance rules, and adjudication form.

## 2026-09-25 — Named the three onset reviewers

- **What we did:** Assigned the three reviewers for the two-pass onset assessment.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Steve Kirsch, Karl Jablonowski, and Brian Hooker are the designated onset reviewers. Their assessments are independent in the procedural sense—completed separately and blinded to one another—but the overview does not mischaracterize the reviewers as independent of the study team.
- **Next steps:** Assign the remaining study leadership, analysis, data-custody, and operational roles.

## 2026-09-25 — Separated onset adjudication from vaccination abstraction

- **What we did:** Strengthened the three-reviewer workflow so vaccination timing cannot influence onset assessment.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Pass 1 uses the narrative alone; Pass 2 uses onset-supporting evidence with vaccination information masked; only after all six onset assessments are locked is vaccination information abstracted and linked. Unavoidably unblinded cases are flagged, counted, and excluded in a prespecified sensitivity analysis.
- **Next steps:** Create the masking SOP, adjudication copies, exposure-abstraction form, and unblinding log.

## 2026-09-25 — Defined guaranteed and adaptive participant compensation

- **What we did:** Clarified payment for good-faith submissions and added a possible recruitment-response increase.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Every good-faith evidence submission receives $25 regardless of usability or findings. Subject to advance IRB approval, compensation may rise to no more than $100 per complete response under prespecified operational triggers unrelated to vaccination results. Equal work receives equal compensation, including retroactive top-ups for earlier completers if the rate increases.
- **Next steps:** Fix the adaptive trigger, checkpoint, objective completeness definition, payment increments, and budget before IRB submission.

## 2026-09-25 — Fixed the adaptive compensation increments

- **What we did:** Specified the timing, increment, cap, and equal-payment rule for adaptive compensation.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Complete-response compensation begins at $25 and rises by $25 at two-week checkpoints when fewer than 100 usable records have been obtained, to a maximum of $100. Each increase includes retroactive top-ups for earlier participants who completed the same work. Triggers use operational yield only, never vaccination content or interim results.
- **Next steps:** Define objective complete-response criteria and the treatment of submissions awaiting usability review at each checkpoint.

## 2026-09-25 — Separated compensation completeness from scientific usability

- **What we did:** Fixed the denominator used at adaptive-compensation checkpoints.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Two-week payment increases depend only on whether 100 objectively complete submissions have been received. Administrative completeness requires the Survey 2 fields, narrative, birthdate, and requested documentation, but does not use reviewer judgments or scientific results. Recruitment remains directed toward 100 scientifically usable records even after payment increases stop.
- **Next steps:** Translate the completeness checklist into the Survey 2 submission workflow and payment SOP.

## 2026-09-25 — Fixed four Survey 1 record-confidence groups

- **What we did:** Defined the record-availability choices used to phase Survey 2 invitations.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Eligible respondents are grouped as definitely available now; probably available and known how to obtain; might be available but requires investigation; or probably unavailable. Groups are invited sequentially from 1 through 4. No fifth definitely-unavailable group is used.
- **Next steps:** Draft the respondent-facing Survey 1 question and determine whether each group is invited all at once or in smaller batches.

## 2026-09-25 — Added adaptive Survey 2 invitation batches

- **What we did:** Defined the initial and later Survey 2 invitation-batch strategy.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** The first batch randomly selects 100 eligible respondents from the highest available confidence group. Later batch sizes use observed operational response rates plus a prespecified conservative allowance so expected cumulative yield exceeds 100. Selection is random within confidence groups, higher-confidence groups are exhausted first, and all qualifying records from open batches are retained even above 100.
- **Next steps:** Freeze the response window, batch-size formula, allowance, randomization method, and seed before recruitment.

## 2026-09-25 — Fixed Survey 2 batch-size calculation

- **What we did:** Added the approved 20% allowance to the adaptive invitation calculation.
- **Command / executable:** Manual Markdown revision with `apply_patch`.
- **Outputs:** Updated `protocol/v5/study_overview.md`.
- **Results:** Later batch size is the ceiling of 1.20 times the remaining usable-record target divided by observed usable-record yield per matured invitation. Open batches are excluded from the yield denominator. If no usable record has yet been obtained, invite another random batch of up to 100 and recalculate after two weeks. Batch size is capped by the remaining eligible pool and fills from confidence groups in order.
- **Next steps:** Fix the random-selection method and seed, and define when pending record reviews become eligible for the batch-yield count.

## 2026-09-25 — Made recruitment independent of reviewer judgments

- **What we did:** Changed the invitation calculation and stopping rule to use objectively complete record submissions received.
- **Command / executable:** Manual Markdown revision with `apply_patch`; `rg` consistency review and `git diff --check`.
- **Outputs:** `protocol/v5/study_overview.md` version 1.1 draft.
- **Results:** The 100-record operational target, two-week batch-yield formula, compensation checkpoints, and decision to add an organization now use administrative completeness only. Three-reviewer onset assessments determine the later analysis populations, not whether more people are invited. The 20% allowance and zero-yield fallback remain in the batch rule.
- **Next steps:** Define the exact administrative completeness checklist and random-selection procedure before recruitment.

## 2026-09-25 — Clarified the 100-submission minimum

- **What we did:** Made explicit that 100 complete submissions is a minimum recruitment threshold, not a cap on collected records.
- **Command / executable:** Manual Markdown revision with `apply_patch` and `git diff --check`.
- **Outputs:** `protocol/v5/study_overview.md` version 1.2 draft.
- **Results:** New invitation batches end after at least 100 objectively complete submissions have been received, while every submission from an already-open batch is retained and reviewed, including those above 100.
- **Next steps:** Define the administrative completeness checklist and random-selection procedure before recruitment.

## 2026-09-25 — Added most-recent-vaccination confirmation

- **What we did:** Added a Survey 2 check for vaccination after the visit the parent initially identifies as most recent before onset.
- **Command / executable:** Manual Markdown revision with `apply_patch` and `git diff --check`.
- **Outputs:** `protocol/v5/study_overview.md` version 1.3 draft.
- **Results:** A reported later dose triggers a request for the later visit's date, products, and record. An Unsure answer is retained with the most-recent interval flagged unconfirmed. The study still requests only the relevant visit record, not a complete vaccination history.
- **Next steps:** Put the exact conditional question and response options into the Survey 2 instrument.

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

## 2026-09-04 — Published Airtable branching verification

- **What we did:** Tested the published form's developmental-pattern, regression-speed, same-day pediatrician timing, no-prior-well-visit, and vaccine-confirmation branches without submitting a record.
- **Command / executable:** Read-only live Chrome inspection with form controls.
- **Outputs:** No data artifact; verification only.
- **Results:** `Mixed` exposes regression speed; slow change hides sudden-onset detail; rapid/dateable change exposes it. The pediatrician timing confirmer appears for both same-day choices and hides for later onset. Selecting no prior well-child visit hides every visit-dependent follow-up. Selecting vaccines `Yes` exposes the vaccine checklist, while confirmed `No` hides it. The referral-code field is visible.
- **Next steps:** Form logic is ready; optional copy cleanup only.

## 2026-09-04 — Survey record-verification plan

- **What we did:** Created a prespecified plan for validating onset timing, well-child visits, vaccination status, intervening vaccinations, and same-day event order against contemporaneous records.
- **Command / executable:** Manual Markdown authoring with `apply_patch`.
- **Outputs:** `protocol/v4_SPARK/survey_record_verification_plan_v1.md`.
- **Results:** The plan defines sampling, blinded review, evidence standards, independent fact-level classifications, date tolerances, audit trails, and verified-versus-unverified sensitivity reporting.
- **Next steps:** Freeze the sampling rules and tolerances before beginning record review.

## 2026-09-04 — Intervening-vaccination branch verification

- **What we did:** Refreshed the published Airtable form and tested the new question about vaccinations occurring after the preceding well-child visit and before onset.
- **Command / executable:** Read-only live Chrome branch inspection; no form submission.
- **Outputs:** No data artifact; verification only.
- **Results:** The required question appears only after `No--I am certain no vaccines were given` at the visit and provides confirmed No, Yes, and unknown choices. It hides when vaccination at the visit is Yes. Selecting an intervening-vaccination Yes currently produces no date/product follow-up.
- **Next steps:** The question is sufficient to exclude contaminated no-shot controls; optionally collect the intervening vaccination's approximate date and product for vaccination-interval analysis.

## 2026-09-04 — Current no-vaccination control count

- **What we did:** Audited the newest Downloads public export for confirmed no-vaccination well-child visits and never-vaccinated children with usable onset-to-visit intervals.
- **Command / executable:** PowerShell `Import-Csv` and field-value cross-tabulation on `C:\Users\stk\Downloads\SOA2-Public view.csv` (408 rows).
- **Outputs:** No new artifact; read-only calculation.
- **Results:** Only one response completed the new confirmed-no-vaccine-at-visit field, and its visit interval was unknown. Thirteen children were reported never vaccinated, but only six had a usable visit interval. The older visit checklist had 37 rows without vaccination checked, only 16 with a nonmissing/known interval; these are not confirmed no-shot controls.
- **Next steps:** Accumulate responses under the new explicit confirmation and intervening-vaccination questions before performing the negative-control timing test.

## 2026-09-04 — Exploratory no-vaccination timing results

- **What we did:** Applied the existing days 0–5 versus days 6–89 person-time comparison separately to never-vaccinated children and older checklist records without vaccination selected.
- **Command / executable:** PowerShell filtering plus Python exact conditional-binomial calculations with null early-window probability `6/90`.
- **Outputs:** No new artifact; read-only calculation.
- **Results:** Never-vaccinated usable cases had 2 early and 4 reference-window reports (RR 7.0; one-sided exact p=0.0557). The unconfirmed checklist-based group had 6 early and 7 reference-window reports after excluding three observations beyond day 89 (RR 12.0; one-sided exact p=9.995e-5). The latter group is vulnerable to exposure misclassification; both results are exploratory.
- **Next steps:** Report these results rather than suppressing them, but do not label either as the prespecified confirmed no-shot negative-control analysis.

## 2026-09-04 — Same-day vaccination-time field check

- **What we did:** Tested the published same-day onset plus confirmed-vaccination branch for the proposed vaccination-time capture.
- **Command / executable:** Read-only live Chrome branch inspection; no form submission.
- **Outputs:** No data artifact; verification only.
- **Results:** The chronology field asks for visit start/end time and onset time, but not vaccination time. After selecting confirmed vaccination `Yes`, the vaccine-product checklist appears, but no vaccination-time field appears.
- **Next steps:** Add or publish a vaccination-time field visible when onset is same-day and vaccines at the visit are confirmed Yes.

## 2026-09-04 — Structured same-day time-field verification

- **What we did:** Refreshed and tested the two newly published structured time questions under same-day, confirmed-vaccination, confirmed-no-vaccination, and next-day conditions.
- **Command / executable:** Read-only live Chrome branch inspection; no form submission.
- **Outputs:** No data artifact; verification only.
- **Results:** Both vaccination time and onset time appear for same-day cases and hide for next-day cases. The vaccination-time question incorrectly remains visible and required when the respondent confirms no vaccines were given. Both time picklists currently cover only 8 a.m. through 5 p.m.; the onset-time list therefore cannot represent evening or overnight onset.
- **Next steps:** Require confirmed vaccination Yes for vaccination-time visibility, and expand onset-time coverage to the full day or use a time field.

## 2026-09-04 — Uncached structured time-field verification

- **What we did:** Bypassed the existing Chrome form instance and opened a fresh published form with a cache-busting query parameter, then repeated the same-day and next-day branch tests.
- **Command / executable:** Read-only fresh in-app browser inspection; no submission.
- **Outputs:** No data artifact; corrective verification.
- **Results:** The current published form is correct. For same-day confirmed No, onset time appears and vaccination time does not. For same-day confirmed Yes, both appear. For next-day onset, both hide. Onset choices now span `7am or earlier` through `10pm or later` plus `Don't remember`. The preceding stale-tab result was superseded.
- **Next steps:** No correction required for these visibility rules.

## 2026-09-10 — Neutral X survey-ad creative

- **What we did:** Generated a cause-neutral X ad for the parent survey using an autism-explicit early-development framing and no vaccine, sudden-onset, institutional, or compensation claims.
- **Command / executable:** Built-in image generation.
- **Outputs:** `assets/ads/x-ad-understanding-autism-neutral-v1.png`.
- **Results:** Produced a landscape creative with exact survey copy, a parent-child image, and a prominent `TAKE THE SURVEY` call to action.
- **Next steps:** Test this creative as its own recruitment source and retain source-specific funnel metrics.

## 2026-09-10 — Neutral X ad artifact correction

- **What we did:** Removed the stray mark above the word `researchers` while preserving the ad design.
- **Command / executable:** Built-in image editing.
- **Outputs:** `assets/ads/x-ad-understanding-autism-neutral-v2.png`.
- **Results:** Produced a non-destructive corrected version; v1 remains available.
- **Next steps:** Use v2 for publication.

## 2026-09-10 — Neutral X ad timing callout and clean typography

- **What we did:** Added `Takes about 2 minutes` above the CTA and regenerated the creative to eliminate the malformed accented `e` and stray dot around `researchers`.
- **Command / executable:** Built-in image generation and visual review.
- **Outputs:** `assets/ads/x-ad-understanding-autism-neutral-v3.png`.
- **Results:** The final v3 uses plain unaccented `researchers`, contains no nearby artifact, and includes the requested completion-time callout.
- **Next steps:** Use v3 for publication after confirming the two-minute completion claim against observed timings.

## 2026-09-13 — Draft v10 seven-prediction application to latest public CSV

- **What we did:** Applied the mutually exclusive v10 decision regions to the latest 456-row public export, separately for VAX and NEVER, preserving contradictions and unknown status.
- **Command / executable:** Read-only Python/Scipy analysis of `C:\Users\stk\Downloads\SOA2-Public view.csv` (SHA-256 `BB11EB80572376062BF8D2359418F8F6C7E06B8EDF520BA4F79FE4EAC636F25B`).
- **Outputs:** Chat assessment only; source CSV was not modified.
- **Results:** Eligible sudden-onset cohort: VAX 295, NEVER 12, unknown 87, contradictory 3. VAX P2 and P7 were inconsistent with null; VAX P1 and P3-P6 were indeterminate. All NEVER predictions were indeterminate. No result met the v10 null region.
- **Next steps:** Freeze the missing P1-P6 bootstrap, multinomial, and directional procedures before treating later data as confirmatory; enlarge the NEVER negative-control cohort.

## 2026-09-13 — Parent-noticed onset age histogram, 4–60 months

- **What we did:** Plotted exact one-month age-at-onset counts from 4 through 60 months for the same sudden-onset cohort used in the seven-prediction analysis (legacy sudden-onset respondents plus newer respondents reporting a rapid, dateable change).
- **Command / executable:** `python analysis\plot_parent_onset_age_months.py` against the read-only public export.
- **Inputs:** `C:\Users\stk\Downloads\SOA2-Public view.csv` (456 rows; SHA-256 `BB11EB80572376062BF8D2359418F8F6C7E06B8EDF520BA4F79FE4EAC636F25B`).
- **Outputs:** `outputs/parent_onset_age_4_to_60_months.png`; reproducible script `analysis/plot_parent_onset_age_months.py`.
- **Results:** 397 respondents met the sudden-onset cohort rule; 394 had a valid whole-month onset age; 345 were within 4–60 months. Excluded from the displayed range were 32 below 4 months, 17 above 60 months, and 3 missing or invalid. The largest exact-month counts were 18 months (63), 15 months (38), 12 months (31), and 24 months (21).
- **Next steps:** If this pattern is interpreted analytically, quantify digit/visit-age heaping and stratify by recruitment source rather than treating the raw age histogram as a causal test.

## 2026-09-14 — Onset-age histogram sensitivity to onset-date confidence

- **What we did:** Compared the 4–60-month onset-age profile for the full sudden-onset cohort with respondents selecting an onset-date confidence category no wider than one month. Missing confidence and `Could be off by a month or more` were excluded from the restricted group.
- **Command / executable:** `python analysis\compare_onset_age_by_date_confidence.py` against the read-only public export.
- **Outputs:** `outputs/parent_onset_age_confidence_comparison_4_to_60.png`; reproducible script `analysis/compare_onset_age_by_date_confidence.py`.
- **Results:** The plotted denominator fell from 345 to 154. The normalized exact-month profiles remained similar (Pearson correlation 0.966). The principal 12-, 15-, 18-, and 24-month peaks persisted; 18 months declined from 18.3% to 14.3%, while 20 months rose from 4.9% to 7.8%.
- **Next steps:** Treat the comparison as a sensitivity analysis because onset-date confidence was unavailable for many legacy records and is self-reported rather than independently validated.

## 2026-09-15 — CloudResearch regression follow-up response audit

- **What we did:** Reviewed all four responses in the CloudResearch/Airtable follow-up export for eligibility contradictions, narrative specificity, repeated language, chronology, and participant-list membership.
- **Input:** `C:\Users\stk\Downloads\Regression Patterns Follow up-Grid view.csv` (4 rows; SHA-256 `872EA1866BFEFAADE2ACE53119DF58C46855E285EF7A49D6AA5184515FFF90CB`).
- **Results:** The file does not ask respondents to describe the regression itself, so absence of terms such as lost eye contact, language loss, or stimming cannot establish gaming. None of the four narratives independently establishes a sudden, lasting loss of previously acquired skills. One response explicitly describes gradually increasing behavior, and two describe school/social stress or masking rather than a clearly dated developmental regression. The four responses use differing styles and contain no obvious copied wording. A later review of the 30-row original export confirmed that all four had selected the sudden-regression option; the separate seven-ID `autism_participants.csv` was therefore not a valid completeness check for the follow-up invite list.
- **Next steps:** Add a neutral open-ended prompt asking what specific ability was present before onset and absent afterward, then assess persistence, chronology, independent observation, and supporting records without revealing a preferred cause.

## 2026-09-15 — Joined original/follow-up CloudResearch audit

- **What we did:** Matched the four follow-up PIDs to the 30-response original regression-pattern export and compared onset age, confidence, claimed record support, and follow-up narrative.
- **Input:** `C:\Users\stk\Downloads\Regression Patterns-Grid view.csv` (30 rows; SHA-256 `E503BC69368B9A155CFD9F1E620B86044EA73DDA7EDF9740119105C11A4203D0`) joined to the four-row follow-up export by PID.
- **Results:** Seven of 30 respondents selected sudden dramatic lasting loss; four supplied follow-ups. The 48-month case described a progressive increase in tantrums rather than a sudden skill loss. The 96-month case described bullying, withdrawal, and bottled-up emotions rather than developmental regression. The 8-month case attributed onset to masking becoming overwhelming, an age/concept combination that is difficult to reconcile. The 22-month daycare/crying case is plausible but remains unverified because no lost skill was elicited. No pair of narratives showed obvious copied phrasing.
- **Next steps:** Do not infer fraud solely from these answers. Freeze a blinded eligibility rubric and collect a concrete before/after lost-skill narrative before determining inclusion in the research cohort.

## 2026-09-16 — Revised screener response check

- **What we did:** Reviewed the eight responses in the revised CloudResearch/Airtable screener for concrete before/after skill loss, chronology, onset precision, and potential documentary corroboration.
- **Input:** `C:\Users\stk\Downloads\screener.csv` (8 rows; latest export reviewed read-only).
- **Results:** The three responses collected after the added evidence and symptom questions were substantially more discriminating. Record 18 is a strong, specific, documentable candidate; record 19 is plausible and potentially documentable but describes a change unfolding over more than one month; record 20 is sparse and approximate despite claiming before-and-after records. Earlier record 6 contains a chronology contradiction: diagnosis at 13 months precedes reported onset at 50 months.
- **Next steps:** Apply a prespecified eligibility rubric rather than judging authenticity by writing style; automatically flag diagnosis before onset, missing diagnosis age, approximate-only onset, and unsupported or nonspecific skill loss for manual review.

## 2026-09-16 — Six revised-form screener records

- **What we did:** Reloaded `screener.csv` and reviewed the six revised-form submissions (record numbers 18–23) for concrete loss, timing, persistence, diagnosis chronology, and documentary support.
- **Input:** `C:\Users\stk\Downloads\screener.csv` (11 total rows; six revised-form records).
- **Results:** Records 18 and 23 are the clearest candidates, with concrete acquired abilities, specific losses, and dated video support. Record 19 has potentially strong timing corroboration but a less sharply defined skill-loss phenotype and change over more than one month. Records 20 and 22 have approximate, memory-based onset; record 21 cannot determine onset precision, speed, or persistence. All six report diagnosis after onset. None reports an initial noticeable change within seven days; three report 8–30 days, two more than one month, and one cannot determine.
- **Next steps:** Preserve all six paid responses, but use a prespecified tiered invitation rule; verify claimed records without conditioning payment or inclusion on any suspected cause.

## 2026-09-16 — Pediatric-visit interval by onset age

- **What we did:** Reloaded the latest `screener.csv` and tabulated the parent-recalled interval from the most recent pediatric visit to onset, stratified at onset age 20 months.
- **Input:** `C:\Users\stk\Downloads\screener.csv` (13 total rows; modified 2026-09-16 12:16 local time).
- **Results:** Five children had onset at 20 months or younger; one older-form response lacked the interval. Among four usable responses, one each reported 7–29, 30–59, 60–89, and 90+ days. Among four usable responses with onset above 20 months, one reported 0–6 days and three reported 90+ days. Thus 90+ days was 25% in the younger group versus 75% in the older group, but each denominator was only four.
- **Next steps:** Continue collecting responses and report exact counts with percentages; do not infer a visit-schedule effect from this very small convenience sample.

## 2026-09-16 — Latest screener eligibility and narrative audit

- **What we did:** Audited the latest 19-row `screener.csv`, focusing on the 14 revised-form records (18–31), against the 4–60-month onset rule, diagnosis chronology, developmental plausibility, and agreement between open-ended narratives and the prompted symptom checklist.
- **Input:** `C:\Users\stk\Downloads\screener.csv` (modified 2026-09-16 16:34 local time).
- **Results:** Records 24, 29, and 30 reported onset beyond 60 months. Records 29, 30, and 31 reported diagnosis in the same whole-month age as onset; this is a review flag but not proof of impossibility because ages are rounded to months. Record 25 reported diagnosis before onset and its freshman-year narrative conflicts with a 13-month onset, while record 27 describes normal speech/social skills before a claimed four-month onset and likely reflects year/month entry confusion. Several records selected many prompted symptoms not evident in their open narratives, especially records 20, 21, 25–30; records 18, 23, and 31 showed better narrative/checklist agreement.
- **Next steps:** Add hard range validation and unit-safe age entry, treat open-ended acquired-skill loss as the primary phenotype evidence, and use checklist selections only as secondary prompts requiring later verification.

## 2026-09-26 — v5 Survey 2 vaccination-visit spacing decision

- **What we did:** Updated `protocol/v5/study_overview.md` to ask about routine versus delayed/alternative vaccination timing and the immediately preceding vaccination visit for every parent reporting a pre-onset vaccination, after the locked unprompted narrative.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.13 draft.
- **Results:** The preceding visit is recorded by date when known, otherwise approximate spacing or unknown; multiple products on one date count as one visit. No additional prior-visit document is required, and unsupported dates remain parent-reported.
- **Next steps:** Carry these items into the Survey 2 instrument and prespecify the descriptive check for multiple vaccination visits within 90 days before onset.

## 2026-09-26 — v5 quarter-start companion histograms

- **What we did:** Added calendar-quarter-start lag companion histograms for the overall last-vaccination plot, every prespecified visit-age group, and every plotted vaccine-product group; specified one- and two-month-shifted quarterly grids as sensitivity displays.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.14 draft.
- **Results:** Each companion uses the exact child subset and date basis of its vaccination plot, with explicit denominators and an overflow bin for quarter lengths beyond the common comparison range. The calendar-anchor displays are described as descriptive, not as an uncalibrated formal null test.
- **Next steps:** Freeze exact bin endpoints, display specifications, and any inferential use in the statistical analysis plan before examining the records-based lag plots.

## 2026-09-26 — v5 primary date for day-0–2 analysis

- **What we did:** Recorded the decision that reviewers' agreed best-estimate onset date is primary for the planned day-0–2 post-vaccination analysis; the earliest documented post-change date is a separate secondary documentation-date analysis.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.15 draft.
- **Results:** The two dates are not interchangeable and will have separately labeled analyses and denominators.
- **Next steps:** Carry this priority into the statistical analysis plan and plot specifications.

## 2026-09-26 — v5 paired Onset 1 and Onset 2 timing displays

- **What we did:** Revised `protocol/v5/study_overview.md` to make the continuous baseline-break date (Onset 1) the primary histogram anchor and the first definite developmental-change date (Onset 2) a separately required companion for overall, visit-age, and vaccine-product histograms. This supersedes the immediately preceding primary-date decision.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.16 draft.
- **Results:** Defined uncertainty days as the calendar-day gap between the two accepted dates, so Onset 1 lag = Onset 2 lag minus that gap. Visit records are ascertained in the 90 days before Onset 2; Onset 1 can be negative and remains plotted. The same children are used for directly paired displays. An acute baseline-break spike is not, by itself, evidence of a vaccine effect on autism-related developmental change.
- **Next steps:** Carry the neutral pre-disclosure continuity question into Survey 2, specify both endpoints and their separate null models in the statistical analysis plan, and test negative-lag and missing-date cases before IRB submission.

## 2026-09-26 — Standard names for paired timing measures

- **What we did:** Standardized the paired timing terms in `protocol/v5/study_overview.md`: baseline-break lag, definite-change lag, and transition gap; retired Onset 1/Onset 2 shorthand from the active overview.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.17 draft.
- **Results:** The identity is baseline-break lag = definite-change lag − transition gap. Negative baseline-break lags remain valid; the transition gap is distinguished from the broader plausible-onset uncertainty interval.
- **Next steps:** Use the same labels in Survey 2, reviewer forms, plots, and the statistical analysis plan.

## 2026-09-26 — Primary paired-timing endpoint

- **What we did:** Clarified in `protocol/v5/study_overview.md` that baseline-break lag is the single planned primary day-0–2 timing endpoint, while definite-change lag is a required prespecified secondary endpoint; this supersedes the earlier best-estimate-onset primary designation.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.18 draft.
- **Results:** Adjacency is judged from the record rather than vaccination proximity. Separate null models are required because acute post-vaccination symptoms could concentrate baseline breaks even under no vaccine effect on the later developmental change. Until the baseline-break null is valid and frozen, its day-0–2 result remains descriptive.
- **Next steps:** Specify the adjacency rubric and primary null model in the records manual and statistical analysis plan before IRB submission.

## 2026-09-26 — Continuous baseline-break duration rule

- **What we did:** Recorded the agreed rule that an evidence-supported continuous episode adjacent to the definite developmental change has no fixed maximum transition gap; a full return to the prior baseline breaks adjacency regardless of duration.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.19 draft.
- **Results:** The primary paired analysis retains otherwise eligible long-gap cases. Transition-gap lengths will be reported, paired analyses repeated with gaps of 30 days or less, and cases over 30 days reported separately.
- **Next steps:** Specify the reviewer evidence/continuity rubric and exact sensitivity displays before review or exposure-linked analyses.

## 2026-09-26 — Parent-assessed continuity questions

- **What we did:** Simplified the pre-disclosure Survey 2 timing sequence to ask when the clear developmental change began, then whether an immediately preceding uncertain period occurred and how long it lasted. The parent's judgment determines whether there was an intervening full return to normal.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.20 draft.
- **Results:** An approximate duration will not be forced into a precise calendar date; reviewer evidence tiers and objectively verified analysis requirements remain separate from the parent's report.
- **Next steps:** Draft the exact one-question-at-a-time Survey 2 wording and branch logic, then test it for neutral phrasing and date precision.

## 2026-09-27 — Retain submitted partial responses

- **What we did:** Clarified that stopping or declining at the later disclosure does not cause any already submitted survey answer or narrative to be discarded. Proposed redacted public release includes these partial narratives, subject to explicit advance consent, IRB approval, and disclosure-risk review.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.21 draft.
- **Results:** Partial-response status and departure point remain available for analysis. The separate 18-month destruction rule for uploaded evidence files is unchanged.
- **Next steps:** Put the partial-response and public-release policy into consent language for IRB review.

## 2026-09-27 — Retain all submitted source evidence for re-review

- **What we did:** Superseded the earlier 18-month destruction policy for uploaded evidence. The v5 draft now proposes retaining all submitted survey content, source evidence, contact information, and study records for 20 years after study closure, with restricted originals separate from public-use data.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.22 draft.
- **Results:** Source files will be encrypted from receipt and available to additional qualified researchers only through an IRB-approved controlled-access process; raw evidence will not be public. Consent, access/key controls, eventual destruction, and the no-revocation policy remain subject to IRB approval.
- **Next steps:** Specify the custodian, systems, key recovery, audit procedures, access-review workflow, consent text, and IRB submission details.

## 2026-09-27 — Keep records phase focused on regression cases

- **What we did:** Recorded the decision not to recruit a separate non-regression comparison cohort or add its questions to Survey 1. Nonqualifying intake responses remain in funnel reporting, but the records phase stays focused on qualifying regression cases.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.23 draft.
- **Results:** A post-vaccination baseline-break spike alone remains insufficient to infer vaccine-caused regression; without a valid frozen null model it is descriptive.
- **Next steps:** Develop the separate null models and interpretation rules in the statistical analysis plan without expanding Survey 1 to a non-regression cohort.

## 2026-09-27 — Recovery-gap and weekday displays

- **What we did:** Added a prompted, post-disclosure question and prespecified secondary display for vaccination followed by fever or another acute symptom, full parent-assessed recovery, X complete normal days, and later definite developmental change. Added derived weekday of the baseline-break date with vaccination weekday for context. Allowed Onset 1/Onset 2 as short figure labels while retaining precise definitions.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.24 draft.
- **Results:** A recovered earlier fever episode does not qualify as an adjacent baseline break. An X greater than zero would refute an absolute never-occurs claim; equal counts over X are not a valid uncalibrated no-effect expectation, so the display is descriptive unless a separate expected distribution is frozen and calibrated.
- **Next steps:** Draft exact Survey 2 branch wording and prespecify evidence, denominator, missingness, and X-bin rules in the analysis plan.

## 2026-09-27 — Required X and Onset 1 weekday figures

- **What we did:** Made the X-day distribution an explicit required integer-day histogram and the reviewer-agreed Onset 1 weekday distribution an explicit required seven-bar figure with a vaccination-weekday companion panel.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.25 draft.
- **Results:** The X histogram distinguishes a full return with X = 0 from no full return, and reports the symptom, recovery, measurable-X, and unknown denominators. A zero count of X > 0 will receive a confidence bound, not a claim of impossibility or causation. Weekdays are derived without added parent questions.
- **Next steps:** Specify exact display conventions and missingness/evidence tiers in the statistical analysis plan.

## 2026-09-28 — Correct X denominator and zero category

- **What we did:** Corrected X to count complete normal days after the post-vaccination acute period and before the definite change among all cases with the reported symptom and adequate timing, including continuous no-return cases as X = 0. Kept no-return and brief-return zeros separately coded.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.26 draft.
- **Results:** The prior X histogram denominator had incorrectly required a full return. A large well-ascertained sample with all X = 0 is now explicitly recognized as noteworthy, but no-effect does not imply a uniform X distribution or exclude shared causes of the symptom and change.
- **Next steps:** Define the exact eligible denominator, evidence tiers, uncertainty treatment, and any calibrated null before data review.

## 2026-09-28 — Scope X to uncertainty plus regression

- **What we did:** Corrected the overall X figure to include only regression cases with a prior uncertain-functioning period, whether or not the period followed vaccination; removed an implicit 90-day or immediate-adjacency limit from the neutral Survey 2 question. No age-group X panels are planned.
- **Command / executable:** Manual Markdown edit; `git diff --check` and sensitive-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.27 draft.
- **Results:** Survey 2 now asks about the most recent uncertain period even if full normal functioning resumed before the clear change, allowing X greater than zero (including more than 100 days) to be observed rather than excluded by question wording. X = 0 includes no-return cases; those and brief-return cases remain separately coded.
- **Next steps:** Draft exact neutral branching and reviewer forms so the X denominator and earlier-period dates can be verified without confusing them with Onset 1.

## 2026-09-28 — Parent-reported autism at exploratory intake

- **What we did:** Clarified that Survey 1 relies on parent-reported autism without requiring a professional diagnosis or proof; the smaller Survey 2/records subset can collect diagnostic history and optional documentation.
- **Command / executable:** Manual Markdown edit; `git diff --check`.
- **Outputs:** `protocol/v5/study_overview.md` version 2.28 draft.
- **Results:** Missing diagnostic documentation does not automatically exclude a submitted case; parent-reported and clinically verified status remain distinct.
- **Next steps:** Draft the exact low-burden Survey 2 diagnosis-status question and records-review coding rule.

## 2026-09-28 — Focus detailed cohort on onset ages 6–24 completed months

- **What we did:** Set Survey 2 and records-phase eligibility at 6–24 completed months at the first definite developmental change, while retaining all Survey 1 responses in the intake counts.
- **Command / executable:** Manual Markdown edit; `git diff --check` and confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.29 draft.
- **Results:** The operational 100-record target applies to age-screened invitations; the primary timing analysis uses reviewer-agreed change age in range. Out-of-range or unresolved cases remain retained and reported separately.
- **Next steps:** Reflect the age screen, boundary handling, and child-selection rule in the Survey 1 and Survey 2 instruments and statistical analysis plan.

## 2026-09-28 — Count later age discrepancies toward 100 submissions

- **What we did:** Clarified that a respondent screened as 6–24 months at Survey 1 remains in the operational 100-record count after an objectively complete submission, even if Survey 2 dates or reviewer assessment later place onset outside that range.
- **Command / executable:** Manual Markdown edit; `git diff --check` and confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.30 draft.
- **Results:** Such cases remain retained and paid under the ordinary good-faith rules; age discrepancies are reported separately and do not enter the age-restricted primary timing analysis. The 100-submission target is distinct from the final analytic sample size.
- **Next steps:** Implement separate operational-count and final-analysis eligibility flags in the survey and analysis specifications.

## 2026-09-28 — Draft v5 Survey 1 and Survey 2 instruments

- **What we did:** Inspected the live short survey and the v5 overview; created separate respondent-facing working drafts and implementation notes for the dateable-onset intake and staged follow-up, and updated the v5 document guide.
- **Command / executable:** `Invoke-WebRequest https://www.skirsch.com/autism/survey.htm`; manual Markdown edits; `git diff --check` and confidential-partner-name scan.
- **Outputs:** `protocol/v5/survey1.md` version 1.0 draft, `protocol/v5/survey2.md` version 1.0 draft, and updated `protocol/v5/document_guide.md`.
- **Results:** Survey 1 retains the brief developmental-pattern format but removes the seven-day cutoff and requires a determinable first-clear-change date for follow-up screening. Survey 2 places a locked 15-day narrative and neutral continuity questions before staged event disclosure, then specifies structured dates, records, partial responses, and routing. No confidential recruitment organization is named in the new active drafts.
- **Next steps:** Resolve exact consent/disclosure wording with the IRB, reconcile field definitions with the records manual and statistical plan, then test every screen and branch before deployment.

## 2026-09-29 — Make Survey 1 date confidence sufficient for follow-up screening

- **What we did:** Removed the actual onset-date entry from Survey 1 and clarified that a parent who is confident they can determine the date later remains eligible for Survey 2, subject to the existing pattern, age, consent, and contact screens.
- **Command / executable:** Manual Markdown edit; `git diff --check` and confidential-partner-name scan.
- **Outputs:** `protocol/v5/survey1.md` version 1.1 draft and `protocol/v5/study_overview.md` version 2.31 draft.
- **Results:** Survey 1 records date-confidence and record-availability confidence separately; the latter alone sets the order of Survey 2 invitation waves. Survey 2 remains the point where the actual parent-reported date is requested.
- **Next steps:** Test the screening and invitation branches and confirm the final question wording with the IRB.

## 2026-09-29 — Review separate X follow-up form

- **What we did:** Inspected the live Airtable form for the separate rapid-regression follow-up that measures a normal interval after vaccination and before the sudden change. This was a read-only review; no response was submitted.
- **Command / executable:** Opened the supplied form URL in a browser, inspected its displayed options and conditional day-count field, and tested unsubmitted negative and fractional entries.
- **Outputs:** No study files or form settings changed.
- **Results:** The form distinguishes no full return, a return under 24 hours, and a return of at least 24 hours; the last branch displays a required day-count field. The field was labeled Decimal and visibly retained `-1` and `1.5` after focus left it. The email field appeared optional, so matching to an earlier response needs another reliable key if email is omitted. The form lacks a clear path for a known full return whose duration cannot be estimated.
- **Next steps:** Configure nonnegative integer validation (and at least 1 day on the 24-hour-plus branch), ensure reliable record linkage, and add an unknown-duration option before treating the X values as analyzable.

## 2026-09-29 — Analyze early normal-interval follow-up export

- **What we did:** Read the existing Downloads CSV for the separate X follow-up sent to parents who previously reported sudden onset regardless of vaccination status. Counted response categories and checked non-identifying note content for timing qualifications. No source data were changed.
- **Command / executable:** PowerShell `Import-Csv` on `C:/Users/stk/Downloads/Normal interval-Grid view.csv`, grouped `Normal period?`, and inspected Notes without email addresses.
- **Outputs:** Analysis in chat; no derived dataset or edits to the CSV.
- **Results:** 29 responses: 24 vaccination/no full return, 2 vaccination/full return under 24 hours, 2 unsure about full return, and 1 no vaccination before change. The `Interval` column is blank in every row, so X=0 for the first 26 is derived from categorical choices rather than entered day counts. Several notes describe gradual or prolonged changes despite the prior sudden-onset screen. The export has no vaccination/onset dates, invitation denominator, or verified records; it does not calibrate a no-causal-effect null or distinguish it from a vaccine-causal model.
- **Next steps:** Link responses to the original screener, audit the sudden-onset classification and event dates, obtain response denominators, and prespecify a comparison distribution before using X inferentially.

## 2026-09-29 — Test linkage and null calibration for the normal-interval follow-up

- **What we did:** Read both Downloads CSV exports without editing them, checked identifier overlap and field completeness, and calculated a binomial sensitivity range for 26 categorical X=0 responses.
- **Command / executable:** PowerShell `Import-Csv` and grouped/count summaries of `Normal interval-Grid view.csv` and `SOA2-Public view.csv`; exact-email text-overlap check; `Math.Pow` sensitivity calculations.
- **Outputs:** Aggregate analysis in chat only; no row-level joined file was created.
- **Results:** The follow-up has 29 rows: 24 no full return, 2 return under 24 hours, 2 unsure, 1 no preceding vaccination; all 26 determinate vaccinated responses code X=0, and all numeric `Interval` cells are blank. The original public view has 499 rows and no email column; its `number` values are 46–577 versus follow-up record numbers 6–34, so there is no reliable shared key. One follow-up email appears somewhere in free text of the original export, insufficient for systematic linkage. In the newer explicit regression-speed field, 33 rows select rapid/dateable change, 32 have an onset date, and 17 check vaccination in the prior three days. The original export contains no structured individual vaccination-date field; pediatrician-visit intervals cannot substitute for vaccination intervals. If the null probability of X>0 were 5%, 10%, or 20%, the probability of observing 0 of 26 is 26.4%, 6.46%, or 0.302%, respectively; these are sensitivity assumptions, not null estimates from these files.
- **Next steps:** Obtain a privacy-preserving stable key or authorized email-bearing original export and individual vaccination/uncertain-period/onset dates; then audit rapid-onset eligibility and define a defensible comparison model before formal inference.

## 2026-09-29 — Link normal-interval responses to the newly downloaded SOA2 grid export

- **What we did:** Repeated the read-only linkage against `SOA2-Grid view.csv`, which includes parent email, and summarized the matched original responses without exporting identifiers or narratives.
- **Command / executable:** PowerShell `Import-Csv`; lowercase/trim exact-email index with duplicate-key rejection; categorical cross-tabs and missingness counts; `git diff --check`.
- **Outputs:** Aggregate results in chat only; source CSVs unchanged and no joined row-level file created.
- **Results:** The new grid has 509 rows, 402 nonblank email cells and 386 distinct normalized emails; 12 emails appear on multiple original rows. Of 29 normal-interval follow-ups, 21 link to exactly one original row, 1 email is ambiguous, 5 emails have no match, and 2 have no email. The 21 uniquely linked cases comprise 17 vaccination/no full return, 2 vaccination/return under 24 hours, 1 unsure, and 1 no preceding vaccination. Among the 19 linked determinate vaccinated X=0 responses, 13 checked vaccination in the three days before onset in the original response; 12 have an onset-date field and 15 report onset age 6–24 months. The grid has no structured per-child vaccination date or uncertain-period dates, so it cannot supply exact vaccination-to-onset lags or a calibrated null distribution for X. Most linked rows predate the newer explicit regression-speed question; blank speed values are not evidence of slow regression.
- **Next steps:** Resolve ambiguous and unmatched links with a child-level key; obtain exact vaccination and transition dates and a comparison population measured by the same X instrument before formal inference.

## 2026-10-01 — Refine Survey 2 recovery timeline and normal-days analysis

- **What we did:** Updated the Survey 2 draft and study overview to ask about wellness and behavior/skill baseline just before vaccination, preserve a separate post-disclosure event-by-event narrative through the clear change, distinguish new behaviors from reduced or missing skills on that day, and directly record post-vaccination symptom-resolution lag and complete normal days.
- **Command / executable:** Read the current v5 Markdown and relevant methods literature; edited with `apply_patch`; checked `git diff --check` and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/survey2.md` version 1.1 draft and `protocol/v5/study_overview.md` version 2.32 draft.
- **Results:** The overall X histogram remains required, with a separately labeled post-vaccination-symptom normal-days histogram and its own denominator. A zero spike and approximately flat positive tail are documented as predictions of a specific uniform-onset, fixed-recovery comparison model, not of vaccine safety in general. Symptom resolution is not assumed to equal full return to prior behavior and skills; direct normal-day answers remain separate from date-derived lags and from the locked unprompted narrative.
- **Next steps:** Convert the draft into screen-by-screen branching and a frozen statistical analysis plan, including recovery-duration uncertainty, day-count conventions, and sensitivity models; obtain IRB review before recruitment.

## 2026-10-01 — Retain the 90-day vaccination lookback and document its limit

- **What we did:** Confirmed the user's final choice to keep the existing 90-day vaccination-record and histogram window; reversed an in-progress expansion to all earlier vaccinations and added an explicit interpretation limit.
- **Command / executable:** Inspected v5 references with `rg`; edited with `apply_patch`; ran `git diff --check` and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.33 draft; `protocol/v5/survey2.md` remains version 1.1 draft.
- **Results:** The instrument still asks for the most recent vaccination within 90 days of the first definite change. Earlier vaccinations do not become a plotted visit anchor; their absence from the requested records is stated as a limitation, not evidence that no earlier vaccination occurred. The 15-day unprompted narrative remains unchanged. Checks passed; the partner-name scan found no matches.
- **Next steps:** In the statistical analysis plan, define the 0–90-day histogram denominator, outside-window reporting, and appropriate comparison model before analysis.

## 2026-10-01 — Add child age-quarter companion histograms

- **What we did:** Added the agreed descriptive comparator based on each child's 12-, 15-, or 18-month age milestone for the 12–18-completed-month subgroup; left the Survey 2 questions unchanged.
- **Command / executable:** Reviewed the existing calendar-quarter analysis, edited `study_overview.md` with `apply_patch`, and checked the resulting Markdown diff.
- **Outputs:** `protocol/v5/study_overview.md` version 2.34 draft.
- **Results:** The same children and date metrics used in paired vaccination plots will also have lags from a common child-specific age-quarter anchor. The plot is labeled descriptive, not a calibrated null or causal test; negative baseline-break lags remain visible.
- **Next steps:** Freeze exact subgroup and month-anniversary boundary conventions and the inferential null model in the statistical analysis plan before exposure-linked results are inspected.

## 2026-10-01 — Replace startup tasks with IRB completion checklist

- **What we did:** Converted the v5 startup list into ten stable, numbered remaining items with explicit closure criteria, separating scientific decisions, participant/records workflow, and submission/governance work.
- **Command / executable:** Compared `protocol/v5/task_list.md` with the overview's Section 12 and document guide; edited with `apply_patch`; checked the Markdown diff and confidential-partner-name scan.
- **Outputs:** `protocol/v5/task_list.md`.
- **Results:** Existing overview and survey drafts are recognized as the core design, while the analysis plan, eligibility rules, final instruments, operational procedures, consent, reviewer manual, privacy plan, partner arrangements, IRB package, and prelaunch testing remain open. R01 is identified as the next item to close.
- **Next steps:** Work through R01–R10 in order, logging each decision and updating the relevant document before checking an item complete.

## 2026-10-01 — Prespecify two overlapping short-lag windows

- **What we did:** Added days 0–2 and 0–5 as equally prespecified displays for both timing dates, made their overlap explicit, and added the 12-, 15-, and 18-month administration-age groups to the planned plots. Confirmed that vaccination lags, Onset 1 weekday, normal-day counts, calendar-quarter anchors, and child age-quarter anchors remain in the overview.
- **Command / executable:** Checked current schedule wording and the v5 analysis sections; edited `study_overview.md` and `task_list.md` with `apply_patch`; ran `git diff --check` and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.35 draft; updated `protocol/v5/task_list.md` R01.
- **Results:** No window will be selected post hoc as the preferred short lag; days 3–5 are shown separately so the incremental portion of 0–5 is visible. The two overlapping counts are not treated as independent confirmations. Whether either supports formal inference remains an open R01 decision pending a defensible null model and multiplicity rule.
- **Next steps:** Draft the statistical analysis plan with precise age-bin boundaries, denominator and reference-time definitions, both windows, calibrated-null feasibility, and simulation scenarios.

## 2026-10-01 — Make age-at-onset plots explicit

- **What we did:** Added separate records-based Onset 1 and Onset 2 age histograms alongside the existing Survey 1 reported-age display, plus a same-child distribution of actual age at the last documented vaccination.
- **Command / executable:** Reviewed v5 analysis text and primary research on prospective versus recalled onset timing; edited `study_overview.md` and `task_list.md` with `apply_patch`; ran `git diff --check` and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.36 draft; updated `protocol/v5/task_list.md` R01.
- **Results:** Planned figures mark 12-, 15-, and 18-month ages without treating a nominal age as an actual vaccination date. Smooth underlying age-specific onset is framed as a candidate null assumption, not a guaranteed shape of the observed selected or recalled-age histogram. Formal age-peak testing still requires prespecified bins, selection assumptions, calibration, and multiplicity rules.
- **Next steps:** Include age-at-onset plots and peak-model simulations in the R01 statistical analysis plan; keep parent-reported and reviewer-agreed ages distinct.

## 2026-10-01 — Frame v5 as a reusable data study

- **What we did:** Updated the overview and R01 to make collection, adjudication, privacy review, and release the first study's deliverables. Kept timing plots and simulated benchmarks as possible analyses the data paper can explain, with hypothesis-driven results reserved for a separate analysis paper.
- **Command / executable:** Edited `protocol/v5/study_overview.md` and `protocol/v5/task_list.md` with `apply_patch`; checked the diff and confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.37 draft; updated `protocol/v5/task_list.md` R01.
- **Results:** The approved public-use data are planned for release regardless of the observed timing pattern. Post-data analytic choices must be identified as exploratory; listing possible uses in the data paper does not turn them into confirmatory tests. No IRB approval or publication acceptance is implied.
- **Next steps:** Complete the R01 versioned data dictionary, construction/missingness rules, disclosure-risk criteria, and reproducible processing specification before enrollment.

## 2026-10-01 — Draft R01 data and suppression rules

- **What we did:** Recorded the decision to retain an unsafe-to-publish narrative or case row in the restricted dataset while withholding it from public release, with a suppression flag when a row is safe and otherwise safe aggregate counts. Drafted R01 data layers, required dictionary groups, provenance and missingness categories, case/visit construction, processing checks, and release package.
- **Command / executable:** Reviewed the current overview and both survey drafts; edited `data_specification.md`, `study_overview.md`, `document_guide.md`, and `task_list.md` with `apply_patch`; checked Markdown diff and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/data_specification.md` version 1.0 draft; `protocol/v5/study_overview.md` version 2.38 draft; updated document guide and R01 checklist.
- **Results:** The proposal preserves all submitted material under restricted controls while making public release conditional on consent, IRB approval, and case-specific disclosure-risk review. R01 remains open; no public data were released.
- **Next steps:** Finalize R02/R03/R06/R07 dependencies, machine-readable dictionary, processing code and test fixtures, then validate against fictitious edge cases before enrollment.

## 2026-10-03 — Evaluate scheduled-date and symptom-end timing displays

- **What we did:** Reviewed the proposal to compare onset lags from actual vaccination, reported end of post-vaccination symptoms, and an ideal CDC schedule date against the current v5 timing definitions and CDC schedule guidance.
- **Command / executable:** Read `protocol/v5/study_overview.md` and `data_specification.md`; checked CDC child schedule and catch-up guidance using primary-source web search. No protocol text was changed.
- **Outputs:** Methodological recommendation in this discussion; no new analysis or data output.
- **Results:** Actual-dose and symptom-end lags are distinct descriptive quantities. The latter is undefined without a dated symptom episode and may be negative for Onset 1 or if symptoms continue after the definite change. Nominal CDC schedule dates are useful age-anchor sensitivity displays, but actual and schedule-anchored lag histograms need not match under no vaccine effect when real administration dates differ from nominal dates or the last eligible visit changes.
- **Next steps:** Clarify whether the proposed symptom-end lag refers to Onset 1 or Onset 2, and decide whether to add it as a candidate descriptive display. Treat any modeled no-effect benchmark as an explicit simulation with age, scheduling variation, and the same eligibility/90-day rules rather than assuming the ideal schedule is a null control.

## 2026-10-03 — Define post-vaccination return to observed baseline

- **What we did:** Tightened the post-disclosure Survey 2 question so “normal” means return to the child's directly observed pre-vaccination behavior and skills, not merely resolution of acute symptoms. Kept the cause-neutral pre-disclosure X field separate.
- **Command / executable:** Edited `protocol/v5/survey2.md`, `study_overview.md`, and `data_specification.md` with `apply_patch`; checked the Markdown diff and confidential-partner-name scan.
- **Outputs:** `survey2.md` version 1.2 draft, `study_overview.md` version 2.39 draft, and `data_specification.md` version 1.1 draft.
- **Results:** The intended descriptive field counts consecutive complete days back at the pre-vaccination behavior-and-skill baseline immediately before Onset 2. No return, less-than-one-day return, earlier-only return, uncertain pre-vaccination baseline, unknown response, and no post-vaccination symptoms remain distinguishable. The symptom-end date remains a separate measure and is not treated as return to baseline.
- **Next steps:** In R03/R06, finalize exact respondent screen wording, branching, and reviewer coding for repeated normal/uncertain periods and test those paths with fictitious cases before enrollment.

## 2026-10-03 — Add six nonactual-date sensitivity anchors

- **What we did:** Added candidate fixed 30-, 60-, and 90-day grids and nominal CDC-schedule anchors shifted by 0, 7, or 14 days earlier for a later descriptive analysis, while preserving actual-vaccination dates as the exposure-timing fields.
- **Command / executable:** Reviewed current v5 comparator definitions and CDC schedule guidance; edited `protocol/v5/study_overview.md` and `task_list.md` with `apply_patch`; checked the diff and confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.40 draft; updated R01 examples in `task_list.md`.
- **Results:** The proposed fixed-grid origin is child birthdate, with the most recent anchor on or before Onset 2 and the same 90-day convention. The six plots are related sensitivity displays, not independent controls; different grid lengths have different supports. A flat pseudo-anchor histogram or mismatch with the actual-vaccination histogram is not automatically the no-effect expectation or evidence of causation.
- **Next steps:** A later analysis plan must finalize historical schedule versions, nominal visit/product mapping, eligible denominators, grid-origin choice, binning/phase display, and any explicit no-effect simulation before interpreting observed contrasts.

## 2026-10-03 — Clarify the fixed-grid null expectation

- **What we did:** Corrected the wording for fixed 30/60/90-day anchors to state the simple uniform-phase expectation explicitly and identify the limited conditions that can break it without implying a calendar-day effect on autism.
- **Command / executable:** Reviewed the grid definition, CDC developmental-screening guidance, and primary research on parent-reported onset timing; edited `protocol/v5/study_overview.md` with `apply_patch`; checked the diff and confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.41 draft.
- **Results:** Under constant daily onset hazard, accurate dates, phase-independent inclusion, and complete cycles, fixed-grid phases are uniform. A broad smooth age curve should leave the 30-day phase approximately uniform; boundaries, date heaping, age-linked recognition, and study selection can create departures. This does not turn the grid into a calibrated no-effect distribution for actual-vaccination lags.
- **Next steps:** If used in the later analysis paper, quantify the expected phase distribution under the actual age window, date precision, and selection process rather than assuming exact flatness.

## 2026-10-03 — Consolidate the core A/B/C measures

- **What we did:** Recorded the user's core summary as age at onset, A (actual vaccination-to-onset days), B (complete normal days), and C (reference-to-onset days), with calendar-quarter start and unshifted nominal CDC schedule as the two core references. Kept the other grids and shifted schedules as optional sensitivity displays. Added a remained-normal option to Survey 2 so a child who maintained baseline after vaccination is not coded as failing to return.
- **Command / executable:** Reviewed the current overview, Survey 2, and R01 draft; edited with `apply_patch`; ran `git diff --check` and the confidential-partner-name scan.
- **Outputs:** `protocol/v5/study_overview.md` version 2.42 draft; `data_specification.md` version 1.2 draft; `survey2.md` version 1.3 draft.
- **Results:** Age, A, and C preserve separate Onset 1/Onset 2 values, and Onset 1 remains the preferred lead display. B retains the previously agreed consecutive complete days at the observed pre-vaccination baseline immediately before Onset 2, with maintained/returned/unknown sequence status. CDC nominal-age choices and historical versions remain implementation details to specify; no formal test was added to the data paper.
- **Next steps:** Finalize the historical nominal schedule and field map in the later analysis/R03 implementation, reconcile normal-period edge cases in R06, and complete the outstanding R01 dependencies before enrollment.

## 2026-10-03 — Clarify B as the adjacent consecutive normal-day count

- **What we did:** Updated Survey 2, the overview, and R01 to define B as consecutive complete normal days immediately before Onset 2, retaining the user's explicit pre-vaccination behavior-and-skill baseline definition. Removed the vaccination-date start/truncation from the count; preserved the separate cause-neutral earlier-period questions.
- **Command / executable:** Edited the three drafts with `apply_patch`; checked `git diff --check`, document wording, and the confidential-partner-name scan.
- **Outputs:** `study_overview.md` version 2.43 draft; `survey2.md` version 1.4 draft; `data_specification.md` version 1.3 draft.
- **Results:** B can include pre-vaccination days and exceed A. Exact, approximate, lower-bound, unknown, and baseline-unestablished answers remain distinct; disconnected periods are not summed and symptom resolution is not substituted for developmental baseline. Children without reported vaccination retain a separately flagged analogous prior-usual-baseline count. No causal conclusion is implied.
- **Next steps:** Finalize screen routing and reviewer coding for these statuses in R03/R06 before enrollment.

## 2026-10-03 — Add the observed boundary for B

- **What we did:** Added a Survey 2 follow-up describing the observation that stops the backward normal-day count, with free text before symptom categories, date precision, observer, and unknown-boundary options; synchronized overview and R01.
- **Command / executable:** Reviewed current drafts and shared instructions; edited with `apply_patch`; ran `git diff --check` and confidential-name scan.
- **Outputs:** `survey2.md` 1.5 draft; `study_overview.md` 2.44 draft; `data_specification.md` 1.4 draft.
- **Results:** Vaccination alone cannot stop B; observed symptoms or inability to assess baseline are recorded without causal attribution. Zero, unknown, and lower bounds remain separate.
- **Next steps:** Test boundary, zero, and unknown paths in the final R03 instrument and R06 reviewer manual.

## 2026-10-03 — Adopt single ONSET and vaccination-window normal-day count

- **What we did:** Recorded the user's revised single parent-first-notice ONSET endpoint and B as all complete normal days between vaccination and ONSET, including disconnected periods; replaced the core overview table and Survey 2 B prompts.
- **Command / executable:** Read shared instructions and current drafts; edited with `apply_patch`; checked whitespace and confidential-name scan.
- **Outputs:** Overview 2.45, Survey 2 1.6, R01 specification 1.5 drafts.
- **Results:** Known counts obey 0 ≤ B ≤ A; unknown and no-anchor cases remain distinct. Calendar-day counting excludes ONSET day and counts vaccination day only if normal throughout. Earlier two-onset and backward-count details are explicitly superseded, not silently operative.
- **Next steps:** Reconcile the remaining legacy overview, reviewer, dictionary, and instrument wording with the controlling amendment before deployment.

## 2026-10-03 — Include B's normal periods in the prompted narrative

- **What we did:** Made Survey 2's vaccination-to-ONSET narrative explicitly cover all normal periods counted in B, including disconnected stretches, alongside non-normal, unassessable, and unremembered periods; added R01 provenance and reconciliation rules.
- **Command / executable:** Read shared instructions and current drafts; edited with `apply_patch`; ran whitespace and confidential-name checks.
- **Outputs:** Survey 2 1.7 draft; data specification 1.6 draft.
- **Results:** Parents describe observed baseline behavior/skills, dates or duration, and observers for the normal periods. B can be checked against the timeline without overwriting raw answers or inferring normal days from silence. The locked 15-day narrative remains separate.
- **Next steps:** Reconcile legacy two-onset wording and implement timeline/count discrepancy handling in R03/R06 before deployment.

## 2026-10-03 — Reconcile active v5 drafts and expand the tracked R01 checklist

- **What we did:** Removed superseded two-onset endpoints, negative baseline-departure lag rules, transition-gap displays, backward-count B definitions, and the separate X-histogram requirement from active v5 drafts. Retained earlier illness/uncertainty and return-to-normal observations as timeline context. Reconciled reviewer rules, evidence fields, plots and construction rules to one parent-first-notice ONSET, A/B/C, and 0 ≤ B ≤ A.
- **Command / executable:** Read shared instructions and current v5 files; edited with `apply_patch`; compared saved files with reviewed revisions; ran `git diff --check`, stale-definition scans and confidential-recruitment-name checks across `protocol/v5`.
- **Outputs:** `study_overview.md` 2.46 draft; `survey2.md` 1.8 draft; `data_specification.md` 1.7 draft; updated `task_list.md` and `document_guide.md`.
- **Results:** No superseded onset labels or old B instructions remain in active v5 drafts. Original first-notice report, reviewer assessments, accepted date, date precision and separate documentation date remain distinct. Neutral intake, locked 15-day narrative, confidence-only invitation waves, 100-record administrative target, payment rules, three independent one-pass reviews and controlled retention/public-release safeguards are preserved. R01 has explicit completed core/cleanup items and eight open implementation sub-items mapped to R02/R03/R05/R06/R07/R09/R10; it is not marked complete.
- **Next steps:** Complete R01.1–R01.8 as the field map/dictionary, eligibility, evidence/reviewer manual, normal-day edge cases, nominal-reference construction, governance and processing/tests are finalized. Historical decision entries in this log remain archival, not active study instructions.

## 2026-10-04 — Finalization Q1: preserve unknown-day counts and B bounds

- **What we did:** Recorded the user's approval to retain definitely normal, definitely non-normal, and unknown/unassessable counts in the vaccination-to-ONSET window; added respondent prompts and construction rules.
- **Command / executable:** Read shared instructions and current drafts; edited with `apply_patch`; ran whitespace and confidential-name checks.
- **Outputs:** Survey 2 1.9 and data specification 1.8 drafts; updated task list with Q1 marked agreed.
- **Results:** Reconciled N + D + U = A; with U > 0, B ranges from N to N + U rather than treating N as exact. Unknown/unassessable days are not abnormal. Raw counts and conflicts remain auditable; approximate values stay approximate.
- **Next steps:** Confirm partial-day handling, then complete the remaining R01.4 decisions and implementation tests. R01 is still open.

## 2026-10-04 — Finalization Q2: complete days and partial returns

- **What we did:** Recorded the user's approval that B counts complete normal calendar days only, with partial-day returns retained separately.
- **Command / executable:** Read current versions and shared instructions; edited with `apply_patch`; ran whitespace and confidential-name checks.
- **Outputs:** Survey 2 1.10 draft; data specification 1.9 draft; Q2 marked agreed in the task list.
- **Results:** No fractional addition or rounding into B. Definite non-normal portions prevent a complete-day count; genuinely unassessable periods remain uncertain. B = 0 does not imply no brief return to baseline.
- **Next steps:** Settle approximate-date handling and continue the remaining finalization questions; R01 remains open.
