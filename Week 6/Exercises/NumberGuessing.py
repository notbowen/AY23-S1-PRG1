# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Generates a number between 1 to 100 (inclusive)
# User gets 5 tries
# User can input -1 to quit

# Libraries
import random

# Generate random no
ans = random.randint(1, 100)

# Max 5 tries to guess answer
tries = 0
while tries < 5:
    guess = int(input("Try {}: Enter a number between 1 and 100 (or -1 to end): ".format(tries+1)))

    if guess == -1:
        break

    if guess > ans:
        print("{} is too high.".format(guess))
    elif guess < ans:
        print("{} is too low.".format(guess))
    else:
        print("Bingo, you've got it right!")
        break

    tries += 1

# Tell user they ran out of tries
if tries == 5:
    print("You have ran out of tries!")

print("Bye-bye!")
