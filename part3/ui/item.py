from db import Item


def add_item(db):
    print("Adding a new item")
    name = raw_input("Name:")
    price = raw_input("Price:")

    try:
        price = float(price)
    except ValueError:
        print("Price must be a real number")
        return

    item = Item(db)
    err = item.add(name, price)
    if err is not None:
        print(err)
        return

    print("Added item (%s, %.2f)" % (name, price))
