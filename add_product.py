
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

        elif quantity.isdigit():

            quantity = int(quantity)
            if quantity <= 0:
                print("\nPlease enter a positive number!")
            else:
                correct_quantity = 1

        else:
            print("\nPlease enter only integers!")

    product_added = {
        "name" : name,
        "price" : price,
        "quantity" : quantity
    }

    inventory.append(product_added)

    return"\nPRODUCT ADDED!"

# isdigit() → valida si el string tiene solo números
# Para posteriormente hacer la conversion

# Limitación importante
# isdigit() es bastante estricto:
# Solo acepta dígitos puros (0–9)
# No acepta:
# negativos (-5)
# decimales (3.14)
# espacios

# NO lo uses cuando:
# Hay decimales
# Hay negativos

# Idea mental clave
# isdigit() = filtro simple
# try/except = validación real

# El float de price = float(price) es porque:
# float ("") es ValueError, por eso siempre me mandaba alla,
# por tal razon, tuve que crear el try-except asi por aparte,
# el price = float(input("Enter price: ")) y el
# if not price los tenia dentro del try, los tuve que sacar y
# separar el float con price = float(price)