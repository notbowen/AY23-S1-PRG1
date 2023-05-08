# Hu Bowen (S10255800) - CSF02
# Date: 8 May 2023

# Notes:
# To validate a given vehicle plate number with 4 digits starting with ‘S’:
# 1. Ignore the letter S
# 2. Assign the numbers to their index in the alphabet (A=1, B=2, C=3 ...)
# 3. Map and multiply the 6 numbers by [9, 4, 5, 4, 3, 2]
# 4. Modulo the number by 19 and get the remainder
# 5. The last letter should be the index of the remainder in the alphabet

# Libraries
import string

# Variables
final_letters = "AZYXUTSRPMLKJHGEDCB"

# Input: Get the vehicle plate number
plate_no = input("Enter the vehicle number to be validated: ").upper()
plate_no = plate_no[1:]  # Strip off the "S"

# Process: Validate the vehicle no.
# Map the first 2 letters to their index in the alphabet
# And convert the rest to integers
plate_no_list = []
for c in plate_no[:-1]:
    char = int(c) if c.isdigit() else (string.ascii_uppercase.find(c) + 1)
    plate_no_list.append(char)

# Map and multiply the numbers
checksum = sum([a * b for a, b in zip(plate_no_list, [9, 4, 5, 4, 3, 2])])

# Get the remainder
remainder = checksum % 19

# Output: The validity of the vehicle number
valid = final_letters[remainder] == plate_no[-1]  # Check if index == last char
print("Validity of the vehicle number: {}".format("Valid" if valid else "Invalid"))
