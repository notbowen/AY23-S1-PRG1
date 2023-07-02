# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Functions to convert celsius to fahrenheit and vice-versa

def fahr_to_cel(fah: float) -> float:
    return 5.0 / 9.0 * (fah - 32)


def cel_to_fahr(cel: float) -> float:
    return 9.0 / 5.0 * cel + 32


# Runner code
while True:
    print("Temperature Conversion")
    print("[1]Fahrenheit to Celsius\n[2]Celsius to Fahrenheit\n[3]Exit")

    option = int(input("Please enter your option: "))

    if option == 1:
        fah = float(input("Please enter the temperature in Fahrenheit: "))
        cel = fahr_to_cel(fah)
        print("The temperature in celsius is {:.1f} degrees".format(cel))

    elif option == 2:
        cel = float(input("Please enter the temperature in Celsius: "))
        fah = cel_to_fahr(cel)
        print("The temperature in fahrenheit is {:.1f} degrees".format(fah))

    else:
        break

    print()
