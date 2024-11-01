import re
from sqlalchemy.orm import Session
from core.dbutils.db_uar_get_funcs import uar_get_code_by

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.models.db_nomenclature import Nomenclature
from core.models.db_discrete_task_assay import DiscreteTaskAssay
from core.dbutils.db_utils import convert_to_key


dta_data = [
        'DTA Example',
        'Name of Fur Friend',
        'Types of Dog Food',
        'Amount to Feed',
        'Weight, Measured',
        'Weight, Estimated',
        'FiO2',
        "Heart Rate",
        "Temperature",
        "Walk (Minutes)",
        "Walk Distance (Meters)",
        "Sleep (Hours)",
        "Measured Urine Output",
        "Estimated Urine Output",
        "School Training (Minutes)",
        "Home Training (Minutes)",
]

def load_DTAs():
    
    temp_updt_id = 5

    with Session(engine) as session:

        for dta_mnemonic in dta_data:
                    
            # (1) Update to DTA codeset 14003
            kw = {
                'code_set'      : 14003,
                'display_key'    : convert_to_key(dta_mnemonic),
            }
            # check if item already exists
            cs14003_dta = session.query(CodeValue).filter_by(**kw).one_or_none()
            if not cs14003_dta:
                cs14003_dta = CodeValue(**kw)
                cs14003_dta.display = dta_mnemonic
                cs14003_dta.definition = dta_mnemonic
                cs14003_dta.description = dta_mnemonic
                cs14003_dta.updt_id = temp_updt_id                
                session.add(cs14003_dta)
                session.flush([cs14003_dta])

            # (2) Update to discrete_data_assay table
            kw = {
                'task_assay_cd'      : cs14003_dta.code_value,
            }
            # check if the DTA already exists
            dta_in_tbl = session.query(DiscreteTaskAssay).filter_by(**kw).one_or_none()
            if dta_in_tbl is None:
                dta_in_tbl = DiscreteTaskAssay(**kw)
                dta_in_tbl.mnemonic = dta_mnemonic
                dta_in_tbl.mnemonic_key_cap = dta_mnemonic.upper()
                dta_in_tbl.description = dta_mnemonic
                dta_in_tbl.updt_id = temp_updt_id 
                session.add(dta_in_tbl)
                session.flush([dta_in_tbl])
            else:
                dta_in_tbl.description = dta_in_tbl.mnemonic

                
            # (3) Associate to the event code if it exists
            if dta_in_tbl.event_cd == 0:
                event_code_cd = uar_get_code_by('DISPLAYKEY', 72, convert_to_key(dta_mnemonic))
                if event_code_cd is not None:
                    dta_in_tbl.event_cd = event_code_cd
                    session.add(dta_in_tbl)

        session.commit()


def dta_update_description():

    with Session(engine) as session:
                   
        # (1) Update to DTA codeset 14003
        kw = {
            'code_set'      : 14003,
        }
        # check if item already exists
        dta_list = session.query(CodeValue).filter_by(**kw).all()
        for dta in dta_list:
            # Update to discrete_data_assay table
            kw = {
                'task_assay_cd'      : dta.code_value
            }
            # check if the DTA already exists
            dta_in_tbl = session.query(DiscreteTaskAssay).filter_by(**kw).one_or_none()
            if dta_in_tbl:
                dta_in_tbl.description = dta_in_tbl.mnemonic

        session.commit()


if __name__ == "__main__":
    # load_DTAs()
    dta_update_description()
    pass
