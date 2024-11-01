import re
from sqlalchemy.orm import Session
from core.dbutils.db_uar_get_funcs import uar_get_code_by

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.models.db_nomenclature import Nomenclature
from core.models.db_discrete_task_assay import DiscreteTaskAssay
from core.dbutils.db_utils import convert_to_key


DTA_data = [
        'DTA Example',
        'Name of Fur Friend',
        'Types of Dog Food',
        'Amount to Feed',
        'Weight, Measured',
        'Weight, Estimated',
        "FiO2",
        "Temperature",
        "Heart Rate",
        "Walk (Minutes)",
        "Walk Distance (Meters)",
]

def __update_DTA_event_codes():
    
    temp_updt_id = 5

    with Session(engine) as session:

        for dta_mnemonic in DTA_data:
                    
            # (1) Check if DTA exists in codeset 14003
            kw = {
                'code_set'      : 14003,
                'display_key'    : convert_to_key(dta_mnemonic),
            }
            # check if item already exists
            cs14003_dta = session.query(CodeValue).filter_by(**kw).one_or_none()
            if cs14003_dta is not None:

                # (2) Check if DTA exists in the discrete_data_assay table
                kw = {
                    'task_assay_cd'      : cs14003_dta.code_value,
                }
                # check if item already exists
                dta_in_tbl = session.query(DiscreteTaskAssay).filter_by(**kw).one_or_none()
                if dta_in_tbl is not None:                  
                    event_code_cd = uar_get_code_by('DISPLAYKEY', 72, convert_to_key(dta_mnemonic))
                    if event_code_cd is not None:
                        dta_in_tbl.event_cd = event_code_cd
                        session.add(dta_in_tbl)

        session.commit()


if __name__ == "__main__":
    __update_DTA_event_codes()
    pass
