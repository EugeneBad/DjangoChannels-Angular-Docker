

def register_conn(message):
    message.reply_channel.send({"accept": True})


def register_rcv(message):
    pass


def login_conn(message):
    message.reply_channel.send({"accept": True})


def login_rcv(message):
    pass


def reject_conn(message):
    message.reply_channel.send({"accept": False})
