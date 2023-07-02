# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to convert celsius to fahrenheit

def convert_temperature(celsius: int) -> float:
    """ Takes in a degree in celsius and returns the fahrenheit value """
    f = (celsius * 9 / 5) + 32
    return f


# Runner code
cel = int(input("Enter the temperature in degree celsius: "))
f = convert_temperature(cel)
print("The temperature is equivalent to {:.1f} fahrenheit.".format(f))
