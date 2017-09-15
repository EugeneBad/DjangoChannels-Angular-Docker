from django.db.models import Q
from django.contrib.auth.models import User
from .models import UserProfile, TextMessage
import json
from .utils import generate_token, is_authenticated, can_fetch


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

    sndr_rcvr = can_fetch(json.loads(message.content["text"]))

    if sndr_rcvr:
        current_user = sndr_rcvr[0]
        text_with = sndr_rcvr[1]

        sent = Q(sender=current_user,
                 receiver=text_with)

        received = Q(sender=text_with,
                     receiver=current_user)

        txt_messages = [
            {"body": txt_msg.text_content,
             "type": "sent" if txt_msg.sender == current_user else "received"}

            for txt_msg in TextMessage.objects.filter(sent | received)
        ]

        message.reply_channel.send({"text": json.dumps(txt_messages)})

    else:
        message.reply_channel.send({"close": True})


def reject_conn(message):
    message.reply_channel.send({"accept": False})
