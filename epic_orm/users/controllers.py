import provider as p

from argon2 import PasswordHasher
from users.models import UserModels as uModels


def hash_password(password):
    return PasswordHasher().hash(password)


def save_user_to_db(info_user):
    h_password = hash_password(info_user['password'])
    print('Hiiiii')
    user_to_add = uModels.User(employe_number=info_user['en'], nom=info_user['name'], email=info_user['email'], password=h_password)
    print('Hi')
    print(p.session)
    p.session.add(user_to_add)
    p.session.commit()


def get_user_from_mail_pass(email, password):
    hashed_password = PasswordHasher().hash(password)
    pass