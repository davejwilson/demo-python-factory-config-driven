from log_sender import LogSender

class MessageLogSender(LogSender):
    host = "localhost"
    port = 7777
    queue_name = "demo"

    def __init__(self, host, port, queue_name):
        self.host = host
        self.port = port
        self.queue_name = queue_name

    def send(self, log_info):
        print("connecting to ", self.host, ":", self.port, " queue manager ...")
        print("sending log info message to queue ", self.queue_name, " ...")