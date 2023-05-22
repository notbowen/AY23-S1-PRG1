# Written by: Hu Bowen (S10255800) 
# Date: 22 May 2023 
# Class: CSF02

# Program to ask user for a number
# and prints out the times table for that number
# from 1 to 10

# Ask user for number
num = int(input("Please enter a number: "))

# While loop to count number and display
multiply = 1
while multiply < 11:
    print("    {} x {} = {}".format(num, multiply, num * multiply))
    multiply += 1

# Display "The End"
print("The End")
