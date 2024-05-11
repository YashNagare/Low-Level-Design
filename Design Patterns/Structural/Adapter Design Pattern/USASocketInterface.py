# Target interface
from abc import ABC, abstractmethod

class USASocketInterface(ABC):

    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def neutral(self):
        pass