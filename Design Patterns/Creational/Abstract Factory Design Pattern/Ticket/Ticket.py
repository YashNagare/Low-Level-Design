from abc import ABC, abstractmethod

class Ticket(ABC):

    @abstractmethod
    def info(self):
        pass

