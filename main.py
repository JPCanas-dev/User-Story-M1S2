from interactive_menu import menu

inventory = []

if __name__ == "__main__":
    print()
    print("=" * 35)
    print(" WELCOME TO J-PRODUCT SUPERMARKET")
    print("=" * 35)
    end_message = menu(inventory)
    print(end_message)
