from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255), nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    attendees = Column(Integer, unique=True, nullable=False)
    notes = Column(String(1000), nullable=True)
    contract_id = Column(Integer, ForeignKey("contract.id"))
    contract = relationship("Contract", foreign_keys=[contract_id])
    client_id = Column(Integer, ForeignKey("client.id"))
    client = relationship("Client", foreign_keys=[client_id])
