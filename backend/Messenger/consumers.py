from django.db.models import Q
from django.contrib.auth.models import User
from .models import UserProfile, TextMessage
import json
from .utils import generate_token, is_authenticated


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


def fetch_users_conn(message):
    message.reply_channel.send({"accept": True})


def fetch_users_rcv(message):
    token = json.loads(message.content["text"]).get("token")
    if token and is_authenticated(token):
        username = is_authenticated(token)

        other_users = json.dumps([user.username for user in User.objects.exclude(username=username)])
        message.reply_channel.send({"text": other_users})

    else:
        message.reply_channel.send({"close": True})


def fetch_msgs_conn(message):
    message.reply_channel.send({"accept": True})


def fetch_msgs_rcv(message):
    token = json.loads(message.content["text"]).get("token")
    text_with = json.loads(message.content["text"]).get("text_with")

    if token and is_authenticated(token) and User.objects.filter(username=text_with).exists():
        username = is_authenticated(token)
        username_obj = User.objects.get(username=username)
        text_with_obj = User.objects.get(username=text_with)

        sent = Q(sender=username_obj,
                 receiver=text_with_obj)

        received = Q(sender=text_with_obj,
                     receiver=username_obj)

        txt_messages = [
            {"body": txt_msg.text_content,
             "type": "sent" if txt_msg.sender == username_obj else "received"}

            for txt_msg in TextMessage.objects.filter(sent | received)
        ]

        message.reply_channel.send({"text": json.dumps(txt_messages)})

    else:
        message.reply_channel.send({"close": True})


def reject_conn(message):
    message.reply_channel.send({"accept": False})
