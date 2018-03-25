from db import Employee
from utils import boolean_menu


def add_employee(db):
    print("Adding a new employee")
    eid = raw_input("Employee ID: ")
    try:
        eid = int(eid)
    except ValueError:
        print("EmployeeId must be an integer")
        return

    firstname = raw_input("First Name: ")
    lastname = raw_input("Last Name: ")

    manager = boolean_menu("Manager?")
    cashier = boolean_menu("Cashier?")
    driver = boolean_menu("Delivery Driver?")

    employee = Employee(db)
    err = employee.add(eid, firstname, lastname, manager, cashier, driver)
    if err is not None:
        print(err)
        return

    print("Added Employee (%d, %s, %s)" % (eid, firstname, lastname))
