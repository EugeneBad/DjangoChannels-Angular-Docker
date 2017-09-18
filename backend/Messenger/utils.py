import datetime
import jwt
from django.conf import settings
from django.contrib.auth.models import User


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


def can_fetch(message, text_with):
    token = message.get("query_string").decode()
    if token and is_authenticated(token) and User.objects.filter(username=text_with).exists():

        return User.objects.get(username=is_authenticated(token)),  \
               User.objects.get(username=text_with)

    else:
        return None


def msg_width(msg):
    if len(msg) <= 13:
        return 16

    if 70 >= len(msg) >= 14:
        return len(msg)
