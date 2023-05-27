# Written by: Hu Bowen (S10255800)
# Date: 27 May 2023
# Class: CSF02

# Keep prompting user till user inputs zero (zero is not part of list)
# List all odd integers in increasing order
# List all even integers in increasing order
# Print average of all numbers

# Variables
even_numbers = []
odd_numbers = []

# Keep prompting user till user inputs zero
while True:
    num = int(input("Please enter a number (0 to end): "))
    if num == 0: break

    if num % 2:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

# List all odd integers in increasing order
odd_numbers.sort()
print("Odd numbers: {}".format(odd_numbers))

# List all even integers in increasing order
even_numbers.sort()
print("Even numbers: {}".format(even_numbers))

# Calculate and print average
total = sum(even_numbers + odd_numbers)
length = len(even_numbers + odd_numbers)

print("Average = {:.2f}".format(total / length))
