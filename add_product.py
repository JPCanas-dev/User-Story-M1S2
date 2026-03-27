
def new_product (inventory):

    correct_name = 0

    while correct_name == 0:

        name = input("Enter product name: ").strip()

        if not name:
            print("\nEmpty name! Please enter a string")
        elif name.replace(" ", "").isalpha():
            correct_name = 1
        else:
            print("\nPlease enter only letters!")

    correct_price = 0

    while correct_price == 0:

        price = input("Enter price: ").strip()

        if not price:
            print("\nEmpty price! Please enter a number")
        else:
            try:
                price = float(price)
                if price <= 0:
                    print("\nPlease enter a positive number!")
                else:
                    correct_price = 1
            except ValueError:
                print("\nPlease enter only numbers!")

    correct_quantity = 0

    while correct_quantity == 0:
            
        quantity = input("Enter quantity: ").strip()

        if not quantity:
            print("\nEmpty quantity! Please enter a number")
        else:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print("Quantity must be greater than 0!")
                else:
                    correct_quantity = 1
            except:
                print("\nPlease enter only integers!")

    product_added = {
        "name" : name,
        "price" : price,
        "quantity" : quantity
    }

    inventory.append(product_added)

    return"\nPRODUCT ADDED!"