# Relevant documents

Start with [submission_checklist.md](submission_checklist.md) for the assembled current package and unresolved external confirmations. [irb_application.md](irb_application.md) follows the supplied IPAK Form 1/Form 2 structure; it is not signed/submitted. Twelve supporting operational drafts were added October 4, 2026: eligibility/construction, typed dictionary, screen map, consent/disclosure, recruitment/payment, records review, privacy/security/release, governance, application, prior-feedback responses, submission index and validation plan. All remain subject to institutional review and implementation verification.

Run local document/reference checks with `pwsh -NoProfile -File protocol/v5/validation/validate_drafts.ps1` from the repository root. This read-only helper checks local Markdown links and fictitious calendar/count/majority examples; it is not a production dataset pipeline or live survey/security test.

## study_overview.md
Controlling overview: one parent-first-notice ONSET date; A vaccination-to-ONSET days; B total complete normal days in that window, including disconnected periods; C calendar-quarter and nominal CDC-reference lags.

## survey1.md
Draft of the partner's two-question possible-sudden-onset/contact-interest screen. The partner keeps individual answers and transfers only authorized emails with administrative metadata. All authorized possible-case referrals may complete Survey 2; records-confidence is collected there and used only for later supporting-material request phases.

## survey2.md
Draft of the one-question-at-a-time follow-up instrument, with a locked unprompted narrative before staged disclosure and structured records questions. Requires IRB approval and implementation testing.

## data_specification.md
Draft R01 field, provenance, construction, missingness, technical-validation, and public-versus-restricted release specification. It includes the rule for withholding a narrative or case row that cannot be safely de-identified while retaining the restricted original and safe aggregate counts. It is not an approved public-release plan; R02, R03, R06, R07, and IRB/consent decisions remain dependencies.


## IRB feedback document
in irb_submission/feedback

this has one document of initial feedback to incorporate into our proposal

## IRB submission form (Part B/Form 2/Proposal
in "IPAK IRB forms" directory

The IRB proposal should be structured this way.



## task_list.md
Master checklist for R01–R10, including R01's completed core decisions and outstanding dictionary, eligibility, reviewer, normal-day coding, reference-construction, release/security, processing/test, and consistency-review dependencies.

## process/work_log.md
Dated decision and verification history, including superseded design choices. Historical entries are not active protocol instructions.

