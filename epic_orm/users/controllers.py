import provider as p

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
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


def put_user(info_user, user):
    """ With information provided, put user in database """
    print(f'Je suis arrivé jusque là ! {user}')
    user.employe_number = info_user['en']
    user.nom = info_user['name']
    user.email = info_user['email']
    print(f'Et là ? {info_user['role']}')
    user.role.id = info_user['role']
    print(f'End : {user}')

    p.session.commit()


def get_user_from_mail_pass(email, password):
    """
    Return user if found, 404 if not, 401 if password False
    """
    result = p.session.query(uModels.User).filter(uModels.User.email == email).first()

    if result is None:
        return 404

    try:
        PasswordHasher().verify(result.password, password)
    except VerifyMismatchError:
        return 401

    return result


def get_user_with_filter(info):
    """
    Return all user if choice == 1 by id, 2 by num, 3 by mail
    """
    choice_filter = int(info['choice'])

    if choice_filter == 1:
        result = p.session.query(uModels.User).filter(uModels.User.id == info['param']).first()
    if choice_filter == 2:
        result = p.session.query(uModels.User).filter(uModels.User.employe_number == info['param']).first()
    if choice_filter == 3:
        result = p.session.query(uModels.User).filter(uModels.User.email == info['param']).first()

    if result is None:
        return 404

    return result

def get_all_users():
    """
    Return all users in DB
    """
    result = p.session.query(uModels.User).all()

    return result


def del_user(user):
    """
    Delete user
    """
    p.session.delete(user)
    p.session.commit()
