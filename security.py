from user_manager import find_by_id, find_by_username
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return find_by_id(user_id)
