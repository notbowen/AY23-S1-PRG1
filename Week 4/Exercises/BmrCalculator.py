# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Libraries
import os

# Get current folder and read data.txt from it
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "data.txt")

# Open data.txt and read data
with open(data_file) as f:
    data = f.read()
    data = data.split(",")

# Get gender and calculate BMR
if data[2] == "Male":
    bmr = 10 * float(data[0]) + 6.25 * (float(data[1]) * 100) - 5 * float(data[3]) + 5
else:
    bmr = 10 * float(data[0]) + 6.25 * (float(data[1]) * 100) - 5 * float(data[3]) - 161

# Print out extracted data + BMR
print(f"Weight: {data[0]}kg")
print(f"Height: {data[1]}m")
print(f"Age: {data[3]}")
print(f"Gender: {data[2]}")
print(f"BMR: {bmr:.1f} kcal/day")
