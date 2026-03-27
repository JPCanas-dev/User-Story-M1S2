# Import functions from other modules
from add_product import new_product
from display_inventory import show_inventory
from display_statistics import calculations

def menu(inventory):

    # Variable to control the menu loop
    end_menu = 0

    # Main loop: keeps showing the menu until user chooses to exit
    while end_menu == 0:

        # Display menu options
        print("\n1. Add product")
        print("2. Display inventory")
        print("3. Display statistics")
        print("4. Exit")

        # Ask user to select an option
        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            # Call function to add a new product
            # It returns a success message
            success_add = new_product(inventory)
            print(success_add)

        elif option == "2":
            # Check if inventory is empty before displaying
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                # Call function to show all products
                show_inventory(inventory)

        elif option == "3":
            # Check if inventory is empty before calculating statistics
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                # Call function to calculate totals
                total_revenue, total_product = calculations(inventory)

                # Display formatted results
                print(f"Total revenue: $ {total_revenue:,}")
                print(f"Total registered products: {total_product}")

        elif option == "4":
            # Change control variable to exit the loop
            end_menu = 1

        else:
            # Print invalid input
            print("PLEASE ENTER A VALID VALUE!")

    # Return exit message after leaving the loop
    return "THANKS FOR USING MY SERVICES!\n"






