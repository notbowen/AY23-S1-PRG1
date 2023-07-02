# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to print a square shaped pattern

def print_square(side: int) -> None:
    """ Prints out a square with length of side """

    for _ in range(side):
        print("* " * side)

# Runner code
side = int(input("Enter length of side: "))
print()
print_square(side)
