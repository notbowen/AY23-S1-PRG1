# Written by: Hu Bowen
# Date: 12 May 2023
# Class: CSF02

# Read the first 3 lines of the file,
# Read the contents line by line and print to screen with no blank lines

# Libraries
import os

# Get folder where this script is stored
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "todolist.txt")

# Read data from file
with open(data_file) as f:
    data = f.read().splitlines()

# Print the first 3 lines
for i in range(3):
    print(data[i])
