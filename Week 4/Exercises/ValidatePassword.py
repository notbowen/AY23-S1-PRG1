# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Ask user for password
password = input("Enter a password: ")

# Check if length is at least 8 characters
if len(password) < 8:
    print("Password must be 8 characters long.")

# Check if password has at least 1 digit
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")

# Check if password has at least 1 uppercase letter
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")

# Valid password
else:
    print("Password is valid.")
