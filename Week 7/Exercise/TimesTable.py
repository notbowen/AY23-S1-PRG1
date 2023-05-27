# Written by: Hu Bowen (S10255800)
# Date: 27 May 2023
# Class: CSF02

# Prompts user to enter number
# Prints out math times table using for loop

# Prompt user for number
num = int(input("Please enter a number: "))

# Use for loop to print out math times table
for i in range(1, 11):
    print("\t{} x {}\t= {}".format(num, i, num * i))

print("The End")