
def show_inventory(inventory):

    # Loop through each product in the inventory list
    for product in inventory:

        # Print product information in a formatted way
        print(f"Product: {product['name']} | Price: $ {product['price']:,} | Quantity: {product['quantity']}")

