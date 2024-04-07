from .Ticket import Ticket


class IncidentTicket(Ticket):

    def info(self):
        return self.__class__.__name__