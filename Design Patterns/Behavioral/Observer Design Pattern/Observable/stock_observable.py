from abc import ABC, abstractmethod


class StockObservable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def set_stock_count(self, stock_count):
        pass
