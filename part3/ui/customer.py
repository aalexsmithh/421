from datetime import date

from pimento import menu


def add_customer(db):
    '''
    memberNo int
    firstName text
    lastName text
    address text
    expiry date
    '''
    print 'Adding a new customer'
    '''
    f_name = raw_input('First name:')
    l_name = raw_input('Last name:')
    address = raw_input('Address:')
    '''
    expiry_y = input('Membership expiry year:')
    expiry_m = menu(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
                     'sep', 'oct', 'nov', 'dec'],
                    post_prompt="Membership expiry month: ")
    expiry_d = input('Membership expiry day:')

    d = date(int(expiry_y), int(expiry_m), int(expiry_d))
    print d
    # print f_name, l_name, address, expiry
