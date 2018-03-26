MONTHLY_REVENUE = """
    SELECT SUM(amount) FROM transactions
    WHERE
            date_part('year', transactiondate) = %s
        AND date_part('month', transactiondate) = %s
        AND amount > 0
"""


class Transaction:
    def __init__(self, db):
        self._db = db

    def monthly_revenue(self, year, month):
        with self._db.cursor() as cur:
            cur.execute(MONTHLY_REVENUE, (year, month))
            return cur.fetchone()[0]
