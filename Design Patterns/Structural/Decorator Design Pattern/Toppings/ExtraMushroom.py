from .ToppingDecorator import ToppingDecorator


class ExtraMushroom(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def cost(self):
        return self._pizza.cost() + 15