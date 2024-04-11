
from abc import ABC, abstractmethod

class DatabaseQuery(ABC):
    @abstractmethod
    def execute_query(self, query):
        pass