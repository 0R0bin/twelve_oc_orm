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


def get_user_from_mail_pass(email, password):
    """
    Return user if found, 404 if not, 401 if password False
    """
    hashed_password = PasswordHasher().hash(password)
    result = p.session.query(uModels.User).filter(uModels.User.email == email).first()

    if result is None:
        return 404

    try:
        PasswordHasher().verify(result.password, password)
    except VerifyMismatchError:
        return 401

    return result
