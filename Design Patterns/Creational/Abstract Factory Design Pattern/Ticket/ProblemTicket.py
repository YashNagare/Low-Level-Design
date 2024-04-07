from .Ticket import Ticket


class ProblemTicket(Ticket):
    def info(self):
        return self.__class__.__name__