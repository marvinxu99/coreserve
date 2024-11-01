from sqlalchemy import Column, select, Index
from sqlalchemy import Integer, BigInteger, Integer, String, DateTime, Sequence
from datetime import datetime

from app import db


class CodeValueMods(db.Model):
    """
    Stores references to codes changed on the code_value table
    """
    __tablename__ = 'code_value_mods'

    logical_cnt             = Column(BigInteger, Sequence('code_value_mods_id_seq'), primary_key=True)

    cki                     = Column(String(255), nullable=True)
    code_set                = Column(BigInteger, nullable=False)
    code_value              = Column(BigInteger, nullable=False)
    concept_cki             = Column(String(255), nullable=True)

    # PRIMARY KEY.  will populate the column manually using a trigger.  We will use this 
    # new column to create a simple window of changes.  The new column will be calculated using 
    # a formula similar to "LOGICAL_CNT MOD x", where x is the size of the window.  As a simple example, 
    # say we declare x to be 10, meaning we will keep at most 10 items on the table.
    # Note: currently, logical_cnt = logical_cnt_index
    logical_cnt_index       = Column(BigInteger, nullable=False, index=True)

    updt_applctx            = Column(BigInteger,default=0)
    updt_cnt                = Column(Integer, default=0)
    updt_dt_tm              = Column(DateTime, default=datetime.now)
    updt_id                 = Column(BigInteger, default=0)
    updt_task               = Column(Integer, default=0) 

    def __repr__(self):
        return f"<CodeValueMods({self.logical_cnt}, {self.code_value}>"
