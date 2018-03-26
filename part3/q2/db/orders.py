from psycopg2 import IntegrityError

class Orders:
    def __init__(self, db):
        self._db = db

    def get_all(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM orders;")
            return cur.fetchall()

    def add(self, orderNo, memberNo, total, toBeDelivered, driverID=None):
        if driverID is None:
            INSERT_ORDER = """
                INSERT INTO orders(orderNo, memberNo, total, toBeDelivered)
                VALUES (%s, %s, %s, %s)
            """
        else:
            INSERT_ORDER = """
                INSERT INTO orders(orderNo, memberNo, total, toBeDelivered, driverID)
                VALUES (%s, %s, %s, %s, %s)
            """

        with self._db.cursor() as cur:
            try:
                if driverID is None:
                    cur.execute(INSERT_ORDER, (
                        orderNo, 
                        memberNo, 
                        total, 
                        toBeDelivered)
                    )
                else:
                    cur.execute(INSERT_ORDER, (
                        orderNo, 
                        memberNo, 
                        total, 
                        toBeDelivered, 
                        driverID)
                    )
            except IntegrityError:
                return 'Error: Check order details and try again'

            self._db.commit()