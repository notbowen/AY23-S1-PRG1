# Written by: Hu Bowen
# Date: 24 Apr 2023
# Class: CSF02

# Libraries
import math

# Input
a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))

# Process
# Calculate diameter
c = math.sqrt(a ** 2 + b ** 2)

# Calculate radius and use it to get area
radius = c / 2
area = math.pi * (radius ** 2)

# Output
print("The length of c is {}".format(c))
print("The area of the circle is {}".format(area))
