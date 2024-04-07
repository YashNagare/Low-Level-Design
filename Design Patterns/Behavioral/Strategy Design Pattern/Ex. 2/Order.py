from Strategy.CreditCardStrategyImpl import CreditCardStrategy
from Strategy.PayPalStrategyImpl import PayPalStrategy
from Strategy.EMIStrategyImpl import EMIStrategy


# Context Class
class Order:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    # Don't know why this block of code is written
    # def set_payment(self, payment_strategy):
    #     self._payment_strategy = payment_strategy

    def make_payment(self, amount):
        self._payment_strategy.pay(amount)


# Client Code
if __name__ == '__main__':
    order = Order(CreditCardStrategy())
    order.make_payment(100)

    order = Order(PayPalStrategy())
    order.make_payment(250)

    order = Order(EMIStrategy())
    order.make_payment(500)
