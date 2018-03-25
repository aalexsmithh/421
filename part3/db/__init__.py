import psycopg2


class DB:
    def __init__(self, dbconfig=None):
        self.conf = dbconfig

    def connect(self):
        dsn = DB._build_dsn(self.conf)
        self._conn = psycopg2.connect(dsn)

    def close(self):
        self._conn.close()

    def item(self):
        with self._conn.cursor() as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchone()

    @staticmethod
    def _build_dsn(dbconfig):
        return "host={} dbname={} user={} password={}".format(
            dbconfig['hostname'],
            dbconfig['database'],
            dbconfig['username'],
            dbconfig['password']
        )
