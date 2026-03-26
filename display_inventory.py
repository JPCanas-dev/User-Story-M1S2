
def show_inventory(inventory):

    if not inventory:
        print("INVENTORY IS EMPTY!")

    for product in inventory:
        print(f"Product: {product['name']} | Price: $ {product['price']:,} | Quantity: {product['quantity']}")

