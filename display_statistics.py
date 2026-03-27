
def calculations(inventory):

    # Initialize variables to store totals
    total_revenue = 0
    total_products = 0

    # Calculate total revenue:
    # Multiply price * quantity for each product and sum all values
    total_revenue += sum(product["price"] * product["quantity"] for product in inventory)

    # Calculate total number of products:
    # Sum the quantity of all products in the inventory
    total_products += sum(product["quantity"] for product in inventory)

    # Return both results as a tuple
    return total_revenue, total_products