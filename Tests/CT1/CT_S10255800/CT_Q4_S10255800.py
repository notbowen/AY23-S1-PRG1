# Hu Bowen (S10255800) - CSF02

# Create nested list to store data from table
# Structure: [Item name, Unit price, Quantity]
item_data = [
    ["Curry puff", 2.4, 2],
    ["Apple tart", 2.0, 4],
    ["Tuna puff", 2.2, 5],
    ["Egg tart", 1.8, 1],
    ["Custard tart", 1.5, 2],
]

# Variables to calculate the cost of the puffs and tarts
total_tart_price = 0.0
total_puff_price = 0.0

# Calculate and display prices in table,
# And show cost of tarts and puffs
print("{:15} {:>10} {:>10} {:>10}".format("Item Name", "Unit Price", "Quantity", "Amount"))
for item_name, unit_price, quantity in item_data:
    amount = unit_price * quantity

    if item_name.endswith("tart"):
        total_tart_price += amount
    else:
        total_puff_price += amount

    print("{:15} {:10.2f} {:10} {:10.2f}".format(item_name, unit_price, quantity, amount))
    
print("\nTotal cost of tarts: ${:.2f}".format(total_tart_price))
print("Total cost of puffs: ${:.2f}".format(total_puff_price))
