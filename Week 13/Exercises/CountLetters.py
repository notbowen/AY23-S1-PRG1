# Written by: Hu Bowen (S10255800)
# Date: 8 July 2023
# Class: CSF02

# Count the number of letters in a string

# Prompt user for a sentence
sentence = input("Enter a sentence: ").lower()

# Count the occurence of each letter
letters = {}
for c in sentence:
    if c.isalpha():
        try:
            letters[c] += 1
        except KeyError:
            letters[c] = 1

# Display letters in alphabetical order
letters = dict(sorted(letters.items()))
for letter, count in letters.items():
    print(letter, count, sep=" : ")
