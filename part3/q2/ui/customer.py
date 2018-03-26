from utils import date_menu
from pimento import menu
from db import Customers
import numpy as np

def add_customer(db):
    '''
    memberNo int
    firstName text
    lastName text
    address text
    expiry date
    '''
    customers = Customers(db).get_all()
    customers = np.asarray(customers)
    customer_num = max(customers[:,0]) + 1
    
    f_name = raw_input('First name: ')
    l_name = raw_input('Last name: ')
    address = raw_input('Address: ')

    d = date_menu("Please enter the membership expiry date:", in_the_future=True)
    
    err = Customers(db).add(customer_num, f_name, l_name, address, d)
    
    if err is not None:
        print(err)
        return

    print("Added customer (%s, %s, %s, %s, %s)\n" % (customer_num, f_name, l_name, address, d))

if __name__ == '__main__':
    add_customer(None)