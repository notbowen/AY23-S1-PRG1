# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Read mark file and display formatted data

# Libraries
import os

# Get file
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "marks.txt")

# Load data
with open(data_file) as f:
    data = f.readlines()
    data = [x.split(";") for x in data]

# Print data
print("Name\t\tMark")
print("----\t\t----")
for name, mark in data:
    print("{}\t{}".format(name, float(mark)))

# Calculate avg mark
avg = [float(mark) for _, mark in data]
avg = sum(avg) / len(avg)

print("\nAverage Mark:\t{}".format(avg))
