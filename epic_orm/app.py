import json
import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

with open("epic_orm/env.json", "r") as f:
    """
    Get sensible data from JSON so any OS will work 
    """
    data = json.load(f)


engine = db.create_engine(f"postgresql:///?User={data["DB_USER"]}&Password={data["DB_PASS"]}&Database={data["DB_NAME"]}&Server={data["DB_HOST"]}&Port={data["DB_PORT"]}")

Base = declarative_base()

# AUTH UN USER SEULEMENT