from django.contrib.auth.models import User
import json
from . utils import generate_token


def register_conn(message):
    message.reply_channel.send({"accept": True})


def register_rcv(message):
    credentials = json.loads(message.content["text"])
    if "username" in credentials and "password" in credentials:
        if User.objects.filter(username=credentials["username"]).exists():
            message.reply_channel.send({"text": json.dumps({"status": "409"})})

        else:
            User.objects.create_user(username=credentials["username"],
                                     password=credentials["password"])

            token = generate_token(credentials["username"])

            message.reply_channel.send({"text": json.dumps({"status": 200, "token": token})})


def login_conn(message):
    message.reply_channel.send({"accept": True})


def login_rcv(message):
    pass


def reject_conn(message):
    message.reply_channel.send({"accept": False})
