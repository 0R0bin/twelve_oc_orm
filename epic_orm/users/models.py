import datetime

from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    employe_number = Column(Integer, unique=True, nullable=False)
    nom = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role", foreign_keys=[role_id])

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255), unique=True, nullable=False)