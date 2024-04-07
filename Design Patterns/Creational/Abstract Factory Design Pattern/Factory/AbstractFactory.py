from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def create_ticket(self, type):
        pass

