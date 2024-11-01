import re
from sqlalchemy.orm import Session

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.dbutils.db_get_or_create import db_get_or_create
from core.dbutils.db_utils import convert_to_key
from core.models.db_v1_event_code import V1EventCode

"""
Evet codes (EC) live in:
    - codeset 72
    - v1_event_code table:   one to one mapping to codeset 72
"""

EC_data = [
        'Temperature',
        'Heart Rate',
        'Respiratory Rate',
        'Systolic Blood Pressue',
        'Diastolic Blood Pressure',
        
        'Measured Weight',
        'Measured Length',
        'Calculated BMI',
        'Asjusted BMI',

        'Alpha',
        'ALphaAndFreeTExt',
        
        'Name of Fur Friend',
        'Types of Dog Food',
        'Amount to Feed',
        'Weight, Measured',
        'Weight, Estimated',
        "FiO2",
]

def _load_event_codes():
    
    temp_updt_id = 5

    with Session(engine) as session:

        for ec_disp in EC_data:
        
            # (1) Update code_set 72
            kw = {
                'code_set'      : 72,
                'definition'    : ec_disp,
                'display'       : ec_disp,
                'description'   : ec_disp,
                'display_key'   : convert_to_key(ec_disp),  # remove non-alphanumeric characters
            }
            # check if the event set exists in codeset 72
            cv_72ec = session.query(CodeValue).filter_by(**kw).one_or_none()
            if not cv_72ec:
                cv_72ec = CodeValue(**kw)
                cv_72ec.updt_id = temp_updt_id
                session.add(cv_72ec)
                session.flush([cv_72ec])

            # (2) Update to the v1_event_code table
            kw = {
                'event_cd'              : cv_72ec.code_value,
                'event_cd_definition'   : cv_72ec.definition, 
                'event_cd_descr'        : cv_72ec.description,
                'event_cd_disp'         : cv_72ec.display,
                'event_cd_disp_key'     : cv_72ec.display_key
            }
            v1ec_ec = session.query(V1EventCode).filter_by(**kw).one_or_none()
            if not v1ec_ec:
                v1ec_ec = V1EventCode(**kw)
                v1ec_ec.updt_id = temp_updt_id
                session.add(v1ec_ec)

        session.commit()


if __name__ == "__main__":
    _load_event_codes()
    pass