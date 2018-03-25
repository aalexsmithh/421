from db import Transaction


def monthly_revenue(db):
    print("Getting Monthly Revenue")

    year = raw_input("Year: ")
    try:
        year = int(year)
    except ValueError:
        print("Year must be integer")
        return

    month = raw_input("Month: ")
    try:
        month = int(month)
        if month not in range(1, 13):
            raise ValueError
    except ValueError:
        print("Month must be integer between 1 and 12")
        return

    tran = Transaction(db)
    rev = tran.monthly_revenue(year, month)

    print("Revenue for %d-%d is $%.2f" % (year, month, rev))
