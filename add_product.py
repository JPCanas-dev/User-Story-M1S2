
def new_product(inventory):

    # Variable to control name validation loop
    correct_name = 0

    # Loop until a valid name is entered
    while correct_name == 0:

        # Ask user for product name and remove spaces
        name = input("Enter product name: ").strip()  

        if not name:
            # If input is empty
            print("\nEmpty name! Please enter a string")
        elif name.replace(" ", "").isalpha():
            # Check if name contains only letters
            correct_name = 1
        else:
            # If name contains invalid characters
            print("\nPlease enter only letters!")

    # Variable to control price validation loop
    correct_price = 0

    # Loop until a valid price is entered
    while correct_price == 0:
        
        # Ask user for price
        price = input("Enter price: ").strip()  

        if not price:
            # If input is empty
            print("\nEmpty price! Please enter a number")
        else:
            try:
                # Try to convert input to float
                price = float(price)  
                if price <= 0:
                    # Price must be greater than 0
                    print("\nPlease enter a positive number!")
                else:
                    correct_price = 1
            except ValueError:
                # If conversion fails (not a number)
                print("\nPlease enter only numbers!")

    # Variable to control quantity validation loop
    correct_quantity = 0

    # Loop until a valid quantity is entered
    while correct_quantity == 0:

        # Ask user for quantity    
        quantity = input("Enter quantity: ").strip() 

        if not quantity:
            # If input is empty
            print("\nEmpty quantity! Please enter a number")
        else:
            try:
                quantity = int(quantity)  # Try to convert input to integer
                if quantity <= 0:
                    # Quantity must be greater than 0
                    print("Quantity must be greater than 0!")
                else:
                    correct_quantity = 1
            except:
                # If conversion fails (not an integer)
                print("\nPlease enter only integers!")

    # Create a dictionary with the new product data
    product_added = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add the new product to the inventory list
    inventory.append(product_added)

    # Return confirmation message
    return "\nPRODUCT ADDED!"