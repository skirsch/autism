# Validation fixtures and prelaunch acceptance plan

**Version:** 1.2 draft
**Date:** October 4, 2026
**Status:** Test plan with fictitious cases; live platform and production pipeline tests not yet performed

Use no actual families or identifying documents in testing. This plan tests procedures, not a vaccine hypothesis or statistical effect. Record tester/date, approved version, environment, fictitious input, actual output, expected output, pass/fail, issue and rerun proof. Writing an expected result does not count as passing a test.

## Calendar construction and review fixtures

| ID | Fictitious input | Required result |
| --- | --- | --- |
| F01 | ONSET and vaccination both 2024-07-01 | A=0; B=0 under complete-day convention; intraday order unknown unless supplied |
| F02 | ONSET 2024-07-01; administration 2024-04-02 | Vaccination lag 90 eligible; no maximum vaccination lookback |
| F03 | Same ONSET; administration 2024-04-01 | Vaccination lag 91 remains eligible for A/B and minimum/target if other criteria met |
| F04 | Administration 2024-07-02 | Future relative to ONSET; no eligible anchor |
| F05 | Quarter reference for 2024-03-31 | 2024-01-01, C=90; quarter reference is not actual vaccination |
| F06 | Quarter reference for 2024-09-30 | 2024-07-01, C=91 allowed; no false 90-day quarter truncation |
| F07 | Birth 2023-01-31 | 2-month nominal 2023-03-31, 4-month 2023-05-31, 6-month 2023-07-31; original date arithmetic, not cumulative clamped months |
| F08 | Birth 2024-08-31; add 6 months | Nominal date 2025-02-28; no nonexistent February 31 |
| F09 | Birth 2024-02-29; add 12 months | 2025-02-28; leap handling explicit |
| F10 | Birth 2023-01-01; ONSET 2023-06-30 / 2023-07-01 | 5 completed months out / 6 in |
| F11 | Same birth; ONSET 2025-01-31 / 2025-02-01 | 24 completed months in / 25 out |
| F12 | Birth 2023-01-01; ONSET 2024-12-31 | Latest 18-month point 2024-07-01 is >90 days earlier; no nominal anchor; do not add a 21-month point |
| F13 | Actual visit at 12 months with multiple products | One visit/child anchor, repeated product rows; no extra child count |
| F14 | Exact A=20; N=5,D=10,U=5 | B bounds 5–10; lower bound not exact B=5; U not abnormal |
| F15 | Exact A=3; one partial-day return and two unknown days | No rounding partial day into B; N=0,D=1,U=2; B bounds 0–2, not proven exact zero |
| F16 | Parent B=12 with exact A=10 | Preserve raw discrepancy, clarify; no clamping to 10 |
| F17 | No known vaccination on/before ONSET; qualifying vaccine-free well visit | Well-to-ONSET defined as appropriate; A/B not applicable, not zero |
| F18 | Never-vaccinated parent report; no visit; dated onset item submitted | Retain no-anchor/parent-never label; full-payment eligible with complete tasks; not target-complete |
| F19 | Visit document supplied, onset not corroborated | Administrative count may qualify; scientific evidence-supported tier does not automatically qualify |
| F20 | Review dates June 1 / June 1 / June 3 | Majority date June 1; two agreement; no averaging |
| F21 | Reviews exact B=5 / lower-bound B>=5 / unknown | No numeric/status majority; do not accept exact B=5 |
| F22 | Independent majority bounds lower June 4, upper June 2 | Preserve bound votes; constructed interval inconsistent/unresolved |
| F23 | Evidence dated June 3 says first noticed June 1, parent agrees | Preserve both dates/certainty; reviewer assesses content support, no forced ONSET June 3 |
| F24 | After-only video June 3, no first-notice content | Supports earliest documented presence, not automatic first notice |
| F25 | Window contains parent-reported uncertainty about later vaccination | Retain selected visit/history conflict; no confirmed-most-recent label or assumed vaccine-free group |
| F26 | Two parents confirmed same child through authorized linkage | Keep both original accounts; one target/plot child; response funnels two; honor separate prior payment promises |
| F27 | Same birthdate but no confirmed common-child link | Suspected/unresolved duplicate, not automatic merge |
| F28 | Three majority fields individually agree but B's window differs from accepted A | Flag inconsistent-window B; no validated B/A pair |
| F29 | ONSET reported only as month | Store range/precision; no invented midpoint/exact weekday or definite exact-lag classification |
| F30 | Survey 2 receipt-time reported age eligible, reviewer later out of range | Preserve administrative target/payment if independently complete; scientific cohort flag out of range |
| F31 | Authorized possible-case referral; low date confidence or probable record unavailability | Receives Survey 2; best estimate/unknown retained; no confidence access gate |
| F32 | Partner handoff contains individual screen answers or no permission attestation | Quarantine/resolve transfer authority; do not import as approved research rows |
| F33 | Survey 2 complete; records phase not opened | Completed survey retained; no automatic records request/upload or materials payment; request state separate |
| F34 | A4 recorded before disclosure; exposure answers later present | Selection queue exports permission/reported eligibility/original confidence only, not exposure/timing/reviewer fields |
| F35 | Most recent vaccination 200 days before ONSET; B partly unknown | A=200 eligible; retain B bounds/unknown, not zero; no long-lag exclusion from target/minimum if other criteria met |
| F36 | Most recent vaccination >90 days earlier; vaccine-free regular well visit 20 days earlier; no later vaccination established | Both vaccination A/B and independent well lag=20 may apply; once per child in each plot |
| F37 | Vaccine-free regular well visit 90 / 91 days before ONSET, with no vaccination in prior 90 days | Well anchor eligible at 90, not 91; vaccination lookback and nominal reference rules remain distinct |

## Survey and custody tests

- A1 is first substantive question after affirmative consent. Verify HTML titles, previews, help, notifications and invitation text as well as visible questions contain no named candidate events before lock.
- Declining initial consent collects no research answers. Verify any necessary operational/security metadata separately.
- Save A1; verify saved partial persists with permission, then Confirm locks server-side. Try back navigation/resume/direct endpoint requests; original cannot be overwritten after disclosure.
- A2/A3 can answer unknown and describe an uncertain period older than 15/90 days. No forced date or named cause.
- B1 explicit decline and departed-without-choice are different exported states. No later event questions/upload appear without affirmative continuation/authorization.
- No-vaccination/no-well and unsure-history paths reach applicable questions without forcing dates/A/B zero. Routine-plan parents still receive spacing question.
- Each date can be exact/range/week/month/unknown, with bounds and verification distinct. Raw B>A/category conflicts are retained, not rejected/clamped out of the exported data.
- Saved partials versus unsent text, security timeout, operational day-14 closure and late resumption are distinguishable. Stop contact blocks reminders, not an owed payment.
- Partner handoff contains only authorized emails and administrative source/batch/permission attestations; no individual screen answer export or unauthorized contact lists. Aggregate counts are availability-labeled. Partner retention is not mislabeled as study retention. Forwarded tokens cannot expose existing submissions.
- Evidence inventory preserves bytes/hash, creation/described-event dates, parent claim and amendments; malware-safe handling/preview, backup restore and restricted export/access are tested.
- Each reviewer cannot view either other's forms before all locks. Shared login or administrator-visible review results are documented and access-limited, not called blinding.
- Consent copy available in approved form; keyboard/date-entry/screen-reader behavior and mobile rendering tested. English-only limitation is explicit.

## Operations fixtures

At C=20, I_m=100, C_m=20, requested next batch is `ceil(1.2*80/0.2)=480`, capped to available pool. With zero mature yield, fallback batch is 100 or remainder, not division by zero. I_m is supporting-material requests, not Survey 2 invitations. Open records-request waves do not enter the mature denominator. Confidence pools exhaust in order; seeded membership is reproducible from archived input/version without exposure fields. Count confirmed child duplicates once and separately log prior submitted/attributed counts.

At first checkpoint below 100, tier rises $25→$50, with $25 top-up owed for equivalent previously completed work; no-anchor full completions also qualify. Subsequent shortfall checkpoints activate $75/$100, never above $100. C>=100 stops increases/new records-request batches, not confidence-free Survey 2 access within its approved recruitment window or retention/payment for already requested work. Late scientific exclusion does not replace a child to obtain an analytic target. Good-faith incomplete materials remain $25. Failed delivery stays unpaid; duplicate exceptions/prior promises are auditable.

## Public build and incident tests

Build proposed public outputs from a frozen fictitious raw export and locks. Check reproducibility, schemas/missingness, exact majority/status, ranges/ages/anchors, immutable source/correction provenance and separate target/payment/scientific flags. Reject prohibited columns and identifying metadata. Redaction tests include a rare product/age/country/narrative combination, an absolute date disguised in a filename, third-party details and a case identifiable despite no name. Demonstrate narrative-only and row suppression with safe aggregate counts; no suppression depends on lag direction. Verify two-person signoffs, manifest/checksums, license notices and versioned correction. Test a fictitious accidental disclosure with immediate containment/escalation and no identifying public change log.

## What has and has not been verified

Local check executed October 4, 2026: `pwsh -NoProfile -File protocol/v5/validation/validate_drafts.ps1` passed 128 document/reference checks, including 69 relative Markdown links, with zero failures at the final assembled-package check. The arithmetic/agreement checks cover a subset of the fictitious fixtures; unimplemented workflow fixtures are not reported as passed. Subsequent edits require rerunning this helper and the separate whitespace/confidential-name scans.

Local Markdown link/whitespace/confidential-name and consistency scans may be run now and recorded in the work log. A local reference-check helper, if supplied, tests specified arithmetic/rules against fictitious values only; it is not the production raw-export adapter or a platform security test. Actual platform, reviewer calibration, payment vendor, backup/incident, redaction and approved live-version tests remain pending. R10 closes only after those pass and the PI/custodian record launch signoff.
