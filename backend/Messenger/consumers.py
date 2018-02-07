from django.db.models import Q
from django.contrib.auth.models import User
from .models import UserProfile, TextMessage
import json
from .utils import generate_token, is_authenticated, can_fetch, msg_width
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer
from asgiref.sync import AsyncToSync


class RegisterUser(WebsocketConsumer):
    def connect(self):

        self.accept()

    def websocket_receive(self, message):
        credentials = json.loads(message.get("text"))
        if "username" in credentials and "password" in credentials:
            if User.objects.filter(username=credentials["username"].lower()).exists():
                self.send(text_data=json.dumps({"status": "409"}))
            else:
                UserProfile.objects.create(user=User.objects.create_user(credentials["username"].lower(),
                                                                         password=credentials["password"]))

                token = generate_token(credentials["username"])

                self.send(text_data=json.dumps({"status": 200,
                                                "token": token}))
        else:
            self.close()


class LoginUser(WebsocketConsumer):
    def connect(self):
        self.accept()

    def websocket_receive(self, message):
        credentials = json.loads(message.get("text"))
        if "username" in credentials and "password" in credentials:
            user = User.objects.filter(username=credentials["username"]).first()

            if user and user.check_password(credentials["password"]):
                token = generate_token(credentials["username"])

                self.send(text_data=json.dumps({"status": 200, "token": token}))
            else:
                self.send(text_data=json.dumps({"status": "401"}))

        else:
            self.close()


class FetchUser(SyncConsumer):
    def websocket_connect(self, m):
        token = self.scope["url_route"]["kwargs"].get("token")
        if token and is_authenticated(token):
            self.send({"type": "websocket.accept"})

            username = is_authenticated(token)

            other_users = json.dumps([user.username.capitalize() for user in User.objects.exclude(username=username)])
            self.send({"type": "websocket.send",
                       "text": other_users})
        else:
            self.send({"type": "websocket.close"})


class FetchMsg(SyncConsumer):
    def websocket_connect(self, m):
        token = self.scope["url_route"]["kwargs"].get("token")
        if token and is_authenticated(token):
            self.send({"type": "websocket.accept"})

            sndr_n_rcvr = can_fetch(self.scope["url_route"]["kwargs"].get("text_with").lower(), token)

            if sndr_n_rcvr:
                current_user = sndr_n_rcvr[0]
                text_with = sndr_n_rcvr[1]

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
                self.send({"type": "websocket.send", "text": json.dumps(txt_messages)})

        else:
            self.send({"type": "websocket.close"})


class ListenMsg(SyncConsumer):
    def websocket_connect(self, m):
        token = self.scope["url_route"]["kwargs"].get("token")
        current_username = is_authenticated(token)
        if token and current_username:
            current_user = UserProfile.objects.get(user=User.objects.get(username=current_username))
            current_user.online_code = self.channel_name

            current_user.save()
            self.send({"type": "websocket.accept"})
        else:
            self.send({"type": "websocket.close"})

    def websocket_receive(self, message):
        payload = json.loads(message.get("text"))
        sndr_rcvr = can_fetch(token=payload.get('token'), text_with=payload.get('to').lower())

        if sndr_rcvr and payload.get('body'):
            current_user = sndr_rcvr[0]
            user_to = sndr_rcvr[1]

            TextMessage.objects.create(text_content=payload.get('body'), sender=current_user, receiver=user_to)
            user_to_online_code = UserProfile.objects.get(user=user_to).online_code
            print(user_to_online_code)

            if user_to_online_code != "offline":
                real_time_msg = {"from": current_user.username.capitalize(),
                                 "body": payload.get('body'),
                                 "width": msg_width(payload.get('body')),
                                 "status": "received"}
                # This portion of the code is non-operational because the feature has not been fully implemented yet in
                # channels2.0
                ##############################
                self.channel_layer.send(user_to_online_code, {
                    "type": "websocket.send",
                    "text": json.dumps(real_time_msg)})
                ##############################
            self.send({"type": "websocket.send",
                       "text": json.dumps({"status": "sent",
                                           "width": msg_width(payload.get('body')),
                                           "margin": 99 - msg_width(payload.get('body'))})})


def listener_disc(message):
    pass


def reject_conn(message):
    pass
    # message.reply_channel.send({"accept": False})
