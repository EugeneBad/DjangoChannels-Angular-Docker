from . models import UserProfile, TextMessage
import json
from . utils import generate_token, is_authenticated


def register_conn(message):
    message.reply_channel.send({"accept": True})


def register_rcv(message):
    credentials = json.loads(message.content["text"])
    if "username" in credentials and "password" in credentials:
        if UserProfile.user.objects.filter(username=credentials["username"]).exists():
            message.reply_channel.send({"text": json.dumps({"status": "409"})})

        else:
            UserProfile.user.objects.create_user(username=credentials["username"],
                                     password=credentials["password"])

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
        user = UserProfile.user.objects.filter(username=credentials["username"]).first()

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
        current_user = UserProfile.user.objects.get(username=username)
        


def reject_conn(message):
    message.reply_channel.send({"accept": False})
