class DeliveryDrivers:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM deliverydrivers;")
            return cur.fetchone()

    def get_all(self):
    	with self._db.cursor() as cur:
            cur.execute("SELECT * FROM deliverydrivers;")
            return cur.fetchall()