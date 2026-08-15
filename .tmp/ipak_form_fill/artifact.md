# IPAK intake-form template contract

- **Reference:** `C:\Users\stk\Documents\GitHub\autism\irb_submission\CHD_SORA_DATA_RESOURCE\ipakirb-form-1.docx`
- **SHA-256:** `40AB07DD732B3FF857C4931D67A309EA569CA6B7708829F5365790414533C27A`
- **Structure:** Two portrait US-Letter sections, one-inch margins, distinct first-page/header behavior. The source package and all formatting, headers, footers, tables, relationships, and noneditable text are preserve-only.
- **Editable slots:** Fifteen plain-text content controls: study title, PI, affiliation, address, email, phone, funding source, study type, description, aims, duration, participant population, and three repeated header fields (study ID, PI, title).
- **Editing rule:** Create a copy and replace only text inside the identified plain-text content controls. Preserve the controls and all surrounding OOXML.
- **Unknown-data rule:** Use explicit `TBD` or bracketed confirmation language rather than inventing facts.
- **Fidelity gates:** Original remains byte-identical; only `word/document.xml` and `word/header1.xml` may change; control count/tags remain unchanged; final retains two sections and the source page geometry.
- **Render note:** The packaged renderer could not locate LibreOffice on this Windows host. Attempt Microsoft Word PDF export if Word automation is available; otherwise complete structural verification and disclose the visual-QA limitation.
