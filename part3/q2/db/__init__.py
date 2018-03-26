from pimento import menu
import psycopg2

from items import Item
from employees import Employee
from transactions import Transaction
from orders import Orders
from customers import Customers
from deliverydrivers import DeliveryDrivers


class DB:
    def __init__(self, dbconfig=None):
        self.conf = dbconfig

    def connect(self):
        dsn = DB._build_dsn(self.conf)
        self._conn = psycopg2.connect(dsn)

    def close(self):
        self._conn.close()

    def commit(self):
        self._conn.commit()

    def cursor(self):
        return self._conn.cursor()

    @staticmethod
    def _build_dsn(dbconfig):
        return "host={} dbname={} user={} password={}".format(
            dbconfig['hostname'],
            dbconfig['database'],
            dbconfig['username'],
            dbconfig['password']
        )
