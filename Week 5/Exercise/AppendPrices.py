# Written by: Hu Bowen
# Date: 12 May 2023
# Class: CSF02

# Libraries
import os

# Get folder where this script is stored
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "prices.txt")

# Prices
prices = [ ["teh peng", 1.2],
           ["milo peng", 1.4] ] 

# Append prices to file
with open(data_file, "a") as f:
    for item, price in prices:
        f.write("{}: ${:.2f}\n".format(item, price))