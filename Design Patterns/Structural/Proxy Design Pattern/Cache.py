
from RealDatabaseQuery import RealDatabaseQuery
from CacheProxy import CacheProxy
import time

def main():
    real_database_query = RealDatabaseQuery()
    cache_proxy = CacheProxy(real_database_query, cache_duration_seconds=5)

    print(cache_proxy.execute_query("SELECT * FROM table1"))
    print(cache_proxy.execute_query("SELECT * FROM table2"))
    time.sleep(3)

    print(cache_proxy.execute_query("SELECT * FROM table1"))
    print(cache_proxy.execute_query("SELECT * FROM table3"))

if __name__ == "__main__":
    main()