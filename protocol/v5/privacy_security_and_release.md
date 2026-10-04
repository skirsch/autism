# Data protection retention and release plan

**Version:** 1.1 draft
**Date:** October 4, 2026
**Status:** Required controls and proposed procedures; not a platform security attestation

This plan covers linked parent surveys, identifiable child source materials, review, correspondence, payment and public release. The study is not anonymous. Controls below must be documented, configured and tested; platform branding and encryption claims alone do not establish compliance.

## Data flow and access

| Stage | Data and system | Authorized role | Restriction |
| --- | --- | --- | --- |
| Partner invitations/Survey 1 | Partner host; individual screen answers and permission retained under partner notice | Authorized partner administrators; study does not receive individual answers | Secure authorized email-only handoff with administrative permission/source/batch metadata; aggregate counts if available |
| Study referrals | Authorized email, permission attestation and study-assigned ID/crosswalk | Authorized study contact staff | Research consent before Survey 2; no public contacts; no invented partner-answer export |
| Survey 2 | Intended IPAK EDU environment; consent, locked narrative and later answers | IPAK custodian; authorized research/operations roles | No event prompts before narrative lock; no third-party research reuse of raw data |
| Source evidence | IPAK-designated restricted file store, distinct from public files | Custodian and authorized three reviewers; packet preparer as needed | Encrypted receipt/storage/backups; audit access; originals immutable |
| Contacts/payments | Separate contact/entitlement stores and restricted crosswalk | Steve as contact; named backup/payment staff/custodian as authorized | No contacts in analytic export; vendor minimum necessary data |
| Review | Isolated per-reviewer workspaces | Each reviewer sees packet and own judgments only before lock | No other review access/discussion; no interim lag plots for selection/review |
| Processing | Versioned coded build in approved environment | Authorized processor/PI | No production data in public Git repository or personal tooling accounts |
| Redaction/release | Restricted staging copy | Redaction preparer and two authorized privacy checkers | At least one checker not preparer; full package reviewed |
| Public deposit | Zenodo, after permissions/signoffs | Steve release owner; confirmed backup | Approved coded files/redacted narratives/docs/code only |

PI retains overall oversight; IPAK must designate and accept custody responsibility. A funder affiliation grants no data access by itself. Each grant is person/role-specific, time-limited as appropriate and auditable. Contractors, cloud providers and additional researchers need approved terms and scope. Partners keep their original membership/clinical lists; these are not imported as the study cohort.

## Technical confirmation sheet

Partner-held individual screen records have their own disclosed retention policy; the study's 20-year/public-release terms apply only to authorized study-held data. Obtain the IRB determination of the actual partner role rather than assuming the screen is outside research. Minimize records-request selection queues to permission, reported eligibility and original A4 confidence; do not expose vaccination/timing or reviewer outcomes to selection staff.

Before deployment, obtain actual system names/locations, vendor/subprocessor/data-region details, data-flow diagram, contracts and these confirmations from IPAK and any Survey 1 partner:

- Encryption in transit and at rest from receipt, including backups, viewing copies and temporary exports; algorithms/configuration and accountable key custody/recovery. Keys are not embedded in scripts, source files or public repositories. Three researchers personally holding a key is not by itself a complete security plan.
- Named authorized roles, least-privilege grants, multifactor authentication, no shared reviewer login, access logging/review, removal on role departure and continuity if a key holder is unavailable.
- Tested save/lock/version behavior, reviewer isolation, upload scanning/safe preview, export restrictions, recovery and secure transfer. Source backups and crosswalk backups have controlled restoration paths.
- Necessary IP/device/security/session metadata, purposes, access and retention; minimize what is not required. Disable third-party advertising, profiling, session replay, device fingerprinting and unrelated analytics; verify embedded components and access logs rather than assume settings apply everywhere.
- Backup schedule, recovery objectives, restore testing, incident contact and escalation, vendor data-deletion/copy handling, breach notification decision process and key rotation/recovery.
- Consent/contact tokens are nonpublic; forwarded links, shared devices and expired sessions do not silently expose another family's answers. Security timeouts are independent of research response-window disposition.

Until confirmed, each item is pending. No assertion of HIPAA compliance, legal de-identification or exemption is made by this draft. Determine applicable law, provider authorization requirements and cross-border rules with the reviewing institution.

## Retention and stopping participation

Retain all authorized submitted answers, partials, source files, dated evidence, contacts/correspondence, reviews, mapping/audit, regulatory records and analytic builds for 20 years after documented study closure, or longer if required. The earlier 18-month destruction instruction is withdrawn. Closure is the PI/institution's dated regulatory closure milestone, not a participant upload or the first publication. Record the actual retention end date, owner and applicable holds; do not extend or shorten it silently.

Retaining already collected data does not authorize new collection after a participant stops. Log stop/contact preferences and terminate future research invitations/requests; separately handle owed payment, an initiated correction or necessary privacy/legal communication. The proposed nondeletion-after-submission policy requires IRB and legal review and is not justified by an inability to locate linked data. Enforce approved permissions by consent version; submissions outside authorized consent scope are quarantined for institutional direction, not automatically released.

At retention end, the custodian and PI review legal/IRB holds, inventory active stores/backups/vendor copies/derived viewing copies, authorize secure destruction or required continued retention, verify completion and retain an appropriate destruction certificate under institutional policy. Publicly downloaded datasets cannot be guaranteed destroyed after 20 years; consent explicitly states this. Restricted retention and continued public availability are distinct.

## Independent controlled re-review

Applicants submit identity, qualifications, research purpose, requested minimum materials, security environment, conflicts, training and applicable ethics approvals. The PI/custodian and relevant IRB approve adding personnel/protocol access when required; an IRB approval alone does not configure access. Execute confidentiality/data-use terms: no re-identification/contact, redistribution, uncontrolled downloads or publication of source files; incident reporting; use only within approved scope; return/destruction at authorized access end. Prefer a secure viewing environment with audit logs. Record decisions, scope, time period and access termination. Denials use privacy/security/permission criteria, not anticipated findings. Never promise universal access to all uploads.

## Redaction and disclosure-risk review

Public release uses a different random case ID. Remove contacts, absolute dates, birth year/date, filenames/storage pointers, item IDs, payment IDs, identifying notes, metadata and hidden file content. Redact names/initials, specific clinics/schools/locations, other people's information, exact calendar anecdotes and distinctive linked details. Preserve scientifically relevant sequence and relative timing when safe. The original remains restricted; never fabricate a replacement narrative.

Review the full package jointly: exact derived age, A/B/C, weekday, rare products/conditions, country, source and rich narratives may identify a child when combined or linked to a public account. A calendar-quarter lag plus weekday or external event description can constrain dates; removal of an explicit date is not sufficient. Check file metadata, directory/archive names and documentation examples as well as rows.

Proposed review standard is conservative case-by-case reasonable recognition/linkage risk, not a numerical guarantee of anonymity. Do not invent an approved k-anonymity threshold or assert that any minimum cell count makes a detailed narrative safe. First generalize/remove risky fields; if the narrative cannot be made sufficiently safe, withhold it and retain the restricted original. If the coded row remains unsafe, withhold it too and publish only safe aggregate suppression counts. Suppress identifying combinations and small aggregate cells where needed, including complementary totals that could reveal a suppressed value. Document actual thresholds/decisions approved by the privacy reviewers/IRB before release. Never make suppression dependent on vaccine timing or a favorable conclusion.

Two authorized people sign off on each proposed package/correction, at least one not its redaction preparer. Both inspect actual narratives, coded tables, metadata, derived fields and combined/linkage risk. Record identities, training, package/checksum, issues, mitigations and dated approvals. Any unresolved concern blocks the affected material. Scientific votes do not supply privacy approval. Reviewer A/B/C labels are stable coded roles, not guaranteed anonymous identities.

## Release and corrections

Release the approved public dataset/documentation within 90 calendar days after the review dataset is finalized. Record that milestone after locks and accepted-value construction; do not delay it for journal prospects or timing patterns. Complete consent/licensing, technical validation and privacy approvals first. If those prerequisites block the deadline, log reason, responsible role and revised target without resetting the original clock or posting unsafe files.

Steve owns the Zenodo deposit and subsequent maintenance; designate an authorized team-member backup and verify account/security/continuity before release. Public data/documentation use CC BY 4.0 only to the extent rights/participant permission allow; study-authored code uses MIT with holder/third-party notices confirmed. Neither licenses restricted evidence or the whole existing repository. Release manifest lists code/dictionary/build versions, included files/checksums, licenses, denominator/precision limitations, suppressions and approvals. Dataset attribution names the resource, not parents.

Correct through a new version with a nonidentifying change log and repeated validation/signoff, not a silent overwrite. Preserve restricted provenance and version links. Privacy incidents receive prompt containment/repository restriction requests where possible, not delay until a scheduled correction. Downloaded copies may remain.

## Incident procedure and responsibilities

Anyone detecting lost credentials, unintended sharing, participant-identifying public text, unauthorized access or malware notifies the confirmed IPAK incident contact and PI promptly. Stop affected transfers/release, restrict access/links where possible, preserve logs/evidence in restricted storage, and coordinate vendor containment/key revocation. Custodian leads technical assessment; PI/institution determine applicable IRB/legal/participant notification duties and deadlines. Do not invent deadlines or make a blanket promise of no disclosure. Steve handles authorized participant communications; rights concerns go to the independent IRB contact. Record discovery, affected scope/versions, actions, notifications, recovery and prevention. Test a fictitious incident before launch and before public deposit.

This data-resource study has no emergency clinical intervention. For urgent health/safety concerns advise ordinary emergency/local clinical services, not a study diagnosis. Document unexpected research distress/privacy events under the confirmed institutional reporting procedure.
