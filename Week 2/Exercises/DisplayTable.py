# Written by: Hu Bowen
# Date: 26 April 2023
# Class: CSF02

# Libraries
import math

# Display heading
print("{:6}  ".format("Number"), end="")  # Ending char is overwritten to not print \n
print("{:6}  ".format("Square"), end="")
print("{:11}  ".format("Square root"), end="")
print("{:7}".format("English"))

# Variables
numbers = [1, 2, 3, 4, 5]
numbers_str = ["One", "Two", "Three", "Four", "Five"]

# Ensure numbers and numbers_str can be mapped to each other (same length)
assert len(numbers) == len(numbers_str)

# Loop through and print
for i in range(len(numbers)):
    # Calculate required data
    number = numbers[i]
    square = number ** 2
    sqare_root = math.sqrt(number)
    english = numbers_str[i]

    # Print required data
    print("{:>6}  ".format(number), end="")
    print("{:^6}  ".format(square), end="")
    print("{:^11.2f}  ".format(sqare_root), end="")
    print("{:>7}".format(english))
