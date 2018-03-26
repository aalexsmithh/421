import numpy as np

class Customers:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM customers;")
            return cur.fetchone()

    def get_all(self):
    	with self._db.cursor() as cur:
            cur.execute("SELECT * FROM customers;")
            return cur.fetchall()

    def add(self, memberNo, firstName, lastName, address, expiry):
        INSERT_CUSTOMER = """
            INSERT INTO customers(memberNo, firstName, lastName, address, expiry)
            VALUES (%s, %s, %s, %s, %s)
        """

        with self._db.cursor() as cur:
            try:
                cur.execute(INSERT_CUSTOMER, (
                    memberNo, 
                    firstName, 
                    lastName, 
                    address, 
                    expiry)
                )
            except IntegrityError:
                return 'Error: Something is wrong with the customer details, please try again'

            self._db.commit()