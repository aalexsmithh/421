from db import Item


def add_item(db):
    print("Adding a new item")
    name = raw_input("Name:")
    price = raw_input("Price:")

    try:
        price = float(price)
    except ValueError:
        print("Price must be a real number")

    item = Item(db)
    item.add(name, price)

    print("Added item (%s, %.2f)" % (name, price))
