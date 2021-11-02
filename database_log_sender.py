from log_sender import LogSender

class DatabaseLogSender(LogSender):
    host = "localhost"
    port = 3333
    database = "sample"

    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database

    def send(self, log_info):
        print("connecting to ", self.host, ":", self.port, " ...")
        print("inserting log info into ", self.database, " database ...")