# Import the menu function from another module
from interactive_menu import menu

# Create an empty list to store all products
inventory = []

# Check if this file is running in this file (not imported)
if __name__ == "__main__":

    # Print a welcome message with a simple visual format
    print()
    print("=" * 35)
    print(" WELCOME TO J-PRODUCT SUPERMARKET")
    print("=" * 35)

    # Call the menu function and pass the inventory list
    # The function will handle all user interactions
    end_message = menu(inventory)

    # Print the message returned when the user exits the menu
    print(end_message)

# This project demonstrates basic inventory management using Python,
# including input validation, functions, and modular programming.