from abc import ABC, abstractmethod
from Pizzas.BasePizza import BasePizza

class ToppingDecorator(BasePizza):

    def __init__(self, pizza):
        self._pizza = pizza

    @abstractmethod
    def cost(self):
        pass