from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255), nullable=False)
    # Contact FK ?
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    # FK User
    location = Column(String(255), nullable=False)
