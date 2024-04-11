
from DatabaseQuery import DatabaseQuery

class RealDatabaseQuery(DatabaseQuery):
    def execute_query(self, query):
        print(f"Executing query : {query}")
        return f"Results for query : {query}"