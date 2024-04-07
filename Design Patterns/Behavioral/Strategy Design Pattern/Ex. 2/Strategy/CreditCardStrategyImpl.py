from .PaymentStrategyInterface import PaymentStrategy


# Concrete Strategy Class
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print('Paying', amount, 'Using Credit Card')
