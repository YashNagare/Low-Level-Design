
from DatabaseQuery import DatabaseQuery
import time

class CacheProxy(DatabaseQuery):
    def __init__(self, real_database_query, cache_duration_seconds) -> None:
        self._real_database_query = real_database_query
        self._cache = {}
        self._cache_duration = cache_duration_seconds

    def execute_query(self, query):
        
        if query in self._cache and time.time() - self._cache[query]["timestamp"] <= self._cache_duration:
            print(f"CacheProxy: Returning cached result for query: {query}")
            return self._cache[query]["result"]
        else:
            result = self._real_database_query.execute_query(query)
            self._cache[query] = {"result" : result, "timestamp": time.time()}
            return result