# Written by: Hu Bowen
# Date: 3 May 2023
# Class: CSF02

# Libraries
import os

# Find the directory of StudentData.py
file_path = os.path.dirname(os.path.abspath(__file__))
student_data_path = os.path.join(file_path, "StudentData.txt")

# Read the first 2 lines of data
friends = []
with open(student_data_path) as f:
    data = f.read().splitlines()
    friends = data[:2]

# Process the data
friends = [friend.split(",") for friend in friends]

# Display the friends
print("{:15} Mobile Contact".format("Name"))
for name, number in friends:
    print("{:15} {}".format(name, number))
