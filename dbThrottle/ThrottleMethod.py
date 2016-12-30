import sqlalchemy

"""
ThrottleMethod: Default methods for throttling metrics.
"""

class ThrottleMethod(Object):
    """
    ThrottleMethod: Default methods for throttling metrics.
    """

    @classmethod
    def mysql_replica_lag(host, *args):
        """Check the mysql replica lag."""
        pass

    @classmethod
    def mysql_threads(host, *args):
        """Check the number of mysql threads."""
        pass

    @classmethod
    def postgresql_replica_lag(host, *args):
        """Check the postgresql replica lag."""
        pass

    @classmethod
    def postgresql_threads(host, *args):
        """Check the number of postgresql threads."""
        pass
    
    @classmethod
    def mssql_replica_lag(host, *args):
        """Check the mssql replica lag."""
        pass

    @classmethod
    def mssql_threads(host, *args):
        """Check the number of mssql threads."""
        pass
    
    @classmethod
    def oracle_replica_lag(host, *args):
        """Check the oracle replica lag."""
        pass

    @classmethod
    def oracle_threads(host, *args):
        """Check the number of mssql threads."""
        pass
