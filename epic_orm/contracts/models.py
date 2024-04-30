import datetime

from clients.models import ClientModels, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship

class ContractModels():
    class Contract(Base):
        __tablename__ = "contract"

        id = Column(Integer, primary_key=True)
        unique_id = Column(String(255), unique=True, nullable=False)
        client_id = Column(Integer, ForeignKey("client.id"))
        total_amout = Column(Float, nullable=False)
        total_amout_left = Column(Float, nullable=False)
        created_at = Column(DateTime, default=datetime.datetime.utcnow)
        statut_signed = Column(Boolean, default=False)

        client = relationship("ClientModels.Client", foreign_keys=[client_id])

    def init_db(engine):
        Base.metadata.create_all(engine)