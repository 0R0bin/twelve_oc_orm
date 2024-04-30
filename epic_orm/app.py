import json
import sqlalchemy as db

from clients.models import ClientModels
from contracts.models import ContractModels
from events.models import EventModels
from users.models import UserModels
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
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
# User Models
UserModels.init_db(engine=engine)
ClientModels.init_db(engine=engine)
ContractModels.init_db(engine=engine)
EventModels.init_db(engine=engine)
session.commit()