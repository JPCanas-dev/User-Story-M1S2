
def show_inventory(inventory):

    for product in inventory:
        print(f"Product: {product['name']} | Price: $ {product['price']:,} | Quantity: {product['quantity']}")

