from channels import route
from Messenger.consumers import \
    register_conn, register_rcv, \
    login_conn, login_rcv, \
    fetch_users, \
    fetch_msgs, \
    reject_conn

channel_routing = [
    route("websocket.connect", register_conn, path="/register"),
    route("websocket.receive", register_rcv, path="/register"),
    route("websocket.connect", login_conn, path="/login"),
    route("websocket.receive", login_rcv, path="/login"),

    route("websocket.connect", fetch_users, path="/fetch/users"),

    route("websocket.connect", fetch_msgs, path="/fetch/msgs/(?P<text_with>[\w]+)"),

    route("websocket.connect", reject_conn, path="/[\w]?")
]
