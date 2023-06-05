# Hu Bowen (S10255800) - CSF02

# Libraries
import sys

# Prompt user for 2 integers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# Swap num1 and num2 if num1 is greater than num2
if num1 > num2:
    num1, num2 = num2, num1

# Prompt user for integer between num1 and num2 inclusive
x = int(input("Enter a number between {} and {}: ".format(num1, num2)))

# Quit the program if the user inputs an invalid number
if not (num1 <= x <= num2):
    print("Invalid number entered")
    sys.exit(1)

# Display numbers from num1 to num2 in ascending order
# Replacing integers divisible by x with "skip"
skipped = 0
for i in range(num1, num2+1):
    to_print = i
    
    if i % x == 0:
        to_print = "skip"
        skipped += 1

    print("{:>5}".format(to_print))

# Display skipped integers
print("{} integers skipped".format(skipped))
