# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Generate two integers between 0 and 100 inclusive and prompts the user to enter the sum of these 2 integers. 
# Print if the answer is correct or wrong

# Libraries
import random

# Generate two integers between 0 and 100 inclusive
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

# Calculate sum of two integers
sum = num1 + num2

# Prompt user to enter the sum of these 2 integers
user_sum = int(input("Enter the sum of {} and {}: ".format(num1, num2)))

# Compare user_sum with sum
if user_sum == sum:
    print("Your answer is correct!")
else:
    print("Your answer is wrong.")
    print("The correct answer is {}.".format(sum))
