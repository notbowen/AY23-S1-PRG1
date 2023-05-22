# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Prompt user for PIN,
# if incorrect PIN is entered 3 times,
# lock the account

# Variables
PIN = "123"

# Keep track of count
count = 0

# While incorrect tries < 3, keep asking for input and check
while count < 3:
    input_pin = input("Enter pin: ")
    if input_pin == PIN:
        break

    print("Invalid pin.", end=" ")
    print("Please try again.") if count != 2 else print("You have no more tries.")

    count += 1

# Tell user account unlocked/locked
if count == 3:
    print("Your account is locked.")
else:
    print("Your account is unlocked!")
