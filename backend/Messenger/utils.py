import datetime
import jwt
from django.conf import settings


def generate_token(username):
    payload = {'username': username,
               "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=6000)}

    token = jwt.encode(payload, key=settings.SECRET_KEY).decode()

    return token


def is_authenticated(token):
    try:
        current_username = jwt.decode(token, key=settings.SECRET_KEY)["username"]
        return current_username

    except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
        return False
