from psycopg2 import IntegrityError


class Employee:
    def __init__(self, db):
        self._db = db

    def get(self):
        with self._db.cursor() as cur:
            cur.execute("SELECT * FROM employees;")
            return cur.fetchone()

    def add(self, eid, firstname, lastname, manager, cashier, driver):
        INSERT_EMPLOYEE = """
            INSERT INTO employees(employeeID, firstName, lastName)
            VALUES (%s, %s, %s)
        """

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

            if manager:
                self._add_manager(eid, cur)
            if cashier:
                self._add_cashier(eid, cur)
            if driver:
                self._add_driver(eid, cur)

            self._db.commit()

    def _add_manager(self, eid, cursor):
        INSERT_MANAGER = """
            INSERT INTO managers (employeeID)
            VALUES (%s)
        """

        try:
            cursor.execute(INSERT_MANAGER, [eid])
        except IntegrityError:
            return 'WARN: {} is already a manager'.format(eid)

    def _add_cashier(self, eid, cursor):
        INSERT_CASHIER = """
            INSERT INTO cashiers (employeeID)
            VALUES (%s)
        """

        try:
            cursor.execute(INSERT_CASHIER, [eid])
        except IntegrityError:
            return 'WARN: {} is already a cashier'.format(eid)

    def _add_driver(self, eid, cursor):
        INSERT_DRIVER = """
            INSERT INTO deliverydrivers (employeeID)
            VALUES (%s)
        """

        try:
            cursor.execute(INSERT_DRIVER, [eid])
        except IntegrityError:
            return 'WARN: {} is already a driver'.format(eid)
