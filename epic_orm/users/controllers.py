import provider as p

from argon2 import PasswordHasher
from users.models import UserModels as uModels


def hash_password(password):
    """ Simply hash_password with argon2"""
    return PasswordHasher().hash(password)


def save_user_to_db(info_user):
    """ With information provided, save user in database """
    h_pass = hash_password(info_user['password'])
    user_to_add = uModels.User(
        employe_number=info_user['en'],
        nom=info_user['name'],
        email=info_user['email'],
        password=h_pass,
        role_id=int(info_user['role']))
    p.session.add(user_to_add)
    p.session.commit()


def get_user_from_mail_pass(email, password):
    hashed_password = PasswordHasher().hash(password)
    pass