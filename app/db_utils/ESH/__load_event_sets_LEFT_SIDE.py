import re
from sqlalchemy.orm import Session

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.models.db_v1_event_set_code import V1EventSetCode
from core.models.db_v1_event_set_canon import V1EventSetCanon
from core.models.db_v1_event_set_explode import V1EventSetExplode
from core.dbutils.db_uar_get_funcs import uar_get_code_by
from core.dbutils.db_utils import convert_to_key

"""
Evet sets (ES) live in:
    - codeset 93
    - v1_event_set_code table:  one to one mapping to codeset 93
"""

event_set_data = [
    # Parent/Folder                     # ES Name                   # Display                   # Definition           # Event_code
    ("Furry Friend Care/Monitoring",   (
                                        ('Name of Fur Friend',       'Name of Fur Friend',       'Name of Fur Friend',  'Name of Fur Friend'),
                                        ('Types of Dog Food',        'Types of Dog Food',        'Types of Dog Food',   'Types of Dog Food'),
                                        ('Amount to Feed',           'Amount to Feed',           'Amount to Feed',      'Amount to Feed'),
                                        ('Weight, Measured',         'Weight, Measured',         'Weight, Measured',    'Weight, Measured'),
                                        ('Weight, Estimated',        'Weight, Estimated',        'Weight, Estimated',   'Weight, Estimated'),
                                    )),

]

def _load_event_sets_LEFT_SIDE():
    """
    Load event sets to the left/top of ESH hierarchy
    """
    # TODO: to remove, FOR TEST ONLY
    temp_updt_id = 5

    with Session(engine) as session:       

        for event_set in event_set_data:
            
            # (1) Check if parent event set exists
            parent_event_set_cd = uar_get_code_by('DISPLAYKEY', 93, convert_to_key(event_set[0]))
            if parent_event_set_cd is not None:

                # Check if all the child event sets exist? If not, create them
                for seq, primitive_es in enumerate(event_set[1]):
                    # (1) Update to code_set 93
                    kw = {
                        'code_set'      : 93,
                        'definition'    : primitive_es[0],
                        'display'       : primitive_es[1],
                        'description'   : primitive_es[2],
                        'display_key'   : convert_to_key(primitive_es[1]),  # remove non-alphanumeric characters
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
                        session.flush([v1_esc])                

                    # (3) Update to v1_event_set_canon table
                    kw = {
                        'event_set_cd'              : v1_esc.event_set_cd,  
                        'parent_event_set_cd'       : parent_event_set_cd,  
                    }
                    # Check if the event set exists in v1_event_set_canon
                    es_canon = session.query(V1EventSetCanon).filter_by(**kw).one_or_none()
                    if not es_canon:
                        es_canon = V1EventSetCanon(**kw)
                        es_canon.event_set_collating_seq = seq
                        es_canon.event_set_explode_ind = True
                        es_canon.event_set_status_cd = uar_get_code_by('DISPLAY', 48, 'Active') 
                        es_canon.updt_id = temp_updt_id
                        session.add(es_canon)
                        session.add(es_canon)

                    # (4) Update to the v1_event_set_explode table
                    kw = {
                        'event_set_cd'   : v1_esc.event_set_cd,  
                        'event_cd'       : uar_get_code_by('DISPLAYKEY', 72, convert_to_key(primitive_es[3])),  
                    }
                    # Check if the event set exists in v1_event_set_code table
                    v1_es_explode = session.query(V1EventSetExplode).filter_by(**kw).one_or_none()
                    if not v1_es_explode:
                        v1_es_explode = V1EventSetExplode(**kw)
                        v1_es_explode.event_set_collating_seq = seq
                        v1_es_explode.updt_id = temp_updt_id
                        session.add(v1_es_explode)

        session.commit()


if __name__ == "__main__":
    _load_event_sets_LEFT_SIDE()
    pass