# Hu Bowen (S10255800) - CSF02
# Program to calculate surface area of cylinder from
# radius and height, both which are taken from user input

# Libraries
import math

# Input: Radius and height
height = float(input("Enter height of cylinder in cm: "))
radius = float(input("Enter radius of base circle of cylinder in cm: "))

# Process: Calculate total surface area
total_sa = 2 * math.pi * (radius ** 2) + 2 * math.pi * radius * height

# Output: Show the calculated total surface area to 2 decimal places
print("\nTotal Surface Area is: {:.2f}cm squared".format(total_sa))
