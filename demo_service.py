import os

from log_sender_factory import LogSenderFactory

client_type = os.environ['CLIENT_TYPE']
log_sender = LogSenderFactory.get_sender(client_type)
log_info = "demo log info"
log_sender.send(log_info)
