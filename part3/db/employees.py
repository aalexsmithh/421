from psycopg2 import IntegrityError

INSERT_EMPLOYEE = """
    INSERT INTO employees(employeeID, firstName, lastName)
    VALUES (%s, %s, %s)
"""


class Employee:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM employees;")
            return cur.fetchone()

    def add(self, eid, firstname, lastname, manager, cashier, driver):
        with self._db.cursor() as cur:
            try:
                cur.execute(INSERT_EMPLOYEE, (
                    eid,
                    firstname,
                    lastname)
                )
            except IntegrityError:
                return 'Error: Employees cannot have the same IDs. {}' \
                    .format(eid)

            self._db.commit()
