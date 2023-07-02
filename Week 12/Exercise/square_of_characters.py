# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to print a square shaped pattern based on a character

def print_square(side: int, char: str) -> None:
    char = char.strip() + " "
    for _ in range(side):
        print(char * side)

# Runner code
side = int(input("Enter length of side: "))
char = input("Enter character to print: ")

print()
print_square(side, char)
    