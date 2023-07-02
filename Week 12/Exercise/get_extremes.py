# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to get the smallest and largest numbers in a list

from typing import List, Tuple
import math


def get_extremes(num_list: List[int]) -> Tuple[int, int]:
    """ Takes in a list of integers and returns a tuple, 
        which is structured as: (smallest number, largest number) """

    smallest = math.inf
    largest = -math.inf

    for num in num_list:
        if num < smallest:
            smallest = num
        if num > largest:  # No elif here to handle cases where there is only 1 element 
            largest = num

    return smallest, largest


# Runner code
# Sample input: 10, -13, 50, 5, 7, 65, -40, 44, 30
num_list = input("Enter some values, seperated with a ',': ").split(',')
num_list = [int(x.strip()) for x in num_list]

smallest, largest = get_extremes(num_list)

print("The smallest value is: {}".format(smallest))
print("The largest value is: {}".format(largest))
