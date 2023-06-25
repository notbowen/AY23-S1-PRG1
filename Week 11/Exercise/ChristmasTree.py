# Written by: Hu Bowen (S10255800)
# Date: 25 June 2023
# Class: CSF02

# Program to print a pyramid shape using user-specified character
# And user-specified height

# Get character and height
char = input("Enter a character: ")
height = int(input("Enter a number: "))

# Loop through height and print pyramid shape
# From the question we can see that each row has height - current row number of spaces
# E.g Row 1 has 6 - 1 = 5 spaces before the character,
#     Row 2 has 6 - 2 = 4 spaces before the character
# 
# We can see that the number of * corresponds to the current row number
# E.g Row 1 has 1 star, Row 2 has 2 stars
for row in range(height):
    spaces = " " * (height - (row + 1))  # +1 as python starts from 0
    print(spaces, end="")

    stars = "* " * (row + 1)
    print(stars)

# Print merry christmas at the end
print("Merry Christmas!")
