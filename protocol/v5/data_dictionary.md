# Data dictionary and export contract

**Version:** 1.3 draft
**Date:** October 4, 2026
**Status:** Proposed logical schema; platform export names and machine-readable implementation remain to be tested

This dictionary maps the v5 instruments and evidence workflow to research records. Read with [survey_screen_map.md](survey_screen_map.md), [eligibility_and_construction.md](eligibility_and_construction.md) and [records_review_manual.md](records_review_manual.md). It defines a logical export contract, not an assertion that IPAK implements it.

## Shared types and statuses

`id` = randomly assigned string; `date` = local calendar ISO date; `timestamp` = UTC ISO timestamp; `int` = integer; `number` = numeric with unit; `text` = original Unicode text; `enum` = one listed value; `set` = list of listed values; `bool` = true/false only when known. Nullable values always carry status. No negative sentinel in a date/count field.

Every answer exports `value`, `status`, `screen_id`, `submission_id`, `instrument_version`, `saved_at`. Status enum is `answered`, `unknown`, `not_supplied`, `branch_not_asked`, `not_reached`, `unusable`, `review_unresolved`, `not_applicable`, `public_withheld`. A substantive No and numeric zero have `answered` status. Unknown values are null, not zero/empty-string imputations. Retain raw text and raw choices separately from standardized codes and amendments.

Every date object expands to `value`, `precision` (`exact`, `approximate_day`, `week`, `month`, `range`, `unknown`), `lower`, `upper`, `bound_status`, `uncertainty_days`, `verification` (`not_assessed`, `parent_only`, `corroborated_exact`, `corroborated_range`, `conflicting`, `unusable`), `evidence_ids`, `origin`, `conflict_flag`. Width is upper minus lower when both are known. Every count object expands to `value`, `precision` (`exact`, `approximate`, `lower_bound`, `range`, `unknown`, `baseline_unestablished`, `not_applicable`), `lower`, `upper`, `status`, `origin`, `evidence_ids`, `conflict_flag`.

P = proposed public after permission and risk review; R = restricted; A = safe aggregate only; T = redacted text only. P is not automatic permission. All absolute dates, timestamps, internal IDs, contacts, raw narratives, source pointers, identifying free text and payment identifiers remain R. Public row IDs are freshly random, linked by a restricted crosswalk.

## Entities and keys

| Entity | Row and key | Relationships | Release |
| --- | --- | --- | --- |
| `sources` | one source code | batches; restricted identity agreement | A or risk-reviewed generalized code |
| `batches` | one `batch_id` and stage (`partner_screen`, `s2_invitation`, `records_request`) | source; invitations/requests; stage-specific checkpoint calculations | A |
| `contacts` | one `respondent_id` | contact permission, child/submission links | R |
| `submissions` | one `submission_id` per study response | authorized referral; study invitation; respondent; confirmed child; no raw partner response | R IDs; safe derived fields P |
| `screen_events` | one event ID | submission; screen; state; timestamp | R; stage counts A |
| `child_cases` | one `child_id` | all confirmed duplicate submissions | P with new ID |
| `timeline_periods` | one period ID | submission/child; narrative source | R; safe relative summary P |
| `visits` and `visit_products` | visit ID; product-row ID | child; reporting submission; evidence | R dates/IDs; coded derived P |
| `evidence_items` | one `evidence_id` | child; submission; restricted file | R; safe tier/usability P |
| `reviews` | one reviewer ID + child + version | evidence citations; locked assessment | R identity/dates; safe coded P |
| `accepted_values` | one child + field + build version | exact-majority provenance | P safe derivations |
| `payments` | one transaction/entitlement ID | restricted payee/child/submission | R; safe totals A |
| `release_decisions` | one object + version | approvals, suppression, redactions | R audit; safe flags P |

## Partner referrals and aggregate screen counts — no individual answer export

| Name | Type / allowed values | Source | Release |
| --- | --- | --- | --- |
| `referral_id`, `source_code`, `referral_batch_id` | study-assigned ID; restricted source/batch IDs | authorized email handoff | R |
| `referral_email`, `contact_validation` | email; usable/invalid/correction_needed | permitted contact transfer | R |
| `transfer_permission_attestation`, `permission_notice_version` | partner administrative attestation/version/reference; no raw screening answer | confirmed partner audit | R |
| `partner_aggregate_counts` | attempted/delivered/started/completed/possible_yes/no/unsure/authorized_referred counts with available/missing status | aggregate partner report | A |

Partner individual screening responses remain with the partner and are not study research rows. No Survey 1 birth year, age/date, date-confidence, records-confidence or phenotype field is expected. Absence of a transferred field is not an unknown answer imputed to a parent. Referral permission is not research consent.

Study-collected consent attestations, selected-child rule, reported-age/phenotype flags and uncertainty are collected in Survey 2. Legacy `*_s1` research columns from prior drafts are not expected or silently repurposed; document any separately approved legacy import instead.

## Survey 2 and timeline fields

| Name | Type and allowed values | Screen or source | Release |
| --- | --- | --- | --- |
| `s2_initial_consent`, `consent_version` | affirmative / decline; version string | S2-C | R; counts A |
| `adult_parent_guardian`, `english_materials_understood`, `subject_authority_status` | attestations and approved authority/permission status; not inferred from referral | S2-C / approved legal-authority workflow | R; counts A |
| `selected_child_rule_version` | fixed string `youngest_qualifying_v1` | S2 instructions | P |
| `date_confidence_s2` | confidently_exact / uncertain_best_estimate / range_only / cannot_determine | A2 confidence screen | P |
| `records_confidence_s2` | available_now / probably_obtainable / might_obtain / probably_unavailable; unsure/missing status separately | A4 before disclosure | P |
| `reported_age_status_s2`, `reported_phenotype_status_s2` | in_range/out_of_range/unresolved; possible_qualifying/not_qualifying/unresolved; receipt-time version | A1/A2/C01 and construction | P safe flags |
| `records_request_eligible`, `records_request_group`, `records_request_batch_id` | permission + reported-age/phenotype rule; group 1–4 or unclassified; ID | minimized administrative queue | P safe flags/group; R ID |
| `narrative_unprompted` | text; saved/locked timestamps; original hash | A1 | T text, R hash/timestamps |
| `onset_parent` | date object | A2 plus separately logged clarifications | R date; derived P |
| `uncertain_period_present` | yes / no / unsure | A3a | P |
| `uncertain_period_start`, `uncertain_period_end` | date objects / unknown | A3b/c | R; safe relative P |
| `uncertain_period_duration` | count + unit days/weeks/months; approximate flag | A3d | P |
| `full_return_before_onset`, `full_return_start` | yes / no / unsure; date object | A3e/f | P status; R date |
| `disclosure_state` | not_reached / displayed / continue / explicit_decline / departed_no_choice | B1 | P safe state |
| `same_child_confirmation`, `birthdate_parent` | yes / no / unsure; date object | C01 | R date; safe discrepancy P |
| `country_onset`, `country_vaccination` | ISO country code + raw response; unknown / not_applicable | C01a/b | P only if safe |
| `narrative_prompted` | text, separate from A1 | C02 | T |
| `new_behavior_text`, `reduced_skill_text` | text / none / unsure | C03a/b | T |
| `prior_baseline_text`, `change_observer`, `change_persisted`, `persistence_text` | text; parent/other/both/unknown; yes/no/unsure | C03c–f | T text, safe coded P |
| `last_definitely_normal`, `first_definitely_changed` | date objects; observation context not substitute ONSET | C04 clarification | R; safe relative P |
| `uncertainty_clarification` | text + first-notice date bounds | C04 | T/R dates |
| `diagnosis_status`, `diagnosis_date`, `clinician_type` | yes / no / evaluation / unsure; date object; coded clinician type | C05 | P safe status/type; R date |
| `preceding_events` | repeating event enum illness/fever/medication/anesthesia/medical/environment/other; yes/no/unsure; dates/durations/text | C06 | P safe codes/relative; R dates; T text |
| `well_visit_in_window`, `well_visit_parent` | yes/no/unsure; date object | C07a/b | P status; R date |
| `shots_at_well_visit`, `later_vax_after_well` | yes/no/unsure | C07c/d | P |
| `vax_on_or_before_onset`, `vax_parent`, `vax_products_raw` | yes/no/unsure; date object; text/set | C08a–c; no maximum vaccination lookback | P status/standardized products; R dates/raw |
| `later_vax_after_selected`, `selected_visit_corrections` | yes/no/unsure; amendment links | C08d | P flag; R links |
| `vaccination_within_90_days` | yes/no/unsure; reported/derived status and uncertainty; separate from unbounded vaccination selection | C08e; well-comparator eligibility only | P safe status |
| `vax_onset_same_day_order` | administration_before_notice / administration_after_notice / unknown / not_applicable | C08 same-day follow-up | P subject to risk review |
| `pre_vax_unusual`, `pre_vax_unusual_text`, `pre_vax_baseline_text` | yes/no/unsure; text | C09a–c | P flag; T text |
| `baseline_at_vax`, `last_usual_before_vax` | yes/no/could_not_assess/unsure; date object | C09d/e | P status; R date |
| `schedule_report`, `previous_vax_date`, `previous_vax_spacing` | routine/modified/unsure; date object; number + days/weeks/months or no_previous/unknown | C10a/b | P schedule/spacing; R date |
| `ever_vaccinated` | yes/no/unsure, explicitly parent-reported | C11 | P |
| `acute_symptoms_after_vax`, `symptom_types`, `symptom_start`, `symptom_end`, `symptom_end_lag`, `symptoms_ongoing_at_onset` | yes/no/unsure; set; date objects; count object; yes/no/unsure | C12a–e | P codes/lags; R dates |
| `B_parent` | count object, total complete normal days | C12f | P |
| `non_normal_observations`, `non_normal_types` | text then type set | C12g/h | T/P |
| `partial_day_return`, `partial_day_return_text` | yes/no/unsure; text/date/duration | C12i/j | P flag; T/R details |
| `normal_N`, `not_complete_normal_D`, `unknown_U`, `unknown_reason` | count objects; unassessable/unremembered/both | C12k–n | P |
| `materials_available` | set medical/therapy/school/daycare/message/diary/calendar/call/photo/video/visit/other/none/unsure | C13 | P safe codes |
| `records_contact_permission`, `upload_authorization` | yes/no; affirmative/decline/version | C14 | R; counts A |

Repeated timeline periods export `period_id`, `submission_id`, `source_screen`, `start_date`, `end_date`, `duration_value`, `duration_unit`, `precision`, `functioning_status` (complete_normal / not_complete_normal / unassessable / unremembered / mixed_or_unresolved), `observations_text`, `observer`, `partial_return`, `attribution_text`, `evidence_ids`. Keep observations distinct from causal attribution. Periods can be approximate, overlap or conflict; preserve raw records and mark conflicts rather than silently making a continuous invented timeline.

## Visits, evidence, review and acceptance

Each visit exports `visit_id`, `type` (vaccination / regular_well / other / unknown), `administration_date` date object, `actual_administration_status`, `shots_at_visit`, `latest_visit_confirmation`, `vaccination_within_90_days` (yes / no / unsure; separate well-comparator status), `history_90_status` (parent_only_absence / record_supported_window / unknown / conflicting), `coverage_text`, `products`, `evidence_ids`. Products export remembered/documented name, normalized label, mapping version and unknown flag. Do not infer product from child age or nominal grid. Raw product strings remain restricted until reviewed for identifiers.

Each evidence item exports `receipt_at`, `media_type`, `file_hash`, `storage_pointer`, `provenance` (original / copy / screenshot / unknown), `created_date`, `described_event_date`, `parent_claimed_onset`, `parent_certainty`, `date_support`, `content_support`, `alteration_concern`, `legibility`, `tier`, `review_notes`. All R; only safe coded tier/concern summaries may be public. Never equate recording date with described event date.

Every reviewer record contains `reviewer_id`, `child_id`, `review_version`, `locked_at`, `sora_judgment`, birthdate, ONSET, vaccination date, well date, earliest documented post-change date, first-notice bounds, B count object, products, latest/history statuses, supporting/conflicting evidence IDs, evidence tiers, reason codes. Expand the shared date/count objects for every applicable field. Store amendment ID/reason separately. No other review is visible before lock.

Accepted records export one record per field: `field_name`, `accepted_value`, `accepted_status`, `agreement` (three / two / unresolved), `agreeing_reviewer_ids` R, `evidence_tier`, `conflict`, `input_consistency`, `build_version`. A date value, its bounds and verification classification each require independent exact-majority agreement; a majority date does not establish majority verification. Do not independently vote a width or average dates. Check jointly accepted fields for consistency before constructing a tier-qualified dataset.

## Derived and public fields

For each series `parent`, `reviewer_a`, `reviewer_b`, `reviewer_c`, `accepted`, export `onset_age_days`, `onset_age_completed_months`, `onset_weekday`, `vaccination_weekday`, `A_days` with bounds/status, `B` count object, `well_to_onset_days`, `vaccination_to_documentation_days`, `C_quarter_days`, `C_nominal_days`, nominal age selected, reference rule version, and no-anchor/precision flags. Derive only from that series' valid inputs. Parent B remains the direct report. Same-day A does not establish vaccination preceded recognition within the day.

Public files may include `public_child_id`, safe developmental/diagnosis/history classifications, source-generalization code, safe derived series, evidence/verification precision, agreement/conflict/duplicate flags, narrative suppression flags and redacted text. A released approximate interval must retain precision and bounds, never masquerade as exact. Country/product/source/age combinations may require suppression/generalization. A derived interval is not inherently anonymous.

Keep `admin_target_complete`, `full_payment_eligible`, final scientific flags and public approval separate. Export `validated_minimum_eligible` as eligible/ineligible/unresolved with reason codes and rule version: confirmed uniqueness, majority phenotype/age, contemporaneous first-notice corroboration and documented selected most recent vaccination on/before ONSET, with no maximum lookback, supported dates/bounds and no material unresolved contradiction. Well-only/no-anchor records are ineligible for this count, not deleted; uncertain anchor selection stays unresolved. Report exact-date and bounded-date contributors separately. Parent confirmation of no later vaccination is distinct from documentary administration evidence and not proof of complete history. Safe coded eligibility/reasons may be public after privacy review; underlying evidence/absolute dates remain restricted. Payment amounts/payees are restricted; report safe aggregate totals only. Public narrative and row suppression reasons are coarse privacy/permission categories, not identifying explanations. Full reviewer notes remain restricted.

## Screen events and corrections

Events export `event_id`, `submission_id`, `screen_id`, `action` (shown / saved / confirmed / locked / declined / resumed / stopped / operationally_closed), `timestamp`, `version`, `save_success`. Lock must be server-enforced. Before consent collect no research answers; any unavoidable security metadata is separately minimized and disclosed. Do not retain unsent keystrokes as answers. On the narrative screen, explicit Save transmits content after consent and notifies the parent that saved partial answers are retained. Edits before Confirm/lock stay auditable; after lock, corrections are new records linked to the original.

Amendments export original record ID, new value/status, reason, requester, saved time and approval; never replace raw data. Retain original batch/target counts and corrected duplicate or clerical counts. Publication transformations export package version, source build hash, field transformations, suppression/generalization rules, checker approvals and checksums. The final platform export adapters, machine-readable dictionary and end-to-end tests are prelaunch requirements, not completed by this Markdown schema.
