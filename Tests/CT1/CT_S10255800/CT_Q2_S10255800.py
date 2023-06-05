# Hu Bowen (S10255800) - CSF02
# Word swapper

# Prompt user for word in lowercase
word = input("Enter your word: ").strip().lower()
word = list(word)  # Convert word to list so that it is mutable

# Display number of characters in the word
print("Your input has {} characters".format(len(word)))

# Ask user to input 2 numbers that selects 2 characters within the word
# Assume no index out of range
indexes = input("Input the positions of the characters to select, seperated by ',': ")
indexes = [int(x) - 1 for x in indexes.split(',')]  # Convert to int and apply offset
p1, p2 = indexes  # Unpack indexes into individual variables

# Print the 2 characters selected
w1 = word[p1]
w2 = word[p2]
print("Swapping the characters '{}' and '{}'".format(w1, w2))

# Swap all occurrences of the selected characters
word = [w2 if w == w1 else w1 if w == w2 else w for w in word]  # This does the same as the for and if else below

##for i in range(len(word)):
##    if word[i] == w1:
##        word[i] = w2
##    elif word[i] == w2:
##        word[i] = w1

# Convert word back to string
word = "".join(word)

# Print the scrambled word
print("Scrambled word: {}".format(word))
