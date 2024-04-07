from .PaymentStrategyInterface import PaymentStrategy


# Concrete Strategy Class
class EMIStrategy(PaymentStrategy):
    def pay(self, amount):
        print('Paying', amount, 'Using EMI')
