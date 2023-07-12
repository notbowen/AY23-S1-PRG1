# Hu Bowen (S15255800) - CSF02

# Libraries
import os

# Part (a) - Read data from file into list and print it out
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "sales.txt")

with open(data_file) as f:
    data = f.read().splitlines()
    data = [x.split(',') for x in data]

print("========== Part A ==========")
print(data)
print()

# Part (b) - Compute total sales
print("========== Part B ==========")
product_list = ["MacBook Air", "MacBook Pro", "iMac"]
Total_units_list = [0, 0, 0]

print("{:15} {:15} {:<15}".format(*data[0]))
for branch, product, units_sold in data[1:]:
    print("{:15} {:15} {:<15}".format(branch, product, units_sold))
    Total_units_list[product_list.index(product)] += int(units_sold)
print()

print("{:15} {:15}".format("Product", "Total Units Sold"))
for product, units_sold in zip(product_list, Total_units_list):
    print("{:15} {:<15}".format(product, units_sold))
