#!/usr/bin/env python2

import time
from datetime import date

from pimento import menu

from config import get_config
from db import DB
from db.orders import Order

CONFIG_FNAME = 'config.dev.json'


def welcome_msg():
    print '##############################################'
    print '\tWELCOME TO GROCERY MASTER 3000'
    print '##############################################'
    print '\nLoading ...\n'
    time.sleep(1)


def main_action():
    result = menu(
        ['add customer', 'add item', 'add employee', 'add order', 'quit'],
        pre_prompt='What would you like to do:',
        post_prompt="Action: ",
        indexed=True)
    return result


def add_customer():
    '''
    memberNo int
    firstName text
    lastName text
    address text
    expiry date
    '''
    print 'Adding a new customer'
    f_name = raw_input('First name:')
    l_name = raw_input('Last name:')
    address = raw_input('Address:')
    expiry_y = input('Membership expiry year:')
    expiry_m = menu(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
                     'sep', 'oct', 'nov', 'dec'], post_prompt="Membership expiry month: ")
    expiry_d = input('Membership expiry day:')

    d = date(int(expiry_y), int(expiry_m), int(expiry_d))
    print d
    # print f_name, l_name, address, expiry
    pass


def add_item():
    pass


def add_employee():
    pass


def add_order():
    pass


def add_to_db(db, data):
    pass


def main():
    c = get_config(CONFIG_FNAME)
    db = DB(c['database'])

    try:
        db.connect()
        order = Order(db)
        print(order.get())
    except Exception as e:
        raise e
    finally:
        db.close()

    welcome_msg()

    while 1:
        action = main_action()
        if action == 'quit':
            break
        elif action == 'add customer':
            add_customer()
        elif action == 'add item':
            add_item()
        elif action == 'add employee':
            add_employee()
        elif action == 'add order':
            add_order()
        else:
            # should never happen
            break


if __name__ == '__main__':
    main()
