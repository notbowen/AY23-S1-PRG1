# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to calculate x ** n

def power(x: int, n: int) -> int:
    return x ** n

# Runner code
x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

result = power(x, n)
print("The value of {} ** {} is {}".format(x, n, result))
