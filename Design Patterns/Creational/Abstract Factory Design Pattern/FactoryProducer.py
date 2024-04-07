from Factory.JiraFactory import JiraFactory
from Factory.SnowFactory import SnowFactory


class FactoryProducer:
    
    def get_factory(self, type):
        if type == 'jira':
            return JiraFactory()
        if type == 'snow':
            return SnowFactory()