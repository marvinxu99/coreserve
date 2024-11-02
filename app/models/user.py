from sqlalchemy import Column, BigInteger,Integer, String, DateTime
from datetime import datetime
import bcrypt

from app import db
from app.core.constants import END_EFFECTIVE_DATE_ISO


class Users(db.Model):
    __tablename__ = 'users'

    user_id                 = Column(BigInteger, primary_key=True, autoincrement=True)
    username                = Column(String(50), index=True, unique=True)
    email                   = Column(String(255), index=True, nullable=True, unique=True)
    password                = Column(String(128), index=True, nullable=False)
    password_expiry_dt_tm   = Column(DateTime, default=datetime.fromisoformat(END_EFFECTIVE_DATE_ISO) )   

    name_first              = Column(String(200))
    name_first_key          = Column(String(100), index=True)
    name_full_formatted     = Column(String(100))
    name_last               = Column(String(200))
    name_last_key           = Column(String(100))
    name_middle             = Column(String(200), nullable=True)
    name_middle_key         = Column(String(100), nullable=True, index=True)
    
    active_status_cd        = Column(BigInteger, nullable=True)      # Codeset 48: Active 
    active_status_dt_tm     = Column(DateTime, default=datetime.now)
    active_status_prsnl_id  = Column(BigInteger, default=0)
    beg_effective_dt_tm     = Column(DateTime, default=datetime.now)
    end_effective_dt_tm     = Column(DateTime, default=datetime.fromisoformat(END_EFFECTIVE_DATE_ISO))
    create_dt_tm            = Column(DateTime, default=datetime.now)
    create_prsnl_id         = Column(BigInteger, nullable=True)
    updt_applctx            = Column(BigInteger,default=0)
    updt_cnt                = Column(Integer, default=0)
    updt_dt_tm              = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updt_id                 = Column(BigInteger, default=0)
    updt_task               = Column(Integer, default=0) 
        
    def __repr__(self):
        return f"<Users(user_id={self.user_id}, username={self.username}"


