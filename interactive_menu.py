from add_product import new_product
from display_inventory import show_inventory
from display_statistics import calculations

def menu(inventory):

    end_menu = 0

    while end_menu == 0:

        print("\n1. Add product")
        print("2. Display inventory")
        print("3. Display statistics")
        print("4. Exit")

        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            success_add = new_product(inventory)
            print(success_add)

        elif option == "2":
            show_inventory(inventory)

        elif option == "3":
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                total_revenue, total_product = calculations(inventory)
                print(f"Total revenue: $ {total_revenue:,}")
                print(f"Total registered products: {total_product:,}")

        elif option == "4":
            end_menu = 1

        else:
            print("PLEASE ENTER A VALID VALUE!")

    return"THANKS FOR USING MY SERVICES!\n"






