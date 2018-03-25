from pimento import menu
from config import get_config
from db import DB

CONFIG_FNAME = 'config.prod.json'

def add_order():
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
    # orders = db.orders()
    # order_num = max(orders) + 1

    # get and check member number
    correct_member_no = False
    members = db.members()
    while not correct_member_no:
        member_no = input("Member number for this order:")
        if member_no not in members:
            print "Sorry that is an invalid member number"
        else:
            print "Found member %s" % (members[member_no].name)
            correct_member_no = True

    # get order total
    valid_total = False
    while not valid_total:
        try:
            total = float(raw_input("Order total ($):"))
            valid_total = True
        except ValueError:
            print "Please only use numbers in the total"

    # is this a delivery?
    valid_delivery = False
    while not valid_delivery:
        delivery = raw_input("Is this a delivery (y/n)?:")
        if delivery == 'y' or delivery == 'Y':
            delivery = True
            valid_delivery = True
        elif delivery == 'n' or delivery =='N':
            delivery = False
            valid_delivery = True
        else:
            print 'Only use y or n.'

    # if delivery, get driver id
    if delivery:
        drivers = db.deliverydrivers()
        driver = menu(
            drivers,
            pre_prompt='Please assign a delivery driver:',
            post_prompt="Driver: ",
            indexed=True)
        driver = int(driver)


def main():
    c = get_config(CONFIG_FNAME)

    db = DB(c['database'])

    try:
        db.connect()
        item = db.item()
        print(item)
    except Exception as e:
        raise e
    finally:
        db.close()

if __name__ == '__main__':
    main()