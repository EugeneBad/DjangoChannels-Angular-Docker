from django.core.serializers import serialize
from django.contrib.auth.models import User
from . models import UserProfile, TextMessage
import json
from . utils import generate_token, is_authenticated


def register_conn(message):
    message.reply_channel.send({"accept": True})


def register_rcv(message):
    credentials = json.loads(message.content["text"])
    if "username" in credentials and "password" in credentials:
        if User.objects.filter(username=credentials["username"]).exists():
            message.reply_channel.send({"text": json.dumps({"status": "409"})})

        else:
            UserProfile.objects.create(user=User.objects.create_user(credentials["username"],
                                       password=credentials["password"]))

            token = generate_token(credentials["username"])

            message.reply_channel.send({"text": json.dumps({"status": 200,
                                                            "token": token})
                                        })

    else:
        message.reply_channel.send({"close": True})


def login_conn(message):
    message.reply_channel.send({"accept": True})


def login_rcv(message):
    credentials = json.loads(message.content["text"])
    if "username" in credentials and "password" in credentials:
        user = User.objects.filter(username=credentials["username"]).first()

        if user and user.check_password(credentials["password"]):
            token = generate_token(credentials["username"])

            message.reply_channel.send({"text": json.dumps({"status": 200,
                                                            "token": token})
                                        })

        else:
            message.reply_channel.send({"text": json.dumps({"status": "401"})})

    else:
        message.reply_channel.send({"close": True})


def fetch_users_conn(message, token):
    username = is_authenticated(token)

    if username:
        other_users = serialize('json', UserProfile.user.objects.exclude(username=username))
        message.reply_channel.send({"text": other_users})


def reject_conn(message):
    message.reply_channel.send({"accept": False})
