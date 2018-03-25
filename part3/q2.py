#!/usr/bin/env python2

import time

from pimento import menu

from config import get_config
from db import DB

CONFIG_FNAME = 'config.prod.json'


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
    pass


def add_item():
    pass


def add_employee():
    pass


def add_order():
    pass


def main():
    c = get_config(CONFIG_FNAME)
    print(c)

    db = DB(c['database'])

    try:
        db.connect()
        item = db.item()
        print(item)
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
