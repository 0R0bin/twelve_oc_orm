from argon2 import PasswordHasher


def save_user_to_db(**kwargs):
    pass

def get_user_from_mail_pass(email, password):
    hashed_password = PasswordHasher().hash(password)
    pass