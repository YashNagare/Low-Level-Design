from .PaymentStrategyInterface import PaymentStrategy


# Concrete Strategy Class
class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print('Paying', amount, 'Using PayPal')
