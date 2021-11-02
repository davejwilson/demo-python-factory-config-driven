from abc import ABC, abstractmethod


class LogSender(ABC):

    @abstractmethod
    def send(self, log_sender):
        pass