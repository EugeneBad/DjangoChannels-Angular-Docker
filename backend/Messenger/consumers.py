from django.db.models import Q
from django.contrib.auth.models import User
from channels import Group
from .models import UserProfile, TextMessage
import json
from .utils import generate_token, is_authenticated, can_fetch, msg_width


def register_conn(message):
    message.reply_channel.send({"accept": True})


def register_rcv(message):
    credentials = json.loads(message.content["text"])
    if "username" in credentials and "password" in credentials:
        if User.objects.filter(username=credentials["username"].lower()).exists():
            message.reply_channel.send({"text": json.dumps({"status": "409"})})

        else:
            UserProfile.objects.create(user=User.objects.create_user(credentials["username"].lower(),
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


def fetch_users(message):

    token = message.get("query_string").decode()
    if token and is_authenticated(token):
        username = is_authenticated(token)

        other_users = json.dumps([user.username.capitalize() for user in User.objects.exclude(username=username)])
        message.reply_channel.send({"text": other_users})

    else:
        message.reply_channel.send({"close": True})


def fetch_msgs(message, text_with):
    sndr_rcvr = can_fetch(message, text_with.lower())

    if sndr_rcvr:
        message.reply_channel.send({"accept": True})
        current_user = sndr_rcvr[0]
        text_with = sndr_rcvr[1]

        sent = Q(sender=current_user,
                 receiver=text_with)

        received = Q(sender=text_with,
                     receiver=current_user)

        txt_messages = [
            {"margin": 99 - msg_width(txt_msg.text_content),
             "width": msg_width(txt_msg.text_content),
             "body": txt_msg.text_content,
             "type": "sent" if txt_msg.sender == current_user else "received"}

            for txt_msg in TextMessage.objects.filter(sent | received).order_by('pk')
        ]

        message.reply_channel.send({"text": json.dumps(txt_messages)})

    else:
        message.reply_channel.send({"close": True})


def listener_conn(message):
    token = message.get("query_string").decode()
    if token and is_authenticated(token):
        message.reply_channel.send({"accept": True})

def listener_rcv(message):
    pass


def listener_disc(message):
    pass


def reject_conn(message):
    message.reply_channel.send({"accept": False})
