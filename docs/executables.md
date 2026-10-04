# Executable guide

## V5 local draft and reference validation

- Script: `protocol/v5/validation/validate_drafts.ps1`.
- Run from repository root: `pwsh -NoProfile -File protocol/v5/validation/validate_drafts.ps1`.
- Requires PowerShell 7; no external packages, network, secrets or participant files.
- Reads the Markdown files in `protocol/v5` and checks required documents, version headers and relative links; tests a subset of fictitious calendar/lag/count/exact-majority examples in `prelaunch_validation.md`. Also checks text contracts for the two-question partner screen, all-referral Survey 2 access, pre-disclosure confidence fields, deferred material requests and minimized selection queue. These are not live routing or permission tests.
- Prints JSON with check/link/failure counts; exits nonzero on failures. Does not write files, transform production exports, inspect security configuration or submit anything.
- This is a local document/reference helper, not the production processing pipeline or proof that a platform workflow/IRB requirement is satisfied.

## Onset-age histogram and CDC reference

- Script: `outputs/onset_age_n322/plot_onset_age.py`.
- Run from repository root: `python outputs/onset_age_n322/plot_onset_age.py`.
- Requires Python with matplotlib. Bundled runtime lacked matplotlib; this run used installed system Python.
- Reads `C:\Users\stk\Downloads\SOA2-Grid view.csv` without modification.
- Outputs `onset_age_cdc_reference.png` and `summary.json` beside the script. The summary hashes the current input. Running after the export changes regenerates this snapshot; use a new output directory for a distinct archived report.
- Uses one-month bins; excludes missing, negative, noninteger, or greater-than-1,200-month ages with explicit flags. The actual current exclusion is record #84 at 2,212 months. Does not infer corrected ages.
- CDC 2025 reference ranges are illustrative, not individualized vaccination dates. The plot is descriptive, not a hypothesis test.

## Monthly onset-age zoom

- Run: `python outputs/onset_age_n322/plot_onset_age_zoom.py`.
- Same Downloads CSV and matplotlib dependency as above; generates `onset_age_2_to_20.png` and prints adjacent-month counts for requested ages 2, 4, 6, 12, 15, and 18. Month 1 is included in the boundary comparison but not the plotted crop. Source remains unchanged.
