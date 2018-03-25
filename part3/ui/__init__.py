import time

from pimento import menu

from item import add_item
from order import add_order
from employee import add_employee
from customer import add_customer
from transaction import monthly_revenue


def welcome_msg():
    print '##############################################'
    print '\tWELCOME TO GROCERY MASTER 3000'
    print '##############################################'
    print '\nLoading ...\n'
    time.sleep(1)


def main_action():
    result = menu(
        ['add customer', 'add item', 'add employee', 'add order',
         'monthly revenue', 'quit'],
        pre_prompt='What would you like to do:',
        post_prompt="Action: ",
        indexed=True)
    return result
