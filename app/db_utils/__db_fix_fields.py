from sqlalchemy.sql.expression import and_, select, desc, label
from datetime import datetime

from app.models.code_value import CodeValue
from app.core.constants import END_EFFECTIVE_DATE_ISO


def db_update_CV_fields(db, codeset):
    """
        Fix the values of the end_effective_dt_tm column of codeset 106
    """
    with db.session() as session:
        stmt = select(CodeValue).where(
                CodeValue.code_set == codeset,
                CodeValue.active_ind == True 
            )
        results = session.execute(stmt).all()

        for row in results:
            row[CodeValue].end_effective_dt_tm = datetime.fromisoformat(END_EFFECTIVE_DATE_ISO)

        session.commit()


def db_delete_CV_rows(db, codeset):
    """
        Delete certain code_set rows in the code_value table
    """
    with db.session() as session:
        kw = {
            'code_set': codeset
        }
        cv_rows = session.query(CodeValue).filter_by(**kw).all()

        for row in cv_rows:
            session.delete(row)

        session.commit()

def db_fix_(db):
    
    # db_update_CV_fields(db, 54)    
    
    # db_delete_CV_rows(db, 54)    
    
    pass

