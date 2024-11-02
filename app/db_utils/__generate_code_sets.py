from datetime import datetime
import re

from random import randint

from app.models.code_value_set import CodeSet
from app.models.code_value import CodeValue
from app.services.db_get_or_create import db_get_or_add_instance, db_get_or_create
from .__generate_units_of_measure import SU_codevalues_cs54

from app.core.constants import END_EFFECTIVE_DATE_ISO


#########################################
# System Use Code Sets
def create_SU_codeset_(db):
    """ Creating system use code set - so it is consistent between domains """
    # codeset, display
    su_codesets = (
        (2,         'Admit Source'),
        (3,         'Admit Type'),
        (8,         'Data Status'),
        (10,        'Accommodation'),
        (16,        'Courtesy Code'),
        (19,        'Discharge Disposition'),
        (23,        'Doc_Format'),
        (24,        'Event Relationship'),
        (34,        'Medical Service'),
        (48,        'Active Status'),
        (53,        'Event_Class'),
        (54,        'Units of Measure'),
        (68,        'Admit Mode'),
        (69,        'Encounter Type Class'),
        (71,        'Encounter Type'),
        (72,        'Event Code'),
        (79,        'Task Status'),
        (87,        'Confidential Level'),
        (88,        'Position'),
        (89,        'Contributor System'),
        (93,        'Event Sets'),
        (106,       'Activity Type'),
        (120,       'Compression Code Value'),
        (200,       'Order Catalog'),
        (220,       'Location'),
        (261,       'Encounter Status'),
        (263,       'Alias Pool Code'),
        (289,       'Result Type'),           # The default result type for the task/assay specified
        (302,       'Person Type'),
        (321,       'Encounter Class'),
        (400,       'Source Vocabulary'),
        (4003,      'Frequency'),
        (4010,      'Task Priority'),
        (6000,      'Catalog Type'),
        (6003,      'Order Action Type'),
        (6004,      'Order Status'),
        (6006,      'Communication Type'),
        (6011,      'Mnemonic Type'),
        (6014,      'Reschedule Reason'),
        (6024,      'Message Subject'),                
        (6025,      'Task Class'),
        (6026,      'Task Type'),
        (6027,      'Task Activity'),
        (6029,      'Task Activity Class'),
        (6034,      'Task Subtypes'),
        (14003,     'Discrete Data Assay'),           # Define how data are entered
        (14024,     'Task Status Reason Code'),
        (14219,     'Blood Bank Donor Procedure'),  
        (14281,     'Department Status'),  
        (14766,     'Accompanied By Code'),
        (14767,     'Accommodation Reason'), 
        (16389,     'DCP Clinical Category'),       # CS 16389: DCP Clinical Category
        (17969,     'ABN Status'),                  # Advnaced Beneficiary Notice Status Code
        (18309,     'Med Order Type'),
        (22589,     'Alternate Level of Care'),
        (255090,    'Charting Agent'),

        (4002164,   'Offset Minute Type Code'),
        (4002509,   'Rounding Rule Code'),
    )

    with db.session() as session:
        for cs in su_codesets:
            db_get_or_add_instance(
                    session, 
                    CodeSet,
                    code_set = cs[0],
                    display = cs[1],
                    display_key = re.sub('[^0-9a-zA-Z]+', '', cs[1]).upper(),
                    definition = cs[1],
                    description = cs[1],
                )
        session.commit()


#########################################
# System Use Code Values
def SU_codevalues_cs2(db):
    """ Codeset 2: Admit Source """
    code_values = (
        'Clinic',
        'Newborn',
        'Day Procedure',
        'Stillborn',
        'Direct',
        'Emergency',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 2,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs3(db):
    """ Codeset 3: Admit Type """
    code_values = (
        'Elective',
        'Newborn',
        'Urgent/Emergent',
        'Stillborn',
        'Deceased Donor',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 3,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs8(db):
    """ Codeset 8: Data Status """
    code_values = (
        'Active',
        'Modified',
        'Anticipated',
        'Auth (Verified)',
        'Canceled',
        'Transcribed (corrected)',
        'Dictated',
        'In Error',
        'In Lab',
        'In Progress',
        'Not Done',
        'REJECTED',
        'Started',
        'Superseded',
        'Transcribed',
        'Unauth',
        '? Unknown',
        'Transcribed',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 8,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs10(db):
    """ Codeset 10: Accommodation Code Value """
    code_values = (
        'Private',
        'Semi Private',
        'Ward',
        '1Semi2Private',
        '1Private2Semi',
        'Ask Patient',
        'Not Applicable',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 10,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs16(db):
    """ Codeset 16: Courtesy Code 
        It indicate whether the patient will be extended certain special courtesies such as express discharge,
        bypassing a stop at the cashiers window upon leaving when finanical arrangements are agreed upon in advance.
    """
    code_values = (
        'Yes',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 16,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs19(db):
    """ Codeset 19: Discharge Disposition
    """
    code_values = (
        'Admitted to an Inpatient Unit',
        'Left Against Medical Advice',
        'Transferred to Acute/Rehab/Tertiary MH',
        'Deceased',
        'Transferred to Outpatient Clinic',
        'Discharged Home without Support Services',
        'Discharged Home with Support Services',
        'Stillbirth',
        'Registered, Triaged, Not Assessed (LWBS)',
        'Admitted to Critical Care or an OR',
        'System Discharge',
        'Transferred to Other',
        'Left AMA After Initiation of Treatment',
        'Left AMA After Assessment, No Treatment',
        'Externally Referred in Deceased Donor',
        'Discharged to Funeral Home or Autopsy',
        'Admitted to Day Surgery',
        'No Service Provided/Created in Error',
        'Patient Did Not Return From a Pass/Leave',
        'Registered But Not Triaged (LWBS)',
        'Cancelled After Arrival',
        'Patient Deceased While On a Pass/Leave',
        'Deceased Discharged to Family/Other',
        'Return to Inpatient Unit',
        'Notified of Death',
        'Involuntary Patient Absconded',
        'End of Treatment',
        'Transferred to Residential',
        'Transferred to Jail or Corrections',
        'Transferred to Assisted Living/Shelters',
        'Transferred to Hospice',
        'Transferred to Community MH/Addiction',
        'Registered/Transferred to ED In Error',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 19,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs23(db):
    """ Codeset 23: Doc Format """
    doc_formats = (
        'ACR-NEMA',
        'AH',
        'AS',
        'AUDIO BASIC',
        'AUDIO MPEG',
        'CP',
        'DDIF',
        'DIO',
        'GIF',
        'HTML',
        'JPEG',
        'LONG_BLOB',
        'LONG_TEXT',
        'MSWORD',
        'NONE',
        'PACS FOLD ID',
        'Paper',
        'PDF',
        'PNG',
        'PTIFF',
        'RTF',
        'RVS',
        'TIFF',
        '? Unknown',
        'url',
        'VIDEO MPEG',
        'VOICE',
        'WINBMP',
        'WINEMF',
        'XHTML',
        'XML',
    )
    with db.session() as session:
        for df in doc_formats:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 23,
                definition = df,
                description = df,
                display = df,
                display_key = re.sub('[^0-9a-zA-Z]+', '', df).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs24(db):
    codes = (
        # DISPLAY	    MEANING	    DESCRIPTION	        DEFINITION	            DISPLAY_KEY
        ['C',	        'CHILD',	'Child',	        'Child Document',	    'C'],
        ['Link',	    'LINK', 	'Linked Result',	'Linked Result',        'LINK'],
        ['O',	        'ORPHAN',	'Orphan', 	        'Orphaned Document',    'O'],
        ['R',   	    'ROOT',	    'Root',	            'Root Document',    	'R'],
        ['? Unknown',   'UNKNOWN',	'Undefined Code',	'Undefined Code',	    'UNKNOWN'],
    )

    with db.session() as session:
        for cv in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 24,
                display = cv[0],
                meaning = cv[1],
                description = cv[2],
                definition = cv[3],
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv[1]).upper()    # remove non-alphanumeric characters
            )

def SU_codevalues_cs34(db):
    """ Codeset 34: Medical Service """
    codes = (
        'Allergy and Immunology',
        'Anesthesiology',
        'Emergency',
        'Family Practice',
        'Obstetrics',
        'Dermatology',
        'Urology',
        'Endocrinology',
        'Gastroenterology',
        'Nephrology',
        'Ophthalmology',
        'Pathology',
        'Pediatrics',
        'Radiation Oncology',
        'Dentistry',
        'Laboratory Medicine',
        'Newborn',
        'Respiratory Therapy',
        'Assisted Living',
        'Palliative Medicine',
        'Neonatology',
        'Neurology',
        'Neurosurgery',
        'General Surgery',
        'Infectious Diseases',
        'Nutrition',
        'Hyperbaric Medicine',
        'Cardiology',
        'Transplant',
        'Gynecologic Oncology',
        'Medical Imaging',
        'Thoracic Surgery',
        'Trauma',
        'Deceased Donor',
        'Plastic Surgery',
        'Psychiatry',
        'Psychology',
        'Audiology',
        'Occupational Therapy',
        'Orthopedic Surgery',
        'Otolaryngology',
        'Pain Medicine',
        'Pharmacy',
        'Physical Medicine and Rehabilitation',
        'General Internal Medicine',
        'Geriatric Medicine',
        'Critical Care',
        'Gynecology',
        'Rheumatology',
        'Bone Marrow Transplant',
        'Cardiac Surgery',
        'Clinical Trials',
        'Deceased',
        'Developmental Pediatrics',
        'Hospitalist Medicine',
        'Medical Oncology',
        'Midwifery',
        'Occupational Medicine',
        'Physiotherapy',
        'Speech Language Pathology',
        'Medical Imaging Inpatient',
        'Hospice',
        'Transitional Care Unit',
        'Short Stay Long Term Care',
        'Vascular Access',
        'Wound Ostomy',
        'Community IV',
        'Short Stay Hospice',
        'External Results',
        'Surgical Oncology',
        'Genetic Counselling',
        'Late Effects',
        'Positron Emission Tomography',
        'High Acuity',
        'In-Error',
        'Respirology',
        'Vascular Surgery',
        'Medical Genetics',
        'Oral and Maxillofacial Surgery',
        'Public Health',
        'Stillborn',
        'Social Work',
        'Forensic Pathology',
        'Hematology',
        'Biochemical Diseases',
        'HIM Documentation',
        'Podiatry',
        'Residential',
        'Adolescent Medicine',
        'Referral Oncology',
        'Community Day Program',
        'Support Session',
        'Counselling',
        'Hereditary Cancer Surveillance',
        'Multidisciplinary Oncology',
        'Medical Imaging Emergency',
        'Internal Results',
        'Addiction Medicine',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 34,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs48(db):
    """ Creating System Use (SU) code values - Codeset 48 Active Status """
    statuses = (
        'Active',
        'Combined',
        'Historical value - combined',
        'Deleted',
        'Draft',
        'Inactive',
        'Recall',
        'Review',
        'Suspended',
        'Unknown',
    )
    with db.session() as session:
        for s in statuses:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 48,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs53(db):
    """ Creating System Use (SU) code values - Codeset 53: Event Class """
    event_classes = (
        'Addendum',
        'AP',
        'Attachment',
        'Case',
        'Clinical Document',
        'Contribution',
        'Count',
        'Date',
        'DOC',
        'Document',
        'Done',
        'GRP',
        'Group Document',
        'Group Section',
        'Helix',
        'HLA Typing',
        'Immunization',
        'Interp',
        'IO',
        'MBO',
        'mdoc',
        'MED',
        'NUM',
        'Place Holder',
        'Procedure',
        'Radiology',
        'Result - Document',
        'Single Contributor Document',
        'Section',
        'Trans',
        'TXT',
        '? Unknown',
    )
    with db.session() as session:
        for ec in event_classes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 53,
                definition = ec,
                description = ec,
                display = ec,
                display_key = re.sub('[^0-9a-zA-Z]+', '', ec).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs68(db):
    """ Codeset 68: Admit Mode """
    code_values = (
        'Ground Ambulance Only',
        'No Ambulance',
        'Air Ambulance Only',
        'Air and GRound Ambulance',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 68,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs69(db):
    """ Codeset 69: Encounter Type Class """
    codes = (
        'Blood donation',
        'Case Management',
        'community health record',
        'Emergency',
        'Home Health',
        'Inbox Message',
        'Inpatient',
        'zzMapping Not Found',
        'Observation',
        'Outpatient',
        'Phone Msg',
        'Preadmit',
        'Private Duty',
        'Recurring',
        'Research',
        'Skilled Nursing',
        'Wait List',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 69,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs71(db):
    """ Codeset 71: Encounter Type """
    codes = (
        'Emergency',
        'Day Surgery',
        'Inpatient',
        'Outpatient in a Bed',
        'Outpatient',
        'Recurring',
        'Historical',
        'Pre-Inpatient',
        'Pre-Recurring',
        'Pre-Day Surgery',
        'Pre-Outreach',
        'Home Care',
        'Deceased',
        'Tertiary MH',
        'Data Storage',
        'Outside Images',
        'Phone Message',
        'Virtual Health',
        'Pre-Outpatient',
        'Assisted Living',
        'Provider to Provider',
        'Outreach',
        'Residential',
        'Stillborn',
        'Newborn',
        'Referral',
        'Specimen',
        'ALC',
        'Outpatient OB',
        'Pre-Outpatient OB',
        'Pre-Home Care',
        'Phone Consult',
        'Minor Surgery',
        'Pre-Outpatient in a Bed',
        'Pre-Minor Surgery',
        'External Results',
        'In-Error',
        'Lab Recurring',
        'Internal Results',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 71,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs79(db):
    """ Creating System Use (SU) code values - Codeset 79: Task Status """
    statuses = (
        'Cancelled',
        'Complete',
        'Deleted',
        'Delivered',
        'Discontinued',
        'Dropped',
        'In Error',
        'InProcess',
        'OnHold',
        'Opened',
        'Overdue',
        'Pending',
        'Read',
        'Read Awaiting Signature',
        'Recalled',
        'Refused',
        'Rework',
        'Suspended',
        'Pending Validation',
    )
    with db.session() as session:
        for s in statuses:
            if s in ("Pending", "Overdue"):
                db_get_or_create(
                    session,
                    CodeValue,
                    code_set = 79,
                    definition = s,
                    description = s,
                    display = s,
                    display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper(),  # remove non-alphanumeric characters
                    meaning = s.upper()
                )

            else:
                db_get_or_create(
                    session,
                    CodeValue,
                    code_set = 79,
                    definition = s,
                    description = s,
                    display = s,
                    display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()  # remove non-alphanumeric characters
                )


def SU_codevalues_cs87(db):
    """ Codeset 79: Confidential Level.
        Identifies a level of security that may restrict access or release of information.
    """
    code_values = (
        'Chemical Dependency',
        'Routine Clinical',
        'Legal/Sensitive',
        '? Unknown',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 87,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs88(db):
    """ Codeset 88: Position """
    code_values = (
        'Ambulatory - Nurse',
        'DBA',
        'Emergency - Nurse',
        'Emergency - Nurse Manager',
        'Nurse - ICU',
        'Residential Care',
        'RadNet - Nurse',
        'Nurse - Wound Ostomy',
        'OB - Ambulatory Nurse',
        'Respiratory Therapist',
        'Nurse',
        'MH - Nurse',
        'Nurse - Supervisor',
        'Nurse - NICU',
        'OB - Nurse',
        'Nurse - Oncology Ambulatory',
        'Nurse - Oncology',
        'Rehab Assistant Basic',
        'Perioperative - Nurse',
        'Perioperative - Nurse Team Lead',
        'Physician - Lab',
        'DBC - HIM',
        'MH - Health Care Worker',
        'DBC - FSI (Interfaces)',
        'DBC - Scheduling',
        'Dietetic Student Basic',
        'Greaseboard',
        'HIM - Manager/Supervisor',
        'HIM - Clerk',
        'Infection Control Practitioner',
        'Nurse - Rural',
        'HIM - Document Correction',
        'Lactation Consultant',
        'Unit Clerk',
        'RadNet - Clerk',
        'MH - Nurse Supervisor',
        'DBC - Charge Services',
        'DBC - Registration',
        'Cardiology Technician',
        'Occupational Therapist Basic',
        'Occupational Therapy Student Basic',
        'PharmNet - Pharmacist Supervisor',
        'Physical Therapist Basic',
        'RadNet - Medical Imaging Technologist',
        'RadNet - Supervisor',
        'OB - Clerk',
        'Recreational Therapist Basic',
        'Music/Art Therapy Basic',
        'Nurse Practitioner',
        'PharmNet - Pharmacist Student',
        'DBC - SurgiNet',
        'Physician - Emergency',
        'Physician - Oncologist/Hematologist',
        'Perioperative - Anesthesia Resident',
        'DBC - FirstNet',
        'DBC - PowerChart',
        'Audiologist',
        'Child Life Specialist',
        'DBA Lite',
        'DBC - RadNet',
        'RadNet - View Only',
        'Resident',
        'Respiratory Therapy Student',
        'Social Worker Basic',
        'Speech Language Pathology Student Basic',
        'DBC - PharmNet Pharmacy Technician',
        'PharmNet - Pharmacy Buyer',
        'PharmNet - Pharmacy Technician',
        'Emergency - Greaseboard',
        'Finance Clerk - Accounts Receivable',
        'Perioperative - Scheduler',
        'Psychologist',
        'Psychology Student',
        'Perioperative - Anesthesia Assistant',
        'HIM - Auditor',
        'HIM - ROI',
        'Laboratory - Assistant with Reg',
        'Emergency - Registration Clerk',
        'Emergency - Unit Clerk',
        'Emergency - Health Care Assistant',
        'Midwife',
        'Data Quality',
        'PharmNet - Pharmacist',
        'Social Work Student Basic',
        'Physician - Allergist/Immunologist',
        'Physician - Cardiologist',
        'PharmNet -Pharmacy Technician Supervisor',
        'Physician - Orthopedics',
        'Physician - Physical Medicine Rehab',
        'Switchboard',
        'Quality and Risk Management',
        'Physician - Anesthesiologist Admin',
        'External - Provider',
        'Physician - Pediatric Hem/Onc/BMT',
        'Physician - Pediatric General Surgeon',
        'Physician - Psychiatrist',
        'Physician - Residential Care',
        'Physician - Sports Medicine',
        'Physician - Surgeon',
        'Physician - Transplant',
        'Finance Clerk - Accounts Payable',
        'Finance Supervisor - Accounts Payable',
        'PharmNet - Pharmacy Receiver',
        'Physician - OB/GYN',
        'Patient Care Manager',
        'Physician - Anesthesiologist',
        'Midwife Student',
        'OB - Nurse Postpartum',
        'Perioperative - Materials Management',
        'Perioperative - Nurse Cath Lab',
        'Perioperative - OR Management',
        'Registration - Forensics Clerk',
        'Resident Care Manager',
        'Medical Student',
        'Nurse - Acute Pain Service',
        'Scheduling Supervisor',
        'Scheduling - Clerk Advanced',
        'Speech Language Pathologist Basic',
        'User Provisioning',
        'Physician - Developmental Pediatrics',
        'Physician - Plastic Surgeon',
        'Physician - Primary Care',
        'Physician - Rheumatologist',
        'Physician - Urgent Care',
        'Physician - Palliative Care',
        'Physician - Pediatric Cardiologist',
        'Physician - Pediatrician',
        'Physician - Trauma Team Leader',
        'Physician - Genetics',
        'Physician - Nephrologist',
        'Physician - Endocrinologist',
        'Ethicist Basic',
        'Physician - Otolaryngologist',
        'Physician - PICU',
        'Physician - Podiatrist',
        'Physician - Respirologist',
        'Physician - RRT',
        'Physician - Urologist',
        'Physician - Vascular',
        'Physician - Colorectal Surgeon',
        'Physician - Dermatologist',
        'Physician - Float',
        'Physician - General Medicine',
        'Emergency - Nurse Practitioner',
        'Registration - Forensics Supervisor',
        'Perioperative - Tracking',
        'Health Care Assistant',
        'Rehab Assistant Student Basic',
        'OB - Greaseboard',
        'Patient Placement',
        'RadNet - Radiologist',
        'RadNet - Resident',
        'FirstNet View Only',
        'Genetic Counsellor',
        'Laboratory - Technologist with Reg',
        'PharmNet - Pharmacy Assistant',
        'Physical Therapy Student Basic',
        'DBC - PharmNet Pharmacist',
        'Dietitian Basic',
        'Registration - Clerk',
        'Physician - Gastroenterologist',
        'Physician - Infectious Disease',
        'Physician - Neurosurgeon',
        'Physician - Neurologist',
        'Physician - Ophthalmologist',
        'Physician - Geriatrician',
        'Physician - Critical Care',
        'Nurse Practitioner - Student',
        'View Only',
        'Physician - Rural Oncology',
        'HIM - Coding',
        'Physician - BMT Hematologist',
        'Laboratory - Assistant',
        'Laboratory - Technologist',
        'Private MOA',
        'Finance Clerk - Accounts Rec Cashier',
        'Physician - Critical Care with SaMacro',
        'Physician - Rural with SaMacro',
        'Ambulatory - Nurse with Reg/Sched',
        'Physical Therapist with Reg/Sched',
        'Nurse - Oncology Ambulatory with Reg/Sch',
        'Occupational Therapist with Reg/Sched',
        'Speech Language Pathologist with Reg/Sch',
        'Super Clerk',
        'Physician - NICU',
        'Physician - Oral Maxillofacial Surgery',
        'Research - Lev 1/Monitor/Auditor/Inspect',
        'MH - Nurse Emergency',
        'Perioperative - Nurse PAC',
        'Research - Level 2',
        'Research - Level 3',
        'Position Picker',
        'Nurse - IV Therapy',
        'DA2 Access Only',
        'OB - Hearing Screener',
        'Nurse - Outreach',
        'Resident/Fellow - Oncology Core',
        'OB - Nurse Community Liaison',
        'Perioperative - Nurse with SaAnesthesia',
        'Nurse - Supervisor ICU',
        'HIM - Clerk with Reg/Sched',
        'HIM - Manager/Supervisor with Reg/Sched',
        'Nurse - Patient Educator',
        'External - Institutional Entity',
        'External - Non-Provider',
        'MH - Occupational Therapist',
        'Physician - Medical Microbiologist',
        'Physician - Rural',
        'Decision Support',
        'PharmNet - VPC Pharmacy Technician',
        'DBC - BioMed',
        'Dietitian',
        'Dietetic Student',
        'Social Worker/Counsellor',
        'Speech Language Pathologist',
        'Speech Language Pathology Student',
        'Social Work/Counsellor Student',
        'Physician - Dentistry',
        'Spiritual Health',
        'Nurse Practitioner - Oncology',
        'Physical Therapist',
        'DBC - Devices',
        'Physical Therapy Student',
        'Physician - Cardiac Surgeon',
        'Physician - Thoracic Surgeon',
        'Oncology - Radiation Therapist/Physicist',
        'RadNet - Medical Imaging Tech Student',
        'Aboriginal/Indigenous',
        'PharmNet - Pharmacist CAP Informatics',
        'Music/Art Therapist',
        'Orthoptist',
        'Nurse - LTC',
        'Occupational Therapist',
        'Occupational Therapy Student',
        'Music/Art Therapy Student',
        'Perfusionist',
        'Perfusionist Student',
        'Recreation Therapist',
        'Rehab Assistant',
        'Rehab Assistant Student',
        'Dental Hygienist/Assistant',
        'Ethicist',
        'Ambulatory - Technician',
        'Laboratory - Transfusion Tech',
        'View and Print Only',
        'Audiology Student',
        'Recreation Therapy Student',
        'Ambulatory - Technician with Reg/Sched',
        'Private MOA with Reg/Sched',
        'Orthoptist with Reg/Sched',
        'COVID Screening Clerk',
        'Physician - Nephrology Fellow',
        'Physician - Pediatric Cardiac Surgeon',
        'Physician - Pediatric Infectious Disease',
        'Physician - Pediatric Nephrologist',
        'Physician - Pediatric Neurologist',
        'Physician - Pediatric Palliative Care',
        'Physician - Pediatric Respirologist',
        'Physician - Pediatric Rheumatologist',
        'Clinical Informatics',
        'Nurse Practitioner - OB',
        'Scheduling - Clerk Oncology',
        'Physician - Pediatric Endocrinologist',
        'Physician - Pediatric Gastroenterologist',
        'Physician - Biochemical Diseases',
        'Scheduling - Clerk PHC WQM 01',
        'Perioperative - Nurse APS',
        'Physician - Radiation Oncologist',
        'Physician - Gynecologic Oncologist',
        'Laboratory - Technologist with Reg/Sched',
        'Laboratory - Assistant with Reg/Sched',
        'Genetic Counsellor Student',
        'Physician - GPO',
        'Perioperative - Anesthesia Fellow II',
        'Ambulatory - Health Care Assistant',
        'Ambulatory - Nurse Medical Genetics',
        'HIM - Clerk Routing',
        'Physician - Adolescent Medicine',
        'Nurse - Pediatric',
        'Physician - GP OB/ED',
        'Scheduling - Clerk Medical Genetics',
        'Physician - Hematologist',
        'Orthoptist Student',
        'Laboratory - Scientist',
        'Patient Placement - BCH/BCW WQM',
        'Physician - Maternal Fetal Medicine',
        'Scheduling - Clerk BCH WQM',
        'Scheduling - Clerk BCW WQM',
        'Scheduling - Clerk BCH MH WQM',
        'Social Worker/Counsellor with Reg/Sched',
        'Scheduling - Clerk PHC WQM 02',
        'Child Life Specialist Student',
        'Scheduling - Clerk BCW CARE',
        'Research - Level 3 with Reg/Sched',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 88,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs89(db):
    """ Creating System Use (SU) code values - Codeset 48: Contributor system"""
    contributors = (
        '3M CODING AND REIMBURSEMENT',
        '3M Australia',
        'PROFIT_PRECOLL_AGENCY',
        'ESO OUT',
        '3M Canadian Coding and Reimbursement',
        '3M_32',
        'Australian Dental Association',
        'AMA',
        'ANS',
        'APA',
        'ASA',
        'ASCEND HiT L.L.C',
        'Technical info agency on hospitalisation',
        'BCB',
        'BCDX',
        'BMOH',
        'BOH',
        'CAP',
        'Care Management',
        'CARETRACKER',
        'CCEE',
        'CCH',
        'CCR Document System',
        'CDA Document System',
        'Centers for Disease Control',
        'CDI Possible DRG',
        'CDI Working DRG',
        'Cerner',
        'Cerner Direct',
        'Cerner Health',
        'Cerner LDAP',
        'CIHI',
        'Client',
        'CMOP - CDB',
        'Centers for Medicare & Medicaid Services',
        'CodeMaster Plus',
        'COVERMYMEDS',
        'CPA Contract DRG',
        'CPA Remit DRG',
        'DGIS',
        'IRDRG Dubai Health Authority',
        'DIACOS',
        '3M DialeCT',
        'DIMDI',
        'Discern Expert',
        'DMIX',
        'DOD',
        'DOD_EXPORT',
        'DOD Import',
        'DQR',
        'eBooking',
        'eHealth Ireland',
        'ESI DEFAULT',
        'ESO Default',
        'EXTERNAL-FHIR',
        'FDA',
        'GDDB',
        'G-DRG Organization',
        'Healthcare Association of New York State',
        'HCFA',
        'Healthe IDM',
        'HIM',
        'HIM Coding Merge',
        'HIM Dual Coding',
        'HIM Rule-Based Coding',
        'HIM Working DRG',
        'Health Level-7',
        'HLi',
        'HPO',
        'HSSGROUPER',
        'ICDPLUS',
        'Intelligent Medical Objects',
        'INEGI',
        'Infoway',
        'Info-X',
        'Interop',
        'Invision',
        'IOC',
        'KODIP',
        'MAYO',
        'MBSExtended',
        'Australian Dept of Health - MBS',
        'California Medical Assistance Program',
        'Medicode',
        'medicom',
        'MEDICUS',
        'Merge Medical Systems',
        'Military Health Systems',
        'Ministry of Health',
        'Ministry of Health, Ontario',
        'Monitoring',
        'Mosby',
        'Ministry of Health Spain',
        'Multum',
        'N/A',
        'Nanda',
        'NCI',
        'nCoder',
        'National E-Health Transition  Authority',
        'NHS',
        'NHSIA',
        'NRCL',
        'OMF Pay Period/Timesheet',
        'OMF PAYROLL FEED',
        'Optum Knowledge Components',
        'Pan American Health Organization',
        'PathLink',
        'PHARMA',
        'PMC',
        'PowerChart',
        'PROFILE',
        'Prosthesis - Department of Health',
        'PSCC',
        'ProView Image Server',
        'REGENSTRIEF',
        'ROE',
        'ROL',
        'SNRC',
        'RxHub',
        'SBOH',
        'SEBFR',
        'Spanish Health Ministry',
        'Siemens Healthcare',
        'SKL',
        'SNRC',
        'SSI',
        'SURESCRIPT',
        'SurgiNet',
        'TUSS',
        'Uniform Data System',
        'UMLS',
        'VIHA',
        'WHO',
        'PROFIT_COLL_AGENCY',
        'PYXIS',
        'SUNQUEST_2',
        'CCD_TO_CEPA',
        'SUNQUEST_3',
        'PROBLEMS',
        'EMPI_PHN_DTH_NV_SYS',
        'URL',
        'Bridge',
        'MUSE_PDF',
        'BEMC_PAT_CAT_ESI',
        'SUN_PAT_CAT_ESI',
        'BWMC_PAT_CAT_ESI',
        'CORA_PAT_CAT_ESI',
        'BWPC_PAT_CAT_ESI',
        'HIE',
        'COPATH',
        'Family History',
        'BEHAV_PAT_CAT_ESI',
        'IMH',
        'OCEAN_PAT_CAT_ESI',
        'WEBCONNECT',
        'ECET_UEP',
        'VARIANBILL',
        'INTELLICURE',
        'PIX_ADT_RES_SYS',
        'X12CLAIM',
        'XDS_RES_SYS',
        'POWERPATH',
        'SUNQUESTBILL',
        'ECET',
        'OPTIMUMOUTCOMESRCS',
        'ICSYSTEMSINC',
        'PRECOLLWEBCOLLECTESP',
        'X12CLAIM5010IMC',
        'MPI',
        'X12CLAIM5010',
        'MFN_ENGINE',
        'COLLWEBCOLLECTESTP',
        'COLLWEBCOLLECTESP',
        'ADT',
        'PPLSOFT',
        'WEBCOLLECTESP',
        'COLLECTIONS',
        'MGWEBCOLLECTESP',
        'Initiate MPI',
        'IMMUNIZATION',
        'SUNQUEST',
        'SELECTHEALTHUNDELIV',
        'RAD',
        'SIU',
        'KEYBANK',
        'ESCRIPTION',
        'CLAIRVIA',
        'AcuDose',
        'X12CLAIMMG',
        'LAB',
        'TRAIN_ADT_RRHOSPITAL',
        'CCDA_Visit_Summary_to_Portal',
        'CIRIUS',
        'APACHE',
        'PHARM_UPLOAD',
        'COMPUTRITION',
        'Computrion',
        'VARIAN',
        'CAUSE_OF_DEATH',
        'ARUP',
        'MUSE',
        'SYNGO',
        'ALLERGIES',
        'SAFETRACE',
        'TRAIN_ORM_ORU_CLINIC1',
        'IMMUNIZATION_ID',
        'CB_REG',
        'IMMUNIZATION_UT',
        'Exchange',
        'POWERPATH_2',
        'POWERPATH_TEST',
        'ECODE',
        'ePoint',
        'POWERSCRIBE',
        'TRAIN_ADT_CLINIC1',
        'TRAIN_ORM_ORU_RRHOSPITAL',
        'DISCHARGE ORM',
        'CODEFINDER',
        'CODEFINDER MCE',
        'CODE HCPCS/CPT',
        'CODE MCE HCPCS/CPT',
        'DRGFINDER',
        'DRGFINDER HCPCS/CPT',
        'HCPCS/CPTFINDER',
        'HCPCS/CPT (Dx only)',
        'HCPCS/CPT (Dx) Grp',
        'HCPCS/CPT ICD Grp',
        'APCFINDER',
        'INR',
        'CARDIOLOGY',
        'TRAIN-RRT',
        'TELCOR',
        'HDM',
        'TRAIN_ADT_INSTACARE',
        'TRAIN_ORM_ORU_INSTACARE',
        'IMAGE_FLAGS',
        'RAD_URL_3',
        'CB_REG_FLAGS',
        'RxHx',
        'ACCRETIVE',
        'CB_HELP2_ORU',
        'RAD_URL_2',
        'RXHISTORY',
        'BADDEBT',
        'RAD_URL',
        'NONRAD_URL',
        'EMPI_PHN_DTH_SYS',
        'CARDON',
        'MAMMO',
        'SYNGO_DISCRETE',
        'x12_1500',
        'HELP2_PDFS',
        'VITALS_UPLOAD',
        'EMPI_QRY_RSP_SYS',
        'EMPI_PHN_DTH_DIST_SYS',
        'HX_MRN_UTILITY',
        'EMPI_PHN_DTH_DIST_NV_SYS',
        'LIS_SYS',
        'TRN_SYS',
        'ADT_SYS',
        'ANC_SYS',
        'DFT_SYS',
        'MISC_SYS',
        'RIS_SYS',
        'SCH_SYS',
        'OMNICELL_SYS',
        'RDE_SYS',
        'RAD_SYS',
        'HX_LOAD_AUTH',
        'SC_SYS',
        'TEST_SYS',
        'TESTPC_SYS',
        'HX_DG_UPDT',
        'HX_HMRNEND_AUTH',
        'HX_NV',
        'PLR_SYS',
        'CARD_RAD_SYS',
        'CARD_SYS',
        'TRAINDB_SYS',
        'MASTER_SYS',
        'PHARMANET',
        'CARD_SYS_TEST',
        'CARD_ORM_SYS',
        'MIRAD_EXT_SYS',
        'GNT_LIS_SYS',
        'CAIS_SYS',
        'ONC_SYS',
        'RAD_ONC_SYS',
        'VPP_PDB',
        'LAB_EXT_SYS',
        'CARD_PACEORM_SYS',
        'CARD_PACEORU_SYS',
        'CARD_PACE_SYS',
        'HX_UPLOAD_RT_SYS',
        'HX_UPLOAD_BT_SYS',
        'MAGVIEW_SYS',
        'DOC_EXT_SYS',
        'CARD_SYS_DISCRETE',
        'NBS_LIS_SYS',
        'RAD_ONC_UPDT_SYS',
        'CARD_MUSE_SYS',
        'CARD_SYNGO_SYS',
        'IBE_PDF_SYS',
        'WWX',

    )
    with db.session() as session:
        for c in contributors:
            db_get_or_add_instance(
                session,
                CodeValue,
                code_set = 89,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )
        session.commit()


def SU_codevalues_cs106(db):
    """ Codeset 106: Activity Type """
    code_values = (
        'Patient Care',
        'Patient Activity',
        # 'PV Lab Charges',
        # 'Sunquest',
        # 'Training Codes',
        # 'CS Bill Only',
        # 'SafeTrace',
        # 'PowerPath',
        # 'Varian',
        # 'Charge Upload',
        # 'DME',
        # 'AFC DEFAULT BILL ITEM ADD-ON',
        # 'AFC GENERIC ADD-ON',
        # 'AFC BILL ITEM SPECIFIC ADD-ON',
        # 'Anesthesia Monitors',
        # 'Anesthesia Times',
        # 'Anatomic Pathology',
        'Asmt/Tx/Monitoring',
        # 'Blood Bank',
        # 'Blood Bank Communication',
        # 'Blood Bank Product',
        # 'Blood Bank Donor',
        'Bill Only',
        # 'Blood Gases',
        # 'Cardiovascular',
        # 'Nuclear Cardiac',
        # 'Vascular Ultrasound',
        # 'Case Integration',
        # 'Clinical Documentation',
        # 'COSTING',
        # 'Critical Care',
        # 'Cytogenetics',
        # 'Supplements',
        # 'Diet Communication',
        # 'Pediatric Formulas',
        # 'Pediatric Special Instructions',
        # 'Pediatric Supplements',
        # 'Snacks',
        # 'Oral Diets',
        # 'Tube Feeding',
        # 'Nutrition Asmt/Tx/Monitoring',
        'Diet Patient Care',
        # 'Milk Safety Orders',
        # 'Milk Safety Communication',
        # 'Discharge Orders',
        # 'Medication Related',
        # 'Non-Medication Related',
        # 'ED Encounter Charges',
        'Patient Education',
        'Intake and Output',
        # 'Supplies',
        # 'Genomics',
        # 'General Lab',
        # 'HLA',
        # 'Helix',
        # 'Sequencing',
        # 'Surveillance',
        # 'Care Manage',
        # 'Teach',
        # 'Direct Care',
        # 'Micro',
        # 'Ambulatory Patient Care',
        # 'Blood Bank Product Patient Care',
        # 'General Lab Patient Care',
        # 'Patient Care Medication',
        # 'Patient Care TDM',
        # 'Order Entry Detail',
        # 'Online Form',
        # 'Occupational Therapy',
        # 'Outreach Services',
        # 'Package',
        # 'Patient Request',
        # 'Pharmacy',
        # 'Physician Charges',
        # 'Person Management',
        # 'ProFile',
        # 'Physical Therapy',
        # 'Protocol',
        # 'Radiology',
        # 'External Referral',
        # 'Internal Referral',
        # 'Remote Patient Monitoring',
        # 'ROI Rejected',
        # 'Remote Report Distribution',
        # 'Discern Rule Order',
        # 'AMB Clinic Flag Order',
        # 'Scheduling',
        # 'Speech-Language Pathology',
        'Surgery',
        # 'Surgical Op',
        # 'Surgical Prsnl',
        # 'Surgery Document',
        # 'Surgery Caselevel',
        # 'Surgery Anesthesia',
        # 'Surgical Stage',
        # 'Surgery Acuity Level',
        'Task',
        'Admit/Transfer/Discharge',
        # 'Endocrine',
        'Home Care',
        # 'Urology Consults',
        # 'Urology Tx/Procedures',
        # 'Ventilator',
        # 'Wound Care',
        # 'Pulmonary Tx/Procedures',
        # 'ST Consults',
        # 'Discharge Instructions',
        # 'ENT Consults',
        # 'ENT Tx/Procedures',
        # 'Evaluation and Management',
        # 'Cardiology Consults',
        # 'Consults',
        # 'Nutrition Services Consults',
        # 'OB/GYN Consults',
        # 'OB/GYN Tx/Procedures',
        # 'Ortho Consults',
        # 'Orthopedic Supplies',
        # 'Orthopedic Tx/Procedures',
        # 'OT Consults',
        # 'OT Tx/Procedures',
        # 'Procedures',
        # 'PT Consults',
        # 'Pulmonology Consults',
        # 'RT Consults',
        # # 'Audiology Consults',
        # 'Audiology Tx/Procedures',
        # 'Cardiac Cath Lab',
        # 'Cardiac Tx/Procedures',
        # 'GI Consults',
        # 'GI Tx/Procedures',
        # 'Infection Control',
        # 'Infusion Therapy',
        # 'Neuro Consults',
        # 'Dietary Manager Consult',
        # 'Acitivites Consult',
        # 'Dentist Consults',
        # 'Dermatology Consults',
        # 'Diabetic Nurse Specialist Consults',
        # 'Endocrinology Consults',
        # 'Enterostomal Therapist Consults',
        # 'General Assessments',
        # 'General Surgery Consults',
        # 'Hematology Consults',
        # 'Home Health Consults',
        # 'Hospice Consults',
        # 'Interventional Radiology Consults',
        # 'Lactation Consultant Consults',
        # 'Massage Therapist Consults',
        # 'Neonatology Consults',
        # 'Nephrology Consults',
        # 'Neurosurgery Consults',
        # 'Pulmonary Rehabilitation Consults',
        # 'Radiation Therapy Consults',
        # 'Radiologic Consults',
        # 'Rheumatology Consults',
        # 'Social Services Consults',
        # 'Thoracic Surgery Consults',
        # 'Vascular Surgery Consults',
        # 'Immunology Consults',
        # 'Infectious Diseases Consults',
        # 'Internal Medicine Consults',
        # 'Nutritionist Consults',
        # 'Oncology Consults',
        # 'Ophthalmology Consults',
        # 'Optometry Consults',
        # 'Oromaxillofacial Surgery Consults',
        # 'Pain Management Consults',
        # 'Pastoral Care Consults',
        # 'Patient Activity Status',
        # 'Pediatric Consults',
        # 'Pediatric Surgery Consults',
        # 'Perinatology Consults',
        # 'Pharmacy Consults',
        # 'Physiatry Consults',
        # 'Plastic Surgery Consults',
        # 'POC Asmt/Tx/Monitoring',
        # 'Podiatry Consults',
        # 'Psychiatry Consults',
        # 'Psychologist Consults',
        # 'Psychotherapy Consults',
        # 'Anesthesiology Consults',
        # 'Cardiac Rehabilitation Consults',
        # 'Cardiothoracic Surgery Consults',
        # 'Case Management Consults',
        # 'Chiropractor Consults',
        # 'Communication Orders',
        # 'Continuous Asmt/Tx/Monitoring',
        # 'Counselor Consults',
        # 'Neuro Tx/Procedures',
        # 'Basic Care',
        # 'PT Tx/Procedures',
        # 'Transfer Activity',
        # 'Hygiene Activity',
        # 'Activity Daily Living',
        # 'SLP Consults',
        # 'SLP Tx/Procedures',
        # 'RT Tx/Procedures',
        # 'Infection Control Practitioner Consults',
        # 'CM Asmt/Tx/Monitoring',
        # 'Pastoral Asmt/Tx/Monitoring',
        # 'SW Asmt/Tx/Monitoring',
        # 'Provider Consults',
        # 'IV Therapy Consults',
        # 'Wound Care Consults',
        # 'Transitional Feeding',
        # 'Rule',
        # 'Radiation Oncology',
        # 'General Lab Bilirubin',
        # 'Discharge Laboratory Tests',
        # 'Activity Restrictions',
        # 'Imaging',
        # 'ED Charges',
        # 'Ambulatory POC',
        # 'Ambulatory Procedures',
        # 'Ambulatory Referrals',
        # 'Diet Instructions',
        # 'Cardiovascular Consults',
        # 'Pediatric Sedation',
        # 'Ophthalmology',
        # 'Maternity',
        # 'Nervous Sys',
        # 'Rad',
        # 'Injections',
        # 'Hospital Visits',
        # 'Integumentary',
        # 'Media/Diaphram',
        # 'Pulmonary',
        # 'Consultations',
        # 'Emergency Dept',
        # 'Nursing Faclty',
        # 'Prolong Serv',
        # 'Preventive Care',
        # 'Dermatological',
        # 'Respiratory',
        # 'Cardio',
        # 'Patho/Lab',
        # 'Female Genital',
        # 'Auditory',
        # 'Psychiatry',
        # 'Allerg/Clin Imm',
        # 'Chemotherapy',
        # 'Otorhinolaryngology',
        # 'Musculoskeletal',
        # 'Hemic/Lymphatic',
        # 'Digestive',
        # 'Urinary',
        # 'Male Genital',
        # 'Eye/Occular',
        # 'Cardiovas Med',
        # 'Neurology/Musc',
        # 'Office Visits',
        'Critical Care',
        # 'Special Serv',
        # 'Case Mgmt',
        # 'Physician Quality Reporting',
        # 'Supply',
        # 'Gastroenter',
        # 'Home Visits',
        # 'Dialysis',
        # 'Ophthal',
        # 'Conversion Charges',
        # 'Phy Med/Rehab',
        # 'ECET OT Tx/Procedures',
        # 'ECET PT Tx/Procedures',
        # 'ECET SLP Tx/Procedures',
        # 'AMB PROC MOD',
        # 'Cosmetic',
        # 'Retail',
        # 'Community/Speciality Pharmacy',
        # 'Automated Charging',
        # 'Dialysis Tx',
        # 'Dialysis Assessments',
        # 'Sleep Medicine',
        # 'Radiopharmaceuticals',
        # 'Neonatal Care',
        # 'Non Inv Vasc',
        # 'qShift Assessments',
        # 'Nutrition',
        # 'ASC Charges',
        # 'Molecular Genetics',
        # 'Cardiac ECG',
        # 'Nurse Collect POC',
        # 'IV Therapy',
        # 'Orthopedics',
        # 'Cardiac Echo',
        # 'ED Supplies',
        # 'Follow Up Consults',
        # 'Transfusion Medicine Consults',
        # 'Spine Precautions and Clearance',
        # 'Renal',
        # 'Cardiac Monitor',
        # 'Amb Scheduling',
        # 'Amb Asmt/Tx/Monitoring',
        # 'Lab Do Not Send',
        # 'AMB Patient Care',
        # 'AMB Wound Care',
        # 'PCP Charges',
        # 'Ambulatory Follow Up',
        # 'Ophthalmology Tx/Procedures',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 106,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs120(db):
    """ Codeset 120: Compression Code Value """
    code_values = (
        'No Compression',
        'OCF Compression',
    )

    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 120,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs261(db):
    """ Codeset 261: Encounter Status Codes """
    codes = (
        'Active',
        'Cancelled',
        'Cancelled Pending Arrival',
        'Discharged',
        'Hold',
        'Pending Arrival',
        'Preadmit',
        'Referred',
        'Rejected Pending Arrival',
        'Transferred',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 261,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs263(db):
    """ Codeset 263: Alias Pool """
    codes = (
        'BC PHN',
        'PharmaNet GPID',
        'Health Plan',
        'DEA',
        'Doctor Nbr',
        'Encounter Org',
        'External Id',
        'Insurance Code',
        'Media Alias',
        'SSN',
        'UPIN',
        'PERSONNEL PRIMARY IDENTIFIER',
        'PFT_STATEMENT_ALIAS',
        'PFT_CLAIM_ALIAS_POOL',
        'ORG UNIQUE IDENTIFIER',
        'YY Training MRN',
        'Financial Extract Org Alias',
        'Visit #',
        'NAIC',
        'Client Code',
        'Organization NPI',
        'PROVIDER_MESSAGING',
        'SureScripts Prescriber  Index',
        'CONSUMER_MESSAGING',
        'UNOS Donor ID',
        'LIS Filler Order ID',
        'LOCAL MESSAGING BW',
        'RESONANCE_ALIAS_POOL',
        'XDS_ALIAS_POOL',
        'National Provider Identifier',
        'MRN',
        'Texas DEA',
        'YY Training FIN',
        'NCT Number',
        'Encounter #',
        'Default Place of Service',
        'NAIC Org',
        'RxHx Order Event ID',
        'McKesson HMRN',
        'Sechelt Cerner HMRN',
        'FPH Cerner HMRN',
        'Powell River Meditech HMRN',
        'MSP #',
        'College #',
        'CW Cerner HMRN',
        'BCCA CAIS HMRN',
        'Employee #',
        'VA Carecast HMRN',
        'PHC Access Manager HMRN',
        'Company Code',
        'Hospital Approval #',
        'REB #',
        'Health Canada NOL #',
        'PositionPicker',
        'Purchase Order #',
        'Site #',
        'Primary Contact',
        'Secondary Contact',
        'VCHRI #',
        'NCT #',
        'BCCA Pharmacy Code',
        'Health Canada NOL Approval Date',
        'PharmaNet Physicians and Surgeons',
        'PharmaNet Dental Surgeons',
        'PharmaNet Pharmacists',
        'PharmaNet Registered Nurses',
        'Facility Transfer LGH and HOpe',
        'Facility Transfer PHC Acute',
        'External Filler ID',
        'Facility Transfer SPH Pain and OPD',
        'Facility Transfer PHC Elder Care',
        'Facility Transfer SPH PACH',
        'Facility Transfer PHC CDU and SPH HD',
        'Facility Transfer BCH BCW Acute',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 263,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs289(db):
    """ Codeset 289: Default Result Type """
    codes = (
        'Text',
        'Time',
        'Date and Time',
        'Read Only',
        'Count',
        'Provider',
        'ORC Select',
        'Inventory',
        'Bill Only',
        'Yes / No',
        'Date/Time/Time Zone',
        'Alpha',
        'Alpha and Freetext',
        'Multi-alpha and Freetext',
        'Numeric',
        'Interp',
        'Multi',
        'Date',
        'Freetext',
        'Calculation',
        'On-line Code Set',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 289,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper(),  # remove non-alphanumeric characters
                end_effective_dt_tm = datetime.fromisoformat(END_EFFECTIVE_DATE_ISO)
            )


def SU_codevalues_cs302(db):
    """ Codeset 302: Person Type """
    codes = (
        'Contributor System',
        'Freetext',
        'Numeric Name',
        'Organization',
        'Person',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 302,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs321(db):
    """ Codeset 321: Encounter Class """
    codes = (
        'Emergency',
        'Inpatient',
        'Outpatient',
        'Preadmit',
        'Historical',
    )
    with db.session() as session:
        for c in codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 321,
                definition = c,
                description = c,
                display = c,
                display_key = re.sub('[^0-9a-zA-Z]+', '', c).upper()  # remove non-alphanumeric characters
            )

def SU_codevalues_cs400(db):
    """ Codeset 400: Source Vocabulary
        The internal or external vocabulary or lexicon that contributed the string, e.g. ICD9, SNOMED, etc.
    """
    code_values = (
        'Patient Care',
        'Internal Codes',
        'ICD-10-CA',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_add_instance(
                session,
                CodeValue,
                code_set = 400,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )
        session.commit()


def SU_codevalues_cs4010(db):
    """ Creating System Use (SU) code values - Codeset 4010: Task Priority Code """
    priority_codes = (
        'NOW',
        'Routine',
        'STAT',
    )
    with db.session() as session:
        for s in priority_codes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 4010,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6000(db):
    """ Codeset 6000: Catalog Type """
    catalog_types = (
        'Ambulatory POC',
        'Ambulatory Procedures',
        'Ambulatory Procedure Scheduling',
        'Ambulatory Referrals',
        'Admit/Transfer/Discharge',
        'Audiology',
        'Blood Bank Donor',
        'Cardiology',
        'Cardiovascular',
        'Case Manager',
        'Charges',
        'Consults',
        'Conversion Charges',
        'Dialysis',
        'Nutrition Services',
        'Durable Medical Equipment',
        'Evaluation and Management',
        'ENT',
        'Environmental Services',
        'Gastroenterology',
        'Laboratory',
        'Home Care Plans/Pathways/Protocols',
        'Home Care',
        'Infection Control',
        'Materials Management',
        'NeuroDiagnostics',
        'Patient Care',
        'Occupational Therapy',
        'Ophthalmology',
        'Orthopedics',
        'Pastoral Care',
        'Person Management',
        'Pharmacy',
        'Physical Therapy',
        'Physician Charges',
        'Point of Care Testing',
        'Procedures',
        'Pulmonary Medicine',
        'Radiology',
        'Recreational Therapy',
        'Referral',
        'Respiratory Therapy',
        'Community/Speciality Pharmacy',
        'Discern Rule Order',
        'Scheduling',
        'Sleep Disorders',
        'Social Work',
        'Speech Therapy',
        'Supplies',
        'Surgery',
        'Urology',
        'Volunteer Services',
        "Women's Services",
    )
    with db.session() as session:
        for ct in catalog_types:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6000,
                definition = ct,
                description = ct,
                display = ct,
                display_key = re.sub('[^0-9a-zA-Z]+', '', ct).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6003(db):
    """ Codeset 6003: Order Action Type """
    code_values = (
        'Activate',
        'Add Alias',
        'Cancel',
        'Cancel/Discontinue',
        'Cancel and Reorder',
        'Clear Future Actions',
        'Collection',
        'Complete',
        'Void',
        'Demog Change',
        'Discontinue',
        'Discharge Order',
        'Future Discontinue',
        'History Order',
        'Modify',
        'Order',
        'Refill',
        'Renew',
        'Reschedule',
        'Restore',
        'Resume',
        'Resume/Renew',
        'Review',
        'Status Change',
        'Activate Student Order',
        'Suspend',
        'Transfer/Cancel',
        'Undo',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6003,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6004(db):
    """ Codeset 6004: Order Status """
    code_values = (
        'Canceled',
        'Completed',
        'Voided',
        'Discontinued',
        'Future',
        'Incomplete',
        'InProcess',
        'On Hold, Med Student',
        'Ordered',
        'Pending Complete',
        'Pending Review',
        'Suspended',
        'Transfer/Canceled',
        'Unscheduled',
        'Voided With Results',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6004,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6006(db):
    """ Codeset 6006: Communication Type """
    code_values = (
        'No Cosignature Required',
        'Cosignature Required',
        'Discern Expert',
        'Paper/Fax',
        'Proposed',
        'Phone',
        'Verbal',
        'Electronic',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6006,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6011(db):
    """ Codeset 6011: Mnemonic Type """
    code_values = (
        'Ancillary',
        'Brand Name',
        'Direct Care Provider',
        'C - Dispensable Drug Names',
        'Generic Name',
        'Y - Generic Products',
        'M - Generic Miscellaneous Products',
        'E - IV Fluids and Nicknames',
        'Outreach',
        'PathLink',
        'Primary',
        'Rx Mnemonic',
        'Surgery Med',
        'Z - Trade Products',
        'N - Trade Miscellaneous Products',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6011,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6014(db):
    """ Creating System Use (SU) code values - Codeset 6014: Reschedule Reason """
    reasons = (
        'Charted on Incorrect Patient',
        'Equipment/Supplies Unavailable',
        'Not appropriate at this time',
        'Patient Out on Pass',
        'Patient Unavailable',
        'Parent/Guardian Refused',
        'Task Duplication',
        'Charted Prior to Order Placed',
        'Change in Patient Status',
        'Order Cancelled by Provider',
    )
    with db.session() as session:
        for s in reasons:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6014,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs6024(db):
    """ Creating System Use (SU) code values - Codeset 6024: Message Subject """
    subjects = (
            'Call Back',
            'Complaint',
            'Medical Problem',
            'Medication Reaction',
            'Medication Renewal',
            'Personal',
            'Results Inqury',
            'Scheduling Question',
        )
    with db.session() as session:
        for s in subjects:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6024,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs6025(db):
    """ Creating System Use (SU) code values - Codeset 6025: Task Class """
    classes = (
            'Adhoc',
            'Continuous',
            'Non Scheduled',
            'PRN',
            'Scheduled',
        )
    with db.session() as session:
        for s in classes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6025,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs6026(db):
    """ Creating System Use (SU) code values - Codeset 6026 Task Type """
    task_types = (
            'Respiratory Care',
            'Respiratory Interventions',
            'SLP Evaluations',
            'Respiratory Medications',
            'SLP Outpatient Communication',
            'Music Therapy',
            'Palliative Care',
            'OT/SLP Tasks',
            'Respiratory Nursing',
            'Cardiac Home Nursing',
            'OT/PT Tasks',
            'Respiratory Therapy',
            'Print to PDF',
            'Assessment',
            'General Assessments',
            'Basic Care',
            'Ambulatory Care',
            'Social Services Consults',
            'Nutrition Services Consults',
            'Continuous Asmt/Tx/Monitoring',
            'Asmt/Tx/Monitoring',
            'Critical Care',
            'Admit/Discharge/Transfer',
            'Nutrition Support',
            'Nursing Tasks',
            'Ambulatory POC',
            'Unit Clerk Task',
            'Cardiac Nurse Consults',
            'Nursing System Task',
            'Periop/Inpatient Nursing Tasks',
            'Clinical Pharmacy',
            'Laboratory',
            'Medication',
            'Medication Reconciliation',
            'Notification',
            'Nurse Collect',
            'Sunquest Nurse Collect',
            'Order Notifications',
            'Patient Care',
            'Patient Education',
            'POC Asmt/Tx/Monitoring',
            'Emergency Care',
            'Pharmacy Verify',
            'Long Term Care',
            'PRN Response',
            'Transcription',
            'Transfusion'
        )
    with db.session() as session:
        for tt in task_types:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6026,
                definition = tt,
                description = tt,
                display = tt,
                display_key = re.sub('[^0-9a-zA-Z]+', '', tt).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs6027(db):
    """ Creating System Use (SU) code values - Codeset 6027 Task Activity """
    tast_activities = (
        'Abnormal Result',
        'Collect Specimen',
        'Chart IO Dialog',
        'Chart Results',
        'Chart Variance',
        'Complete Order',
        'Complete Personal',
        'Dr. Cosign',
        'Provider Letter Draft',
        'IPASS Action',
        'Medication History',
        'New Result',
        'Nurse Collect',
        'Nurse Review',
        'Order Plan',
        'Perform Result',
        'Letter',
        'Review Result',
        'Saved Document',
        'Sign Result',
        'View Only'
    )
    with db.session() as session:
        for ta in tast_activities:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6027,
                definition = ta,
                description = ta,
                display = ta,
                display_key = re.sub('[^0-9a-zA-Z]+', '', ta).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs6029(db):
    """ Creating System Use (SU) code values - Codeset 6029: Task Activity Class """
    classes = (
            'Anticipated Document',
            'Block Signature',
            'Paper Based Document',
            'PowerNote',
        )
    with db.session() as session:
        for s in classes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6029,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs6034(db):
    """ Creating System Use (SU) code values - Codeset 6034: Task Subtype Code """
    subtypes = (
            'Appointment Request Cancel',
            'Appointment Request',
            'Appointment Request Reschedule',
            'Care Coordination Referral',
            'Community Outreach',
            'Complex Care Management Referral',
            'Disease Management Referral',
            'Enrollment Outreach',
            'Initial Assessment',
            'Patient Follow-up',
            'Payer Outreach',
            'Pharmacy Follow-up',
            'Pharmacy Outreach',
            'Provider Follow-up',
            'Provider Outreach',
            'Wellness Referral',
            'General Message',
            'Match',
            'Non-match',
            'Patient Information',
            'Medication Refill',
            'Prescription Renewal',
            'Suspect Match',
        )
    with db.session() as session:
        for s in subtypes:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 6034,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs14024(db):
    """ Creating System Use (SU) code values - Codeset 14024: Task Status Reason Code """
    reasons = (
            'Task Charted with Form',
            'Task Charted as Done',
            'Task Charte as Not Done',
            'Analysis - Chart not Available',
            'Analysis - For Review',
            'Analysis - For Training Review',
            'Scan Reconciliation - Misc Hold',
            'Analysis - Review Completed',
            'Analysis - Traing Review Complete',
            'Analysis - See Note',
            'Analysis - Rework',
        )
    with db.session() as session:
        for s in reasons:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 14024,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs14219(db):
    """ Codeset 14219: Blood Bank Donor Procedure """
    code_values = (
        'Autologus Donation',
        'Direct Donation',
        'Apheresis Donation',
        'Phlebotomy',
        'Recruitment',
        'Reinstatement',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 14219,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs14281(db):
    """ Codeset 14281: Department Status """
    code_values = (
        'Canceled',
        'Completed',
        'Arrived',
        'Procedure Completed',
        'ED Review',
        'Procedure In Process',
        'Scheduled',
        'Signed',
        'Unsigned',
        'Verified',
        'Deleted',
        'Discontinued',
        'Initiated',
        'Collected',
        'Lab Activity Deleted',
        'Dispatched',
        'Final',
        'Received',
        'Result, Partial',
        'See Administer Order',
        'Result, Preliminary',
        'Lab Results Deleted',
        'Scheduled',
        'Stain',
        'Susceptibility',
        'On Hold',
        'Ordered',
        'Partial Fill',
        'Pending Collection',
        'Exam Completed',
        'Exam Ordered',
        'Exam Removed',
        'Exam Replaced',
        'Exam Started',
        'Refill',
        'Historical',
        'Rx History Incomplete',
        'On File',
        'On Hold',
        'Transfer Out',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 14281,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )


def SU_codevalues_cs14766(db):
    """ Creating System Use (SU) code values - Codeset 14024: Task Status Reason Code """
    code_values = (
            'Parent',
            'Guardian',
            'Spouse',
            'Sibling',
            'Friend',
            'Grandparent',
            'Other Relative',
            'Self',
            'Police',
            'Co-worker',
            'Child',
        )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 14766,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs14767(db):
    """ Codeset 14767: Accommodation Reasons """
    code_values = (
            'Security',
            'Medically Necessary',
            'Patient Request',
            'Psychiatric Concerns',
            'Senior Administration Request',
            'To Be Moved When Bed Available',
            'Equipment in Room',
            'INfection Control',
            'Private Only',
        )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 14767,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs16389(db):
    """ Codeset 16389: DCP Clinical Category """
    code_values = (
            'Activity',
            'Allergies',
            'Admit/Transfer/Discharge',
            'Consults/Referrals',
            'Diagnosis',
            'Diagnostic Tests',
            'Diet/Nutrition',
            'Continuous Infusions',
            'Laboratory',
            'Medications',
            'Supplies',
            'Patient Care',
            'Procedures',
            'Status',
            'Respiratory',
            'Allied Health',
            'Blood Products',
            'Communication Orders',
            'Non Categorized',
        )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 16389,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs17969(db):
    """ Codeset 17969: Advanced Beneficary Note (ABN) Status Code """
    Statuses = (
        'Not Required',
        'On File',
        'Required & Missing',
        'On File - Self Pay',
        'On File - Refused to Sign',
        'On File - Refused Service',
        'Review Required',
    )
    with db.session() as session:
        for s in Statuses:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 17969,
                definition = s,
                description = s,
                display = s,
                display_key = re.sub('[^0-9a-zA-Z]+', '', s).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs18309(db):
    """ Creating System Use (SU) code values - Codeset 6027 Task Activity """
    tast_activities = (
        'Dialysis',
        'Intermittent',
        'Irrigation',
        'IV',
        'Med',
        'PCA',
        'Sliding Scale',
        'Taper',
        'Titrate',
        'TPN',
    )
    with db.session() as session:
        for ta in tast_activities:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 18309,
                definition = ta,
                description = ta,
                display = ta,
                display_key = re.sub('[^0-9a-zA-Z]+', '', ta).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs22589(db):
    """ Codeset 22589: Alternate Level of Care """
    code_values = (
        'Home Health',
        'Specialized/Tertiary MH & Addiction',
        'Transitional Care Unit or Convalescent',
        'Assisted Living or Supportive Housing',
        'Family or Social Services',
        'Adequate Housing',
        'Mental Health & Addiction Community',
        'Assessment in Progress - RC',
        'Companion',
        'Acute Rehabilitation Facility or Unit',
        'Assessment in Progress - Other',
        'Hospice',
        'Residential Care',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 22589,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs255090(db):
    """ Creating System Use (SU) code values - Codeset 255090 Charting Agent """
    charting_agents = (
        'apache',
        'DocSet',
        'PowerForm',
        'Task Completion Service',
    )
    with db.session() as session:
        for agent in charting_agents:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 255090,
                definition = agent,
                description = agent,
                display = agent,
                display_key = re.sub('[^0-9a-zA-Z]+', '', agent).upper()   # remove non-alphanumeric characters
            )


def SU_codevalues_cs4002164(db):
    """ Codeset 4002164: Offset Minute Type Code"""
    code_values = (
        'Acknowledge Results',
        'MDI BackWard Minutes',
        'MDI Forward Minutes',
    )

    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 4002164,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()  # remove non-alphanumeric characters
            )
        session.commit()

def SU_codevalues_cs4002509(db):
    """ Codeset 4002509: Rounding Rule code """
    code_values = (
        'Automatic rounding',
        'Down Nearest hundred',
        'Down Nearest hundredth',
        'Down Nearest tenth',
        'Down Nearest thousandth',
        'Down Nearest ten',
        'Down Nearest whole number',
        'Manually Entered',
        'Nearest hundred',
        'No rounding',
        'Nearest hundredth',
        'Nearest tenth',
        'Nearest thousandth',
        'Nearest ten',
        'Nearest whole number',
        'Up Nearest hundred',
        'Up Nearest hundredth',
        'Up Nearest tenth',
        'Up Nearest thousandth',
        'Up Nearest ten',
        'Up Nearest whole number',
        'Nearest Twentyfive',
        'Nearest Twenty',
        'Nearest Fifty',
        'Nearest Five',
        'Nearest Seventyfive',
        'Nearest Two',
        'Nearest OnehundredForty',
        'Nearest Thirtyeight',
        'Nearest Five Hundred',
        'Nearest Half of Whole Number',
        'Nearest Six',
        'Nearest Two and One Half',
        'Nearest TwentyOne',
        'Nearest One and One Quarter',
        'Nearest One-eighth',
        'Nearest One-twentieth',
        'Nearest hundred and fifty',
        'Nearest Thirty',
        'Nearest One-fourth',
        'Nearest Forty',
    )
    with db.session() as session:
        for cv in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 4002509,
                definition = cv,
                description = cv,
                display = cv,
                display_key = re.sub('[^0-9a-zA-Z]+', '', cv).upper()   # remove non-alphanumeric characters
            )
        session.commit()



def init_code_set_(db):

    # create_SU_codeset_(db)   # Creating the code sets in code_value_set table

    # SU_codevalues_cs2(db)
    # SU_codevalues_cs48(db)
    # SU_codevalues_cs3(db)
    # SU_codevalues_cs8(db)

    # SU_codevalues_cs54(db)

    # SU_codevalues_cs10()
    # SU_codevalues_cs16()
    # SU_codevalues_cs19()

    # SU_codevalues_cs23()
    # SU_codevalues_cs24()
    # SU_codevalues_cs34()

    # SU_codevalues_cs53()
    # SU_codevalues_cs68()
    # SU_codevalues_cs69()
    # SU_codevalues_cs71()
    # SU_codevalues_cs79()
    # SU_codevalues_cs87()
    # SU_codevalues_cs88()
    # SU_codevalues_cs89()

    # SU_codevalues_cs106()
    # SU_codevalues_cs120()

    # SU_codevalues_cs261()
    # SU_codevalues_cs263()
    # SU_codevalues_cs289()

    # SU_codevalues_cs302()
    # SU_codevalues_cs321()

    # SU_codevalues_cs400()

    # SU_codevalues_cs4010()

    # SU_codevalues_cs6000()
    # SU_codevalues_cs6003()
    # SU_codevalues_cs6004()
    # SU_codevalues_cs6006()
    # SU_codevalues_cs6011()
    # SU_codevalues_cs6014()
    # SU_codevalues_cs6024()
    # SU_codevalues_cs6025()
    # SU_codevalues_cs6026()
    # SU_codevalues_cs6027()
    # SU_codevalues_cs6029()
    # SU_codevalues_cs6034()

    # SU_codevalues_cs18309()

    # SU_codevalues_cs14024()
    # SU_codevalues_cs14219()
    # SU_codevalues_cs14281()
    # SU_codevalues_cs14766()
    # SU_codevalues_cs14767()

    # SU_codevalues_cs16389()
    # SU_codevalues_cs17969()

    # SU_codevalues_cs22589()

    # SU_codevalues_cs4002164()
    
    # SU_codevalues_cs4002509()
    pass
