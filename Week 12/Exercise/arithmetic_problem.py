# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Activity 14
# Let user choose different arithmetic problem

# Libraries
import random
from typing import Tuple

# Functions


def print_menu() -> int:
    """Shows the menu and returns the option selected by user

    Returns:
        int: The selected option
    """

    print("Choose from the following options:")
    print("1. Addition Problems")
    print("2. Subtraction Problems")
    print("3. Multiplication Problems")
    print("4. Division Problems")

    choice = int(input("\nEnter your choice: "))
    return choice


def print_incorrect_msg() -> None:
    """Displays a random message telling the user is incorrect"""

    choices = [
        'No. Please try again.', 'Wrong. Try once more.',
        'Don\'t give up!', 'No. Keep trying.'
    ]

    chosen = random.choice(choices)
    print(chosen)


def print_correct_msg() -> None:
    """Displays a random message telling the user is correct"""

    choices = ['Very good!', 'Excellent!',
               'Nice work!', 'Keep up the good work!']

    chosen = random.choice(choices)
    print(chosen)

def generate_numbers() -> Tuple[int, int]:
    """Generates 2 random numbers between 1 and 9

    Returns:
        int: The 1st generated number
        int: The 2nd generated number
    """
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    return a, b

def get_answer_and_operation(a: int, b: int, choice: int) -> Tuple[float, str]:
    """Returns the answer based on the 2 input values and the choice

    Args:
        a (int): The first value to do the operation against
        b (int): The second value to do the operation against
        choice (int): The choice the user input

    Returns:
        int: The result of the first and second value going through the chosen operation
        str: The operation
    """

    if choice == 1:
        return a + b, '+'
    elif choice == 2:
        return a - b, '-'
    elif choice == 3:
        return a * b, '*'
    else:
        return a / b, '/'

# Main loop
while True:
    # Generate numbers and answer
    choice = print_menu()
    a, b = generate_numbers()
    ans, op = get_answer_and_operation(a, b, choice)

    while True:
        # Keep trying until user is correct
        user_ans = float(input("How much is {} {} {}? \n> ".format(a, op, b)))
        if user_ans == ans:
            break

        print_incorrect_msg()

    # Print congrats and move on
    print_correct_msg()
    print()
