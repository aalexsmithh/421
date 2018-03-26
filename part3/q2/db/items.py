from psycopg2 import IntegrityError

INSERT_ITEM = """
    INSERT INTO items(name, price)
    VALUES (%s, %s)
"""


class Item:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchone()

    def add(self, name, price):
        with self._db.cursor() as cur:
            try:
                cur.execute(INSERT_ITEM, (name, price))
            except IntegrityError:
                return 'Error: {} is a duplicate item'.format(name)

            self._db.commit()
