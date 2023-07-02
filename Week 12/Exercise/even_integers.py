# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to check if number is even

def is_even(n: int) -> bool:
    """ Checks if a value is even or odd """
    return n % 2 == 0


# Code to display even integers in list
num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
even_nums = []

for num in num_list:
    if is_even(num):
        even_nums.append(str(num))

print("Even numbers: " + ", ".join(even_nums))
