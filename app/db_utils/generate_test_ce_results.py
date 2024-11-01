from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, select

from core.models.db_base import engine
from core.models.db_clinical_event import ClinicalEvent
from core.dbutils.db_get_or_create import db_get_or_create
from core.dbutils.db_uar_get_funcs import uar_get_code_by


def generate_ce_results():

    tm_now = datetime.now()
    tm_1 = tm_now - timedelta(hours=4) 
    tm_2 = tm_now - timedelta(hours=8) 


    event_times = [
        # Result1_dttm,     Result2_dttm,           Result3_dttm
        tm_now,             tm_1,                   tm_2    
    ] 

    results_list = [
        ['Temperature', '37.5', None, '37.0'],
        ['Heart Rate', '100', '98', None],
        ['Respiratory Rate', '22',  None, '16' ],
        ['Systolic Blood Pressue', '120', None, '110'],
        ['Diastolic Blood Pressure', '80', None, '75'],
        
        ['Measured Weight', None, '65', None],
        ['Measured Length', None, '175', None],
        
    ]

    with Session(engine) as session:
        
        for results in results_list:
            ec_disp = results[0]
            for i in range(1, 4):
                if results[i] is not None:
                    # Res1
                    db_get_or_create(
                        session,
                        ClinicalEvent,

                        person_id = 1,
                        encntr_id = 1,

                        event_cd                = uar_get_code_by('DISPLAY', 72, ec_disp),
                        event_class_cd          = uar_get_code_by('DISPLAY', 53, 'NUM'),
                        event_end_dt_tm         = event_times[i-1],
                        event_id                = 0,
                        event_reltn_cd          = uar_get_code_by('DISPLAY', 24, 'R'),
                        event_tag               = ec_disp,
                        performed_dt_tm         = event_times[i-1],
                        record_status_cd        = uar_get_code_by('DISPLAY', 48, 'Active'),
                        result_status_cd        = uar_get_code_by('DISPLAYKEY', 8, 'AUTHVERIFIED'),
                        result_val              = results[i],
                        updt_id                 = 5

                    )


if __name__ == "__main__":
    # generate_ce_results()
    pass