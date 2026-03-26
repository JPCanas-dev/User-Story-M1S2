
def calculations(inventory):

    total_revenue = 0
    total_products = 0

    total_revenue += sum(product["price"] * product["quantity"] for product in inventory)
    total_products += sum(product["quantity"] for product in inventory)

    return total_revenue, total_products