""" Database manipulation using SQLAlchemy ORM
"""
from sqlalchemy import Column, select
from sqlalchemy import Integer, BigInteger, String, Sequence, DateTime, Boolean 
from sqlalchemy import ForeignKey
from datetime import datetime

from app import db
from app.core.constants import END_EFFECTIVE_DATE_ISO


class CodeValue(db.Model):
    __tablename__ = 'code_value'

    code_value              = Column(BigInteger, primary_key=True, autoincrement=True)

    active_ind              = Column(Boolean, default=True)
    active_type_cd          = Column(BigInteger, nullable=True)
    active_status_prsnl_id  = Column(BigInteger, nullable=True)
    begin_effective_dt_tm   = Column(DateTime, default=datetime.now)
    meaning                 = Column(String(12), nullable=True)
    cki                     = Column(String(255), nullable=True)
    code_set                = Column(Integer, ForeignKey('code_set.code_set') )
    collation_seq           = Column(Integer, default=0)
    concept_cki             = Column(String(255), nullable=True)
    data_status_cd          = Column(BigInteger, default=0)
    data_status_dt_tm       = Column(DateTime, nullable=True)
    data_status_prsnl_id    = Column(BigInteger, nullable=True)
    definition              = Column(String(100))
    description             = Column(String(60))
    display                 = Column(String(40), index=True)
    display_key             = Column(String(40), index=True)
    end_effective_dt_tm     = Column(DateTime, default=datetime.fromisoformat(END_EFFECTIVE_DATE_ISO))
    inactive_dt_tm          = Column(DateTime, nullable=True)
    inst_id                 = Column(BigInteger, default=0)
    txn_id_text             = Column(String(200), nullable=True)
    updt_applctx            = Column(BigInteger,default=0)
    updt_cnt                = Column(Integer, default=0)
    updt_dt_tm              = Column(DateTime, default=datetime.now)
    updt_id                 = Column(BigInteger, default=0)
    updt_task               = Column(Integer, default=0) 

    # TODO: to be tested yet
    # codeset = relationship("CodeSet", back_populates="codevalues")

    def __repr__(self):
        return f"<CodeValue(code_value={self.code_value}, display={self.display}, description={self.description}>"
