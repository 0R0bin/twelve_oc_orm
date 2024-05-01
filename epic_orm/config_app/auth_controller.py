import datetime as dt
import json
import jwt
import os

from config_app.controllers import read_env_file


def gen_jwt_with_user_info(obj_user):
    """
    Generate token with user information
    Save JWT to file
    """
    env = read_env_file()
    data = {
        'id': obj_user.employe_number,
        'username': obj_user.employe_number,
        'exp': dt.datetime.now(tz=dt.timezone.utc) + dt.timedelta(minutes=env['LIFETIME_TOKEN']),
        'role': obj_user.role.id
    }

    token = jwt.encode(data, env['SECRET_KEY'], algorithm='HS256')

    with open('../files/token.json', 'w') as f:
        json.dump(token, f)
    


def check_token():
    """
    Read data from token file
    """
    try:
        with open('../files/token.json', 'r') as f:
            session_data = json.load(f)
            return session_data
    except FileNotFoundError:
        return None


def del_jwt():
    """
    Delete file saving token to logout user
    """
    try:
        os.remove('../files/token.json')
    except Exception:
        pass


def read_jwt_user_info():
    """
    Read User Information
    """
    try:
        token = check_token()
        if token:
            env = read_env_file()
            user_info = jwt.decode(token, env['SECRET_KEY'], algorithms=['HS256'])
            return user_info['role']
        else:
            return None
    except Exception:
        return None