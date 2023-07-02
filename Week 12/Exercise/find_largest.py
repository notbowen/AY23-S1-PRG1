# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to find the larger integer amongst 2 numbers

def find_larger(n1: int, n2: int) -> int:
    """ Returns the larger number """
    return n1 if n1 > n2 else n2


# Runner code to find largest integer amongst 4 ints
i1 = int(input("Enter the first integer numbr: "))
i2 = int(input("Enter the second integer numbr: "))
i3 = int(input("Enter the third integer numbr: "))
i4 = int(input("Enter the forth integer numbr: "))

l1 = find_larger(i1, i2)
l2 = find_larger(i3, i4)

ans = find_larger(l1, l2)

print("The largest integer is {}".format(ans))
