from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import hashlib
import shutil
import tempfile

SRC = Path(r"C:\Users\stk\Documents\GitHub\autism\irb_submission\CHD_SORA_DATA_RESOURCE\ipakirb-form-1.docx")
OUT = Path(r"C:\Users\stk\Documents\GitHub\autism\irb_submission\CHD_SORA_DATA_RESOURCE\ipakirb-form-1_filled.docx")
EXPECTED_SHA = "40AB07DD732B3FF857C4931D67A309EA569CA6B7708829F5365790414533C27A"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

values = {
    "Name of Title": "Multisite Parent-Reported Data Resource of Sudden-Onset Regressive Autism (SORA)",
    "PI Name": "Brian Hooker, Ph.D.",
    "Affiliation": "Children's Health Defense (CHD) [confirm exact legal entity, PI title, and affiliation]",
    "Address": "TBD - coordinating PI/sponsor mailing address",
    "Email": "TBD - coordinating PI email",
    "Phone": "TBD - coordinating PI telephone",
    "Description including background, rationale & goals.": (
        "This minimal-risk, multisite data-resource study will use a clinic-distributed electronic survey "
        "to collect structured parent reports of sudden-onset regressive autism (SORA): an abrupt, dramatic, "
        "persistent developmental or behavioral change with a distinguishable Day 0, followed by a clinical ASD "
        "diagnosis. The study addresses a measurement gap because existing research has not been identified that "
        "combines a narrowly defined discrete onset, individual-day vaccination proximity, recall-quality measures, "
        "and random documentary validation. Clinics will invite their complete defined contactable populations but "
        "will not disclose patient lists to CHD. The goal is to create, quality-check, document, and release a coded, "
        "disclosure-reviewed dataset for independent analysis. This collection study will not test causation or "
        "estimate population incidence."
    ),
    "Aims detailing objectives & outcomes including Type of Study per guidelines.": (
        "Type: minimal-risk, multisite, clinic-distributed, parent-completed coded electronic survey with an embedded "
        "record-validation substudy. Aim 1: collect standardized information on developmental pattern, parent-recognized "
        "SORA Day 0, onset age, the three qualifying change categories, and elapsed vaccination proximity. Aim 2: document "
        "recruitment flow, missingness, recall horizon, confidence, timing anchors, information sources, prior causal "
        "attribution, and post-onset vaccination decisions. Aim 3: assess agreement for a randomly selected, separately "
        "authorized subset using limited contemporaneous onset evidence and vaccination records. Aim 4: produce a "
        "documented, disclosure-reviewed public-use dataset, or aggregate and controlled-access data if row-level release "
        "is not safe, together with descriptive data-quality and feasibility reporting."
    ),
    "Estimate start/end dates of study.": (
        "Proposed start: TBD, only after IRB approval and completion of all operational gates. Proposed end: 12 months "
        "after study initiation [confirm]. Clinic enrollment is initially 30 days and may extend through Day 90 until the "
        "fourth clinic activates; each clinic's invitation campaign lasts 35 days, followed by the prespecified survey and "
        "validation lock periods."
    ),
    "Participant population including age, health & inclusion criteria.": (
        "Adult respondents (age 18 or older) who are parents or legal guardians in participating autism diagnosis/treatment "
        "clinics' complete defined contactable populations, including families of children evaluated but not diagnosed with "
        "ASD. All consenting respondents may provide screening/background data. The SORA analytic resource is limited to "
        "reports about a child with a subsequent clinical ASD diagnosis, parent-recognized onset before the fifth birthday, "
        "a discrete rather than gradual Day 0, at least one qualifying category beginning on Day 0 (new pathological "
        "behavior, loss of an existing behavior/skill, or changed sensory sensitivity), and persistence for at least 30 days "
        "or through a later clinical evaluation. Children are not contacted and undergo no intervention. A random eligible "
        "subset may enter validation only after separate authorization. Final inclusion/exclusion and Subpart D findings are "
        "subject to IRB approval."
    ),
    "Study ID": "TBD - assigned by IPAK-EDU IRB",
}

untagged = {
    "[Source]": "Funder: TBD. Proposed clinic compensation: flat $5,000 per activated clinic, up to 10 clinics; total study budget TBD.",
    "[Type]": "Human - minimal-risk survey/data-resource study with limited record validation",
}

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def replace_sdt_text(root, tag, value):
    changed = 0
    for sdt in root.xpath(".//w:sdt", namespaces=NS):
        tags = sdt.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
        if tags and tags[0] == tag:
            texts = sdt.xpath("./w:sdtContent//w:t", namespaces=NS)
            if not texts:
                raise RuntimeError(f"No text node for control {tag!r}")
            texts[0].text = value
            texts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            for extra in texts[1:]:
                extra.text = ""
            changed += 1
    return changed

if sha256(SRC) != EXPECTED_SHA:
    raise RuntimeError("Source form hash changed; fresh template inspection required")

with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    with ZipFile(SRC) as zin:
        zin.extractall(td)

    changed_counts = {}
    for rel in (Path("word/document.xml"), Path("word/header1.xml")):
        path = td / rel
        root = etree.parse(str(path))
        for tag, value in values.items():
            n = replace_sdt_text(root, tag, value)
            if n:
                changed_counts[tag] = changed_counts.get(tag, 0) + n
        for sdt in root.xpath(".//w:sdt", namespaces=NS):
            tags = sdt.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
            if tags and tags[0]:
                continue
            texts = sdt.xpath("./w:sdtContent//w:t", namespaces=NS)
            current = "".join(t.text or "" for t in texts)
            if current in untagged:
                texts[0].text = untagged[current]
                texts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                for extra in texts[1:]:
                    extra.text = ""
                changed_counts[current] = changed_counts.get(current, 0) + 1
        root.write(str(path), xml_declaration=True, encoding="UTF-8", standalone="yes")

    expected = {
        "Name of Title": 2, "PI Name": 2, "Affiliation": 1, "Address": 1,
        "Email": 1, "Phone": 1,
        "Description including background, rationale & goals.": 1,
        "Aims detailing objectives & outcomes including Type of Study per guidelines.": 1,
        "Estimate start/end dates of study.": 1,
        "Participant population including age, health & inclusion criteria.": 1,
        "Study ID": 1, "[Source]": 1, "[Type]": 1,
    }
    if changed_counts != expected:
        raise RuntimeError(f"Unexpected field replacements: {changed_counts}")

    with ZipFile(OUT, "w", ZIP_DEFLATED) as zout:
        for path in sorted(td.rglob("*")):
            if path.is_file():
                zout.write(path, path.relative_to(td).as_posix())

print(OUT)
print(changed_counts)
