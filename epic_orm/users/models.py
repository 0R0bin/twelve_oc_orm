import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class UserModels():
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

        def __repr__(self):
            return f'User {self.nom}'

    class Role(Base):
        __tablename__ = "role"

        id = Column(Integer, primary_key=True)
        nom = Column(String(255), unique=True, nullable=False)

        def __repr__(self):
            return f'User {self.nom}'
    
    def init_db(engine):
        Base.metadata.create_all(engine)
        return Base