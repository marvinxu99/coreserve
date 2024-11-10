from sqlalchemy import Column, BigInteger,Integer, String, DateTime, Boolean
from datetime import datetime
import bcrypt

from app import db
from app.core.constants import END_EFFECTIVE_DATE_ISO


class User(db.Model):
    __tablename__ = 'user'

    user_id                 = Column(BigInteger, primary_key=True, autoincrement=True)
    username                = Column(String(50), index=True, unique=True, nullable=True)
    email                   = Column(String(255), index=True, nullable=False)
    password                = Column(String(128), index=True, nullable=False)
    password_expiry_dt_tm   = Column(DateTime, default=datetime.fromisoformat(END_EFFECTIVE_DATE_ISO) )
    
    is_confirmed            = Column(Boolean, default=False)
    is_authenticated        = Column(Boolean, default=False)
    is_active               = Column(Boolean, default=True)
    is_anonymous            = Column(Boolean, default=False)

    name_first              = Column(String(200), nullable=True)
    name_first_key          = Column(String(100), index=True, nullable=True)
    name_full_formatted     = Column(String(100), nullable=True)
    name_last               = Column(String(200), nullable=True)
    name_last_key           = Column(String(100), index=True, nullable=True)
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

    def get_id(self):
        return self.user_id

    def get(self, id):
        try:
            return User.query.get(id)
        except Exception as e:
            return None
    
    @classmethod
    def get(cls, user_id):
        user_data = cls.users.get(user_id)
        if user_data:
            user = User(id=user_data["id"])
            return user
        return None
    
    # def __init__(self, id, password=None):
    #     self.id = id
    #     self.password = password
    #     self.is_confirmed = False  # Track if the user has confirmed their email

    # def verify_password(self, password):
    #     return self.password == password
