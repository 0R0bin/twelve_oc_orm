import datetime

from clients.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship

class ContractModels():
    class Contract(Base):
        __tablename__ = "contract"

        id = Column(Integer, primary_key=True)
        unique_id = Column(String(255), unique=True, nullable=False)
        total_amount = Column(Float, nullable=False)
        total_amount_left = Column(Float, nullable=False)
        created_at = Column(DateTime, default=datetime.datetime.now())
        statut_signed = Column(Boolean, default=False)

        client_id = Column(Integer, ForeignKey("client.id"))
        client = relationship("Client", foreign_keys=[client_id])

    def init_db(engine):
        Base.metadata.create_all(engine)