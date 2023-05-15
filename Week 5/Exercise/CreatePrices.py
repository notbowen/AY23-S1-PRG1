# Written by: Hu Bowen
# Date: 12 May 2023
# Class: CSF02

# Read the prices list and write to prices.txt

# Libraries
import os

# Get folder where this script is stored
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "prices.txt")

# Prices list
prices = [ ["kopi", 0.4], 
           ["teh", 0.4], 
           ["milo", 0.5], 
           ["soft drinks", 1.20] ]

# Open file and loop thru list and write
with open(data_file, "w") as f:
    for item, price in prices:
        f.write("{}: ${:.2f}\n".format(item, price))
