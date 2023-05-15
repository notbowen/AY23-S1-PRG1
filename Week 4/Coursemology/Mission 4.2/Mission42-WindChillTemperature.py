# Written by: Hu Bowen
# Date: 15 May 2023
# Class: CSF02

# Ask user for temp and wind speed
temp = float(input("Please enter the outside temperature in Fahrenheit: "))
wind_spd = float(input("Please enter the wind speed in miles per hour: "))

# Validate input
if not (-58 <= temp <= 41) or wind_spd <= 2:
    print("Incorrect input")
    quit()

# Calculate wind chill temperature
twc = 35.74 + 0.6215 * temp - 35.75 * wind_spd ** 0.16 + 0.4275 * temp * wind_spd ** 0.16

# Output the wind chill temperature
print("The wind-chill index is {:.2f}".format(twc))
