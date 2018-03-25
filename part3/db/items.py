class Item:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchone()

    def add(self, name, price):
        with self._db.cursor() as cur:
            cur.execute("INSERT INTO items (%s, %s)",
                        (name, price))
