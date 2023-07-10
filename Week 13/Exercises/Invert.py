# Written by: Hu Bowen (S10255800)
# Date: 8 July 2023
# Class: CSF02

# Read a .csv file and load values into a dict

# Libraries
import os

# Open .csv file
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "colors.csv")

with open(data_file) as f:
    data = f.read().splitlines()

# Load into a dictionary
colors_dict = {}
for line in data:
    name, color = line.split(',')
    colors_dict[name] = color

# Invert dictionary
new_colors = {}
for name, color in colors_dict.items():
    try:
        new_colors[color].append(name)
    except KeyError:
        new_colors[color] = [name]

# Display inverted dictionary
print(new_colors)
