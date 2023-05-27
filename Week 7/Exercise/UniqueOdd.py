# Written by: Hu Bowen (S10255800)
# Date: 27 May 2023
# Class: CSF02

# Given a list of integers
# Use for loop to read numbers given and
# - Choose first 5 unique odd numbers
# - Discard the duplicates
# - Create a list to store findings
# - Print the 5 unique numbers found
# - If fewer than 5 unique numbers, print all odd numbers available

# List of integers
numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]

# Create a list to store unique odd numbers
unique_odd_numbers = []

# Loop through numbers till the set 5 numbers, or no more numbers left
for num in numbers:
    if len(unique_odd_numbers) == 5: break

    # Add number to list if it's odd and hasn't been added
    if num % 2 and (num not in unique_odd_numbers):
        unique_odd_numbers.append(num)

# Print out odd numbers found
print(unique_odd_numbers)
