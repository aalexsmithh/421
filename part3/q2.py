#!/usr/bin/env python2

from config import get_config
from db import DB
from ui import welcome_msg, main_action, add_customer, add_item, \
               add_employee, add_order

CONFIG_FNAME = 'config.dev.json'


def main():
    c = get_config(CONFIG_FNAME)
    db = DB(c['database'])

    welcome_msg()

    try:
        db.connect()
        while 1:
            action = main_action()
            if action == 'quit':
                break
            elif action == 'add customer':
                add_customer()
            elif action == 'add item':
                add_item(db)
            elif action == 'add employee':
                add_employee(db)
            elif action == 'add order':
                add_order()
            else:
                # should never happen
                break
    except Exception as e:
        raise e
    finally:
        db.close()


if __name__ == '__main__':
    main()
