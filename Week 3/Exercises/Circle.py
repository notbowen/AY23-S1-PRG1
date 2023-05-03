# Written by: Hu Bowen
# Date: 24 Apr 2023
# Modified on: 3 May 2023
# Class: CSF02

# Libraries
import math

# Calculate area function
def calculate_circle(a: float, b: float) -> float:
    # Calculate diameter
    c = math.sqrt(a ** 2 + b ** 2)

    # Calculate radius and use it to get area
    radius = c / 2
    area = math.pi * (radius ** 2)

    return area

# Input
a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))

# Process
area = calculate_circle(a, b)

# Output
print("The area of the circle is {}".format(area))
