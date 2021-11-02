from log_sender import LogSender

class FileLogSender(LogSender):
    path = "~"
    filename = "log-info.txt"

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def send(self, log_info):
        print("writing log info to folder ", self.path, ", filename ", self.filename) 