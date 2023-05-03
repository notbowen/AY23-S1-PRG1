# Written by: Hu Bowen
# Date: 1 May 2023
# Class: CSF02

# Get original string and substring to delete
original = input("Enter original string: ")
sub_delete = input("Substring to delete: ")

# Remove substring
new_str = original.replace(sub_delete, "", 1)

# Output new string
print("The modified string is: {}".format(new_str))
