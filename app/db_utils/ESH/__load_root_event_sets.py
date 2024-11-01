import re
from sqlalchemy.orm import Session

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.models.db_v1_event_set_code import V1EventSetCode
from core.models.db_v1_event_set_canon import V1EventSetCanon
from core.dbutils.db_get_or_create import db_get_or_create
from core.dbutils.db_uar_get_funcs import uar_get_code_by
from core.dbutils.db_utils import convert_to_key

"""
Evet sets (ES) live in:
    - codeset 93
    - v1_event_set_code table:  one to one mapping to codeset 93
"""


def _load_root_event_sets():
    """
        ALL EVENT SETS
                +---- ALL RESULT SECTIONS
                            + ----- ALL SERVICE SECTIONS
                                        + ---- OTHER RESULTS
                            + ----- ALL DOCUMENT SECTIONS
                                        + OTHER DOCUMENTS

                +---- ALL SPECIALTY SECTIONS
                            + Working View Secctions
                            + SYSTEM USE EVENTS
    """

    root_ES_data = [
        # Name                      # Display                   # Definition
        ('ALL EVENT SETS',          'ALL EVENT SETS',           'ALL EVENT SETS'),
        ('ALL RESULT SECTIONS',     'ALL RESULT SECTIONS',      'ALL RESULTS SECTIONS'),
        ('ALL SERVICE SECTIONS',    'ALL SERVICE SECTIONS',     'ALL SERVICE SECTIONS'),
        ('OTHER RESULTS',           'OTHER RESULTS',            'OTHER RESULTS'),
        ('ALL DOCUMENT SECTIONS',   'ALL DOC SECTS',            'ALL DOCUMENT SECTIONS'),
        ('OTHER DOCUMENTS',         'OTHER DOCUMENTS',          'OTHER DOCUMENTS'),
        ('ALL SPECIALTY SECTIONS',  'ALL SPECIALTY SECTIONS',   'ALL SPECIALTY SECTIONS'),
        ('Working View Sections',  'Working View Sections',     'Working View Sections'),
        ('SYSTEM USE EVENTS',       'SYSTEM USE EVENTS',        'SYSTEM USE EVENTS'),
    ]

    # TODO: to remove, FOR TEST ONLY
    temp_updt_id = 5

    v1_esc_rows = []

    with Session(engine) as session:       

        for event_set in root_ES_data:
            
            # (1) Update to code_set 93
            kw = {
                'code_set'      : 93,
                'definition'    : event_set[0],
                'display'       : event_set[1],
                'description'   : event_set[2],
                'display_key'   : convert_to_key(event_set[1]),  # remove non-alphanumeric characters
            }
            # check if the event set exists in codeset 93
            cv_event_set = session.query(CodeValue).filter_by(**kw).one_or_none()
            if not cv_event_set:
                cv_event_set = CodeValue(**kw)
                cv_event_set.updt_id = temp_updt_id,
                session.add(cv_event_set)
                session.flush([cv_event_set])

            # (2) Update to v1_event_set_code table
            kw = {
                'event_set_cd'              : cv_event_set.code_value,  
                'event_set_cd_definition'   : cv_event_set.definition,
                'event_set_cd_descr'        : cv_event_set.description,
                'event_set_cd_disp'         : cv_event_set.display,
                'event_set_cd_disp_key'     : cv_event_set.display_key,
                'event_set_name'            : cv_event_set.definition,
                'event_set_name_key'        : convert_to_key(cv_event_set.definition),
                'event_set_name_upper_vc'   : cv_event_set.definition.upper(),
            }
            # Check if the event set exists in v1_event_set_code table
            v1_esc = session.query(V1EventSetCode).filter_by(**kw).one_or_none()
            if not v1_esc:
                v1_esc = V1EventSetCode(**kw)
                v1_esc.updt_id = temp_updt_id
                session.add(v1_esc)
            v1_esc_rows.append(v1_esc)

        session.flush(v1_esc_rows)

        #------------------------------------------
        # ALL EVENT_SETS => ALL RESULT SECTIONS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[1].event_set_cd,
            event_set_collating_seq     = 0,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[0].event_set_cd,  
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL RESULT SECTIONS => ALL SERVICE SECTIONS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[2].event_set_cd,
            event_set_collating_seq     = 0,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[1].event_set_cd,  
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL RESULT SECTIONS => ALL SERVICE SECTIONS => OTHER RESULTS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[3].event_set_cd,
            event_set_collating_seq     = 99,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[2].event_set_cd,  
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL RESULT SECTIONS => ALL DOCUMENT SECTIONS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[4].event_set_cd,
            event_set_collating_seq     = 1,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[1].event_set_cd,  
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL RESULT SECTIONS => ALL DOCUMENT SECTIONS => OTHER DOCUMENTS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[5].event_set_cd,
            event_set_collating_seq     = 99,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[4].event_set_cd, 
        )
        session.add(new_es_canon)

        #------------------------------------------
        # ALL EVENT_SETS => ALL SPECIALTY SECTIONS 
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[6].event_set_cd,
            event_set_collating_seq     = 1,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[0].event_set_cd,    # ALL EVENT SETS
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL SPECIALTY SECTIONS => Working View Secctions
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[7].event_set_cd,
            event_set_collating_seq     = 0,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[6].event_set_cd,    # ALL EVENT SETS
        )
        session.add(new_es_canon)

        # ALL EVENT_SETS => ALL SPECIALTY SECTIONS => SYSTEM USE EVENTS
        new_es_canon = V1EventSetCanon(
            event_set_cd                = v1_esc_rows[8].event_set_cd,
            event_set_collating_seq     = 99,
            event_set_explode_ind       = True,
            event_set_status_cd         = uar_get_code_by('DISPLAY', 48, 'Active'),
            parent_event_set_cd         = v1_esc_rows[6].event_set_cd,    # ALL EVENT SETS
        )
        session.add(new_es_canon)

        session.commit()


def _load_event_sets():
    test_es_data = [


    ]
    
    with Session(engine) as session:
        for ec_display in test_es_data:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 72,
                definition = ec_display,
                description = ec_display,
                display = ec_display,
                display_key = re.sub('[^0-9a-zA-Z]+', '', ec_display).upper()  # remove non-alphanumeric characters
            )


if __name__ == "__main__":
    _load_root_event_sets()
    pass