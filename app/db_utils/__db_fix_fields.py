from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql.expression import and_, select, desc, label
from datetime import datetime

from core.models.db_base import engine
from core.models.db_code_value import CodeValue
from core.wwx.data_role import END_EFFECTIVE_DATE_ISO


def db_update_CV_fields(codeset):
    """
        Fix the values of the end_effective_dt_tm column of codeset 106
    """
    with Session(engine) as session:
        stmt = select(CodeValue).where(
                CodeValue.code_set == codeset,
                CodeValue.active_ind == True 
            )
        results = session.execute(stmt).all()

        for row in results:
            row[CodeValue].end_effective_dt_tm = datetime.fromisoformat(END_EFFECTIVE_DATE_ISO)

        session.commit()


def db_delete_CV_rows(codeset):
    """
        Delete certain code_set rows in the code_value table
    """
    with Session(engine) as session:
        kw = {
            'code_set': codeset
        }
        cv_rows = session.query(CodeValue).filter_by(**kw).all()

        for row in cv_rows:
            session.delete(row)

        session.commit()


# Testing stuff
if __name__ == '__main__':
   
    db_update_CV_fields(289)    
    # db_delete_CV_rows(106)
    
    pass

