# Written by: Hu Bowen
# Date: 26 April 2023
# Class: CSF02

# Libraries
import os

# Find the directory of StudentData.py (as StudentData.txt is stored there too)
file_path = os.path.dirname(os.path.abspath(__file__))
student_data_path = os.path.join(file_path, "StudentData.txt")

# Load data from file
with open(student_data_path) as f:
    data = f.read().splitlines()

# Display only first, third and fifth data on screen
for i in range(0, 5, 2):
    print("{} {}".format(i+1, data[i]))
