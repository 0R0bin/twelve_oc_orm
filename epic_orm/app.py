import json
import sqlalchemy as db

from users.models import User, Role
from sqlalchemy.orm import declarative_base, sessionmaker

with open("epic_orm/env.json", "r") as f:
    """
    Get sensible data from JSON so any OS will work 
    """
    data = json.load(f)


engine = db.create_engine(
    f"postgresql:///?user={data["DB_USER"]}&password={data["DB_PASS"]}&database={data["DB_NAME"]}&host={data["DB_HOST"]}&port={data["DB_PORT"]}", 
    echo=True)

# conn = engine.connect()
metadata = db.MetaData() #extracting the metadata
print(metadata)
Base = declarative_base()
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
print(Base.metadata)
session.commit()

# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()

# Base.metadata.create_all(engine)