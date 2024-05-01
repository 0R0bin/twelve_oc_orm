import json
import provider as p

from clients.models import ClientModels
from contracts.models import ContractModels
from events.models import EventModels
from users.models import UserModels


def read_env_file():
    """ Read Information from .env File"""
    try:
        with open("../files/env.json", "r") as f:
            """
            Get sensible data from JSON so any OS will work 
            """
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None


def create_tables_db():
    """ Create all tables in DB """
    UserModels.init_db(engine=p.engine)
    ClientModels.init_db(engine=p.engine)
    ContractModels.init_db(engine=p.engine)
    EventModels.init_db(engine=p.engine)


def add_roles():
    """ Add Roles to DB """
    gestion = UserModels.Role(nom='Gestion')
    commercial = UserModels.Role(nom='Commercial')
    support = UserModels.Role(nom='Support')
    p.session.add_all([gestion, commercial, support])
    p.session.commit()