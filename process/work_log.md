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
