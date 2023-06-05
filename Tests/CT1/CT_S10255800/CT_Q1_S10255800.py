# Hu Bowen (S10255800) - CSF02

require_var = input('Do you require toppings? [Yes / No]: ')  # Removed int()
toppings_set_var = int(input('Portions of toppings required: '))  # Added int()
loyalty_var = input('Do you have the \'loyalty\' card? [Yes / No]: ')  # Added quote escape and closing quote

total_cost = 2.5  # Changed , to .

if require_var.lower() == "yes":  # Changed "Yes" to "yes" to match .lower()
    total_cost = (toppings_set_var * 1.2) + total_cost  # Changed brackets to correct order

if loyalty_var.capitalize() == "Yes":
    total_cost *= 0.9  # Changed x to * for multiplication

print("Total cost: ${:.2f}".format(total_cost))  # Changed [] to {} for .format()
