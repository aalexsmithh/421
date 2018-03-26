from utils import boolean_menu
from db import Orders, Customers, DeliveryDrivers
import numpy as np
from pimento import menu

def add_order(db):
    '''
    orderNo int
    memberNo int
    total real
    toBeDelivered boolean,
    driverID int,
    FOREIGN KEY(memberNo) REFERENCES customers(memberNo),
    FOREIGN KEY(driverID) REFERENCES deliverydrivers(employeeID)
    );
    '''
    # db queries
    orders = Orders(db).get_all()
    customers = Customers(db).get_all()
    deliverydrivers = DeliveryDrivers(db).get_all()

    # get latest order no from db
    orders = np.asarray(orders)
    order_num = max(orders[:,0]) + 1

    # get and check customer number
    correct_customer_no = False
    customers = np.asarray(customers)
    while not correct_customer_no:
        customer_no = input("customer number for this order: ")
        if customer_no not in customers[:,0]:
            print "Sorry that is an invalid customer number"
        else:
            i, _ = np.where(customers == customer_no)
            name = customers[i,1] + ' ' + customers[i,2]
            address = customers[i,3]
            print "Found customer: %s, living at %s" % (name[0], address[0])
            correct_customer_no = True

    # get order total
    valid_total = False
    while not valid_total:
        try:
            total = float(raw_input("Order total ($): "))
            valid_total = True
        except ValueError:
            print "Please only use numbers in the total"

    # is this a delivery?
    delivery = boolean_menu('Is this a delivery?')

    # if delivery, get driver id
    if delivery:
        drivers = np.asarray(deliverydrivers)
        driver = menu(
            drivers[:,0].tolist(),
            pre_prompt='Please assign a delivery driver:',
            post_prompt="Driver: ",
            indexed=True)
        driver = int(driver)

    order_db = Orders(db)
    if delivery:
        err = order_db.add(order_num, customer_no, total, delivery, driver)
    else:
        err = order_db.add(order_num, customer_no, total, delivery)

    if err is not None:
        print(err)
        return

    if delivery:
        print("Added order (%i, %i, %s, %s, %i)\n" % (order_num, customer_no, total, delivery, driver))
    else:
        print("Added order (%i, %i, %s)\n" % (order_num, customer_no, total))
