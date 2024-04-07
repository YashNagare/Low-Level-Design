from .AbstractFactory import AbstractFactory
from Ticket.IncidentTicket import IncidentTicket
from Ticket.ProblemTicket import ProblemTicket


class JiraFactory(AbstractFactory):
    def create_ticket(self, type):
        if type == 'incident':
            return IncidentTicket()
        if type == 'problem':
            return ProblemTicket()