from werkzeug.security import safe_str_cmp
from user_auth import User


def authenticate(useremail, clavewp):
    user = User.find_by_email(useremail)
    if user and safe_str_cmp(user.clavewp, clavewp):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_username(user_id)
