# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Program to keep looping till a duplicate day is generated

import random

birthdays = set()
counter = 0

while counter == len(birthdays):
    birthday = random.randint(1, 365)
    print("{} was randomly generated.".format(birthday))

    birthdays.add(birthday)
    counter += 1

print("Duplicate day! This took {} tries.".format(counter))
