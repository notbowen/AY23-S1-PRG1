# Hu Bowen (S10255800) - CSF02

# Get sys lib to quit program
import sys

# Ask user for number
n = int(input("Enter a number between 0 and 5000: "))

# Loop through triangular numbers till >= 5000
triangular_index = 0
triangular_number = 0
while triangular_number <= 5000:
    triangular_number = ((triangular_index ** 2) + triangular_index) / 2
    if triangular_number == n:
        print("{} is  triangular number and it is the {}th number.".format(n, triangular_index))
        sys.exit(0)
    triangular_index += 1

print("{} is NOT a triangular number.".format(n))
