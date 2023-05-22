# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Program to add up to 5 unique words,
# Enter x to stop adding words

# Initialise set to ensure unique words
words = []

# Ask user for 5 unique words, and stop when x is entered
while len(words) < 5:
    word = input("Enter word (x to exit): ")

    if word == "x":
        break

    if word not in words:
        words.append(word)
    else:
        print("{} has already been entered.".format(word))

# Display words
print("Your words are {}".format(words))

# Count no. of letters and display
total_len = len("".join(words))
print("The number of letters in these words is {}".format(total_len))
