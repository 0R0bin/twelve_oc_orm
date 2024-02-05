import datetime

from app import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    complete_name = Column(String(255), unique=False, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    enterprise_name = Column(String(255), unique=False, nullable=False)
    last_update_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    contact_commercial_id = Column(Integer, ForeignKey("user.id"))

    contact_commercial = relationship("User", foreign_keys=[contact_commercial_id])