from channels import route
from Messenger.consumers import \
    register_conn, register_rcv, \
    login_conn, login_rcv, \
    fetch_users_conn, fetch_users_rcv, \
    fetch_msgs_conn, fetch_msgs_rcv, \
    reject_conn

channel_routing = [
    route("websocket.connect", register_conn, path="/register"),
    route("websocket.receive", register_rcv, path="/register"),
    route("websocket.connect", login_conn, path="/login"),
    route("websocket.receive", login_rcv, path="/login"),

    route("websocket.connect", fetch_users_conn, path="/fetch/users"),
    route("websocket.receive", fetch_users_rcv, path="/fetch/users"),

    route("websocket.connect", fetch_msgs_conn, path="/fetch/messages"),
    route("websocket.receive", fetch_msgs_rcv, path="/fetch/messages"),

    route("websocket.connect", reject_conn, path="/[\w]?")
]
