import os
from database_log_sender import DatabaseLogSender
from file_log_sender import FileLogSender
from message_log_sender import MessageLogSender

class LogSenderFactory:
    def get_sender(client_type):
        if client_type == 'DATABASE':
            return DatabaseLogSender(os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'], os.environ['DATABASE_NAME'])
        elif client_type == 'FILE':
            return FileLogSender(os.environ['FOLDER_PATH'], os.environ['FILE_NAME'])
        elif client_type == 'MESSAGE':
            return MessageLogSender(os.environ['QUEUE_MANAGER_HOST'], os.environ['QUEUE_MANAGER_PORT'], os.environ['QUEUE_NAME'])
        else:
            raise ValueError(client_type)