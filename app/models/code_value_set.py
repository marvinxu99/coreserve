""" Code Set
"""
from sqlalchemy import Column
from sqlalchemy import Integer, BigInteger, String, DateTime, Boolean 
from datetime import datetime

from app import db


class CodeSet(db.Model):
    __tablename__ = 'code_set'

    code_set                = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)

    active_ind              = Column(Boolean, default=True, nullable=False)
    add_access_ind          = Column(Boolean, default=True)
    alias_dup_ind           = Column(Boolean, default=False)
    cache_ind               = Column(Boolean, default=False)
    meaning_dup_ind         = Column(Boolean, default=False)
    change_access_ind       = Column(Boolean, default=True)
    code_set_hits           = Column(Integer, nullable=True)
    code_value_cnt          = Column(Integer, default=0)
    contributor             = Column(String(20), nullable=True)
    definition              = Column(String(500), nullable=True)
    definition_dup_ind      = Column(Boolean, default=False)
    del_access_ind          = Column(Boolean, default=False)
    description             = Column(String(60), nullable=True)
    display                 = Column(String(40), nullable=False, index=True)
    display_dup_ind         = Column(Boolean, default=False)
    display_key             = Column(String(40), index=True)
    display_key_dup_ind     = Column(Boolean, default=False)
    domain_code_set         = Column(Integer, default=0)
    domain_qualifier_ind    = Column(Boolean, default=False)
    extension_ind           = Column(Boolean, default=True)
    inq_access_ind          = Column(Boolean, default=True)
    inst_id                 = Column(BigInteger, default=0)
    owner_module            = Column(String(20), nullable=True)
    table_name              = Column(String(32), nullable=True)
    txn_id_text             = Column(String(200), nullable=True)
    updt_applctx            = Column(BigInteger, default=0)
    updt_cnt                = Column(Integer, default=0)
    updt_dt_tm              = Column(DateTime, default=datetime.now)
    updt_id                 = Column(BigInteger, default=0)
    updt_task               = Column(BigInteger, default=0)

    # codevalues = relationship("CodeValue", back_populates='codeset')

    def __repr__(self) -> str:
        return (f"<CodeSet(code_set={self.code_set}, display={self.display})>")
