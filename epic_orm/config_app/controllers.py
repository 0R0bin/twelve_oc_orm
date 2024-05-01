import json
import provider as p
import sentry_sdk as sLog
import users.controllers as caCtrl

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
    except FileNotFoundError as e:
        sLog.capture_exception(e)
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


def add_first_user():
    """ Add User to DB """
    h_pass = caCtrl.hash_password('123test456')
    user = UserModels.User(employe_number='123456789', nom='Admin', email='admin@admin.fr', password=h_pass, role_id=1)
    p.session.add(user)
    p.session.commit()
