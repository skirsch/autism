"""Generate spark_survey_redcap_dictionary.csv (REDCap data-dictionary format)."""
import csv

COLS = ["Variable / Field Name","Form Name","Section Header","Field Type","Field Label",
        "Choices, Calculations, OR Slider Labels","Field Note","Text Validation Type OR Show Slider Number",
        "Text Validation Min","Text Validation Max","Identifier?","Branching Logic (Show field only if...)",
        "Required Field?","Custom Alignment","Question Number (surveys only)","Matrix Group Name",
        "Matrix Ranking?","Field Annotation"]
FORM = "spark_parent_survey"
REG = "[change_type] = '1' or [change_type] = '2'"
CMP = "[change_type] = '3' or [change_type] = '4'"

def ch(*opts): return " | ".join(f"{i+1}, {o}" for i, o in enumerate(opts))

INTERVAL = ch("Don't remember","Not within 120 days before","<1 day (<24 h)","2 days (24-48 h)","3 days (49-72 h)",
              "4 days","5 days","6 days","7 days","8-13 days","14-29 days","30-59 days","60-83 days","84-97 days","98-120 days")
SHOTS = ch("0 (no shots)","1","2","3","4","5 or more","Don't remember")
CONF = ch("Absolutely certain","Within 1 day","Within 2 days","Within 3 days","Within 4 days to a week","Could be off by a week or more")
DOW = ch("Don't remember","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","It was a weekday","It was a weekend")
EVID = ch("Memory alone","Calendar or diary","Photos or videos with dates","Texts, emails, or patient-portal messages",
          "Daycare or school notes","A doctor's record","Social-media post","Other")
BEFORE3 = ch("Fever","Tylenol or acetaminophen","Illness","Pediatrician/well-child visit WITHOUT any shots",
             "Pediatrician/well-child visit WITH shots","Ear infection","Vaccination (any setting)","Dentist visit",
             "Toxic environmental exposure (mold, chemical...)","New prescription drug (e.g., antibiotic)",
             "Your child's birthday","Your birthday","New Year's Day","Other (specify in Notes)","None of the above",
             "Too long ago, don't remember")
AFTER14 = ch("High-pitched screaming","Sleepless nights","LOST existing behavior(s) (eye contact, social interaction...)",
             "LOST existing skill(s) (words, motor skills...)","DEVELOPED new repetitive behaviors (head banging, toe walking, arching...)",
             "Change in sensitivities (light, sound, pain, touch, being held)","Extreme fussiness","New obsessions","Other (specify in Notes)")
ATTR = ch("Genetics / family history","Prematurity or birth complications","Something during pregnancy","An illness or infection",
          "A vaccine","A medication","Something in the environment","Nothing in particular - random","Don't know","Other")
HYP = ch("Before my child was born","Before I noticed the change","Around the time I noticed it","After the diagnosis","Never heard it","Not sure")
STATES = ch(*"AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY Other".split())

rows = []
def add(name, ftype, label, choices="", note="", valid="", vmin="", vmax="", branch="", req="y", section=""):
    rows.append({"Variable / Field Name":name,"Form Name":FORM,"Section Header":section,"Field Type":ftype,"Field Label":label,
                 "Choices, Calculations, OR Slider Labels":choices,"Field Note":note,
                 "Text Validation Type OR Show Slider Number":valid,"Text Validation Min":vmin,"Text Validation Max":vmax,
                 "Identifier?":"","Branching Logic (Show field only if...)":branch,"Required Field?":req,
                 "Custom Alignment":"","Question Number (surveys only)":"","Matrix Group Name":"","Matrix Ranking?":"","Field Annotation":""})

add("record_id","text","Record ID",req="")
add("consent","checkbox","I am at least 18, the parent or legal guardian of the SPARK participant, and I agree to take part. I understand that de-identified responses may be shared with other researchers under SPARK's data-sharing rules.",
    ch("I agree"), section="How parents first notice developmental change")
add("sex","radio","What is the sex of your child?", ch("Male","Female"))
add("state","dropdown","What US state do you live in?", STATES)
add("change_type","radio","Which best describes how your child's autism-related differences first appeared?",
    ch("A sudden, dramatic change over about two weeks or less, after developing normally",
       "A noticeable change over a few weeks to a couple of months",
       "Gradual - differences were always there or emerged slowly","Not sure"))
# Regression path
add("how_long_ago","radio","How long ago did you notice the sudden change (the \"onset date\")?",
    ch("Within 3 months","3-6 months ago","6 months to 1 year ago","1-2 years ago","2-5 years ago","More than 5 years ago"), branch=REG, section="When it happened")
add("onset_date","text","If you remember the exact or approximate calendar date of onset, enter it. Otherwise leave blank.",
    valid="date_mdy", branch=REG, req="")
add("onset_dow","radio","Do you remember the day of the week onset happened, or whether it was a weekday or weekend?", DOW, branch=REG)
add("age_onset_months","text","Your child's age in months at onset (e.g., 18)", valid="integer", vmin="0", vmax="72", branch=REG)
add("date_evidence","checkbox","What is your memory of the onset timing based on? Check all that apply.", EVID, branch=REG)
add("sequence","notes","Briefly describe the chain of events in the 15 days before onset that you think might be relevant. Use (0) as the first reference day.",
    note="Example: birthday party (0) -> illness (1) -> fever (2) -> high-pitched screaming for 12 hours (2) -> lost eye contact (4).", branch=REG, section="In your own words")
add("before3","checkbox","What do you remember happening in the 3 days BEFORE onset? Check all that apply.", BEFORE3, branch=REG, section="Timing")
add("after14","checkbox","In the 14 days AFTER onset, which changes did you observe? Check all that apply.", AFTER14, branch=REG)
add("visit_interval","radio","How many days BEFORE onset was your child's most recent doctor visit (well-child or sick visit)? Choose the closest answer, even if unsure of the exact interval.",
    INTERVAL.replace("Not within 120 days before","No visit within 120 days before"), branch=REG)
add("visit_confidence","radio","How certain are you of that interval?", CONF, branch=f"({REG}) and [visit_interval] > 2")
add("visit_shots","radio","How many vaccine injections were given at that visit?", SHOTS, branch=f"({REG}) and [visit_interval] > 2")
add("vax_prior_interval","radio","Was there an earlier visit WITH shots within 120 days before onset? If so, how many days before onset?",
    INTERVAL.replace("Not within 120 days before","No visit with shots within 120 days"), branch=f"({REG}) and [visit_shots] = '1'")
add("documentation","radio","If we asked you for contemporaneous documentation of the onset timing (email, text, video, photo, social-media post, diary note, calendar entry, doctor call), could you provide it?",
    ch("Yes, 100% certain","Yes, 80%+ certain","Maybe","Unlikely","Highly unlikely"), branch=REG)
add("record_upload_ok","radio","Would you be willing to share your child's official immunization record (state registry or pediatrician) with the research team in a follow-up?", ch("Yes","Maybe","No"), branch=REG)
# Comparison path
add("age_concern_months","text","Your child's age in months when you first became concerned about their development", valid="integer", vmin="0", vmax="72", branch=CMP, section="When you first became concerned")
add("concern_date","text","If you remember the approximate calendar date you first became concerned, enter it. Otherwise leave blank.", valid="date_mdy", branch=CMP, req="")
add("concern_dow","radio","Do you remember the day of the week, or whether it was a weekday or weekend?", DOW, branch=CMP)
add("sequence_c","notes","Briefly describe what you noticed and what was going on in your child's life around that time.", branch=CMP)
add("before3_c","checkbox","What do you remember happening in the 3 days BEFORE you first became concerned? Check all that apply.", BEFORE3, branch=CMP)
add("visit_interval_c","radio","How many days BEFORE you first became concerned was your child's most recent doctor visit? Choose the closest answer.",
    INTERVAL.replace("Not within 120 days before","No visit within 120 days before"), branch=CMP)
add("visit_confidence_c","radio","How certain are you of that interval?", CONF, branch=f"({CMP}) and [visit_interval_c] > 2")
add("visit_shots_c","radio","How many vaccine injections were given at that visit?", SHOTS, branch=f"({CMP}) and [visit_interval_c] > 2")
add("vax_prior_interval_c","radio","Was there an earlier visit WITH shots within 120 days before you first became concerned? If so, how many days before?",
    INTERVAL.replace("Not within 120 days before","No visit with shots within 120 days"), branch=f"({CMP}) and [visit_shots_c] = '1'")
# Attribution (all)
add("cause","notes","What do you think might have triggered the change, and why? Do you think it was a random event with no specific trigger?", req="", section="Your view")
add("attribution","checkbox","Which of these do you think contributed? Check all that apply.", ATTR)
add("hypothesis_exposure","radio","When did you first hear the idea that vaccines might be connected to autism?", HYP)
# Close
add("notes","notes","Anything else we should know, or comments on unclear questions or missing options?", req="", section="Finish")
add("recontact_ok","radio","May the research team contact you (through SPARK) about a follow-up?", ch("Yes","No"))
add("share_public_ok","radio","May a coarsened, de-identified version of your answers (no free text, no calendar dates) be included in a public research file?", ch("Yes","No"))

with open("spark_survey_redcap_dictionary.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(rows)
print(len(rows), "fields written")
