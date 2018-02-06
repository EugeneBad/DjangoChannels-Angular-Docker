from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from Messenger.consumers import \
    RegisterUser, \
    LoginUser, \
    FetchUser, \
    FetchMsg, \
    ListenMsg

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("register", RegisterUser),
            url("login", LoginUser),
            url("^fetch/users/(?P<token>[\w\.\-]+)$", FetchUser),
            url("^online/(?P<token>[\w\.\-]+)$", ListenMsg),
            url("^fetch/msgs/(?P<text_with>[\w]+)/(?P<token>[\w\.\-]+)$", FetchMsg),

        ])
    ),
})
