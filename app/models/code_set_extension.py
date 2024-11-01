from sqlalchemy import Column, Index
from sqlalchemy import Integer, BigInteger, Integer, String, DateTime
from datetime import datetime

from app import db


class CodeSetExtension(db.Model):
    """Code sets can be extended by adding additional parameters to the code set definition.  
        This is done in a name value pair lookup approach.  
        Each additional parameter becomes a row on the code set extension entity.    
    """
    __tablename__ = 'code_set_extension'

    code_set                = Column(BigInteger, primary_key=True, autoincrement=False)

    field_default           = Column(String(50), nullable=True)
    field_help              = Column(String(100), nullable=True)
    
    # The input mask for the code value extension
    field_in_mask           = Column(String(50), nullable=True)
    field_len               = Column(Integer, nullable=True)
    field_name              = Column(String(32), nullable=False)
    field_out_mask          = Column(String(50), nullable=True)
    field_prompt            = Column(String(50), nullable=True)
    field_seq               = Column(Integer, default=0)
    
    # The input mask for the code value extension
    field_type              = Column(Integer, default=0, nullable=True)

    # The code_set that all responses must exist in
    validation_code_set     = Column(BigInteger, nullable=True)
    
    # The check for valid values (ie only allow X and Z)
    validation_condition    = Column(String(100), nullable=True)

    updt_applctx            = Column(BigInteger,default=0)
    updt_cnt                = Column(Integer, default=0)
    updt_dt_tm              = Column(DateTime, default=datetime.now)
    updt_id                 = Column(BigInteger, default=0)
    updt_task               = Column(Integer, default=0) 

    Index('ix_code_set_extension_codeset_fieldname', code_set, field_name)

    def __repr__(self):
        return f"<CodeSetExtension({self.code_set}, {self.field_name}>"
