from pimento import menu
from datetime import date

def boolean_menu(prompt):
    post_prompt = prompt + " [{}] "

    result = menu(
        ["yes", "no"],
        pre_prompt="Options:",
        post_prompt=post_prompt,
        default_index=1,
        insensitive=True,
        fuzzy=True)

    if result == "yes":
        return True
    elif result == "no":
        return False
    else:
        raise Exception("This should not happen!")

def date_menu(prompt, in_the_future=False):
    '''
    returns a date object
    '''
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug','sep', 'oct', 'nov', 'dec']

    good_date = False
    while not good_date:
        try:
            print prompt
            y = input('Year: ')
            m = menu(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug','sep', 'oct', 'nov', 'dec'],
                post_prompt="Month: ")
            d = input('Day: ')

            date_obj = date(int(y), int(months.index(m) + 1), int(d))

            date_check = date_obj - date.today()
            if in_the_future:
                if date_check.days > 0:
                    good_date = True
                else:
                    good_date = False
                    print 'Date is in the past, try again.'

        except ValueError as e:
            print 'Error: Something is wrong with your date, try again..'
        except NameError as e:
            print 'Error: Please enter a numeric value.'
        
    return date_obj
