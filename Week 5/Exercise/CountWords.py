# Written by: Hu Bowen
# Date: 12 May 2023
# Class: CSF02

# Libraries
import os

# Get folder where this script is stored
current_folder = os.path.dirname(__file__)

# Prompt user for filename
filename = input("Please enter the filename: ")
data_file = os.path.join(current_folder, filename)

# Get data from file
with open(data_file) as f:
    data = f.read()

# Count number of spacings (words)
words = len(data.split())
print("Number of words in {}: {}".format(filename, words))

# Write number of words to output.txt
data_file = os.path.join(current_folder, "output.txt")
with open(data_file, "w") as f:
    f.write("There are {} words in the document.".format(words))
    print("Number of words successfully written to output.txt")
