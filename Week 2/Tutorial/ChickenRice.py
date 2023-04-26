# Written by: Hu Bowen
# Date: 26 April 2023
# Class: CSF02

"""
Question Overview:
- User input chicken rice price
- Each side dish is $1.20
- GST is 8%
- GST applied on total cost, round final to nearest 10 cents
"""

# Constants
SIDES_PRICE = 1.2
GST = 0.08

# Input
rice = float(input("Enter the price of chicken rice: "))
sides = int(input("Enter the number of side-dishes: "))

# Process
total = rice + (sides * SIDES_PRICE)
total = total * (1 + GST)

# Output
print("Total cost of the purchase is ${:.1f}0".format(total))
