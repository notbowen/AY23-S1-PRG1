# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to check and print if number is even

def is_even(n: int) -> None:
    """ Checks if a value is even or odd, and print the number if even """
    if n % 2 == 0:
        print(n)


# Runner code
num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
even_nums = []

print("Even Numbers")
print("============")
for num in num_list:
    is_even(num)
