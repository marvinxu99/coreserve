import re
from sqlalchemy.orm import Session
from core.dbutils.db_uar_get_funcs import uar_get_code_by

from core.models.db_base import engine
from core.models.db_nomenclature import Nomenclature
from core.dbutils.db_utils import convert_to_key


nomen_data = [
        'nomenclature example',
        'Yes',
        'No',
        'Feed Winter',
        'Feed Wesley',
        'Winter',
        'Wesley',
        'One cup, twice a day',
        'Two cups, twice a day',
        'Three cups, twice a day',
]

def load_nomenclatures():
    
    temp_updt_id = 5

    with Session(engine) as session:

        for nomen in nomen_data:
                    
            kw = {
                'source_string_keycap'  : nomen.upper(),
                'source_string'         : nomen,
                'source_vocabulary_cd'  : uar_get_code_by('DISPLAYKEY', 400, 'PATIENTCARE')
            }
            # check if item aleady exists
            instance = session.query(Nomenclature).filter_by(**kw).one_or_none()
            if not instance:
                instance = Nomenclature(**kw)
                instance.short_string = nomen
                instance.contributor_system_cd = uar_get_code_by('DISPLAYKEY', 89, 'WWX')
                instance.updt_id = temp_updt_id
                
                session.add(instance)
                session.flush([instance])
                instance.nom_ver_grp_id = instance.nomenclature_id

        session.commit()


if __name__ == "__main__":
    load_nomenclatures()
    pass