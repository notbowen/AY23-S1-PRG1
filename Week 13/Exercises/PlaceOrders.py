# Written by: Hu Bowen (S10255800)
# Date: 8 July 2023
# Class: CSF02

# Simple order program

# Price list
prices = {
    "chicken": 8.50,
    "steak": 13.80,
    "fish": 9.80,
    "pasta": 9.50,
    "coffee": 2.50,
    "tea": 1.80,
    "water": 0.50
}

# List to store orders
orders = {}

# Function to add order


def add_order():
    global orders  # To apply changes to the order variable in global scope

    print("{:10} {:10}".format("Item", "Price"))
    print("{:10} {:10}".format("----", "-----"))
    for item, price in prices.items():
        print("{:10} {:<10}".format(item, price))

    # Get order from user
    order = input("Your order? ").lower()

    # Print error and return if the order is invalid
    if order not in prices.keys():
        print("{} is not available".format(order))
        return

    # Get quantity and add to dict of orders
    quantity = int(input("How many sets? "))
    try:
        orders[order] += quantity
    except KeyError:
        orders[order] = quantity
    print("{} sets of {} ordered.".format(quantity, order))

# Function to summarise order
def summarise_order():
    # Init total cost
    total_cost = 0.0

    # Print headers
    print("{:10} {:10}".format("Item", "Price"))
    print("{:10} {:10}".format("----", "-----"))

    # Loop thru orders and add price to total cost
    for order, quantity in orders.items():
        print("{:10} {:<10}".format(order, quantity))
        total_cost += prices[order] * quantity

    print("Total cost = ${:.2f}".format(total_cost))

# Main loop
while True:
    print("-------------------")
    print("1. Add order")
    print("2. Summarize orders")
    print("3. Quit")
    print("-------------------")

    choice = int(input("Your choice? "))

    if choice == 1:
        add_order()
    elif choice == 2:
        summarise_order()
    else:  # Assume choice is 3
        quit()
