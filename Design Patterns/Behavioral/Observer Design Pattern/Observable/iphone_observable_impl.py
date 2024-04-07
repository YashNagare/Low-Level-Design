from .stock_observable import StockObservable


class IphoneObservableImpl(StockObservable):
    def __init__(self):
        self.observers = []
        self.stock_count = 0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def set_stock_count(self, stock_count):
        if self.stock_count == 0:
            self.notify_observers()
        self.stock_count += stock_count
