import psycopg2


class DB:
    def __init__(self, dbconfig=None):
        self.conf = dbconfig

    def connect(self):
        dsn = DB._build_dsn(self.conf)
        self._conn = psycopg2.connect(dsn)

    def close(self):
        self._conn.close()

    def cursor(self):
        return self._conn.cursor()

    def orders(self):
        with self._conn.cursor() as cur:
            cur.execute("SELECT * from orders;")
            return cur.fetchall()

    def members(self):
        with self._conn.cursor() as cur:
            cur.execute("SELECT * from customers;")
            return cur.fetchall()

    def deliverydrivers(self):
        with self._conn.cursor() as cur:
            cur.execute("SELECT * from deliverydrivers;")
            return cur.fetchall()

    @staticmethod
    def _build_dsn(dbconfig):
        return "host={} dbname={} user={} password={}".format(
            dbconfig['hostname'],
            dbconfig['database'],
            dbconfig['username'],
            dbconfig['password']
        )
