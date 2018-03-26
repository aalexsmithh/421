from pimento import menu
from config import get_config
from db import DB
import numpy as np

CONFIG_FNAME = 'config.prod.json'

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

    # get latest order no from db
    orders = np.asarray(db.orders())
    order_num = max(orders[:,0]) + 1

    # get and check member number
    correct_member_no = False
    members = np.asarray(db.members())
    while not correct_member_no:
        member_no = input("Member number for this order: ")
        if member_no not in members[:,0]:
            print "Sorry that is an invalid member number"
        else:
            i, _ = np.where(members == member_no)
            name = members[i,1] + ' ' + members[i,2]
            address = members[i,3]
            print "Found member: %s, living at %s" % (name[0], address[0])
            correct_member_no = True

    # get order total
    valid_total = False
    while not valid_total:
        try:
            total = float(raw_input("Order total ($): "))
            valid_total = True
        except ValueError:
            print "Please only use numbers in the total"

    # is this a delivery?
    delivery = menu(['yes', 'no'], pre_prompt='Is this a delivery?', insensitive=True)
    if delivery == 'yes':
        delivery = True
    else:
        delivery = False

    # if delivery, get driver id
    if delivery:
        drivers = np.asarray(db.deliverydrivers())
        driver = menu(
            drivers[:,0].tolist(),
            pre_prompt='Please assign a delivery driver:',
            post_prompt="Driver: ",
            indexed=True)
        driver = int(driver)


def main():
    c = get_config(CONFIG_FNAME)

    db = DB(c['database'])

    try:
        db.connect()
        add_order(db)
    except Exception as e:
        raise e
    finally:
        db.close()

if __name__ == '__main__':
    main()