# Written by: Hu Bowen, S10255800B
# Date: 15 May 2023
# Class: CSF02

# Variables
insurance_price = {
    "M": {
        25: 1.8,
        35: 1.5,
        45: 1.2,
        55: 1.0,
        65: 1.4,
        float("inf"): 1.7  # Extra big number to account for > 64
    },
    "F": {
        25: 1.4,
        35: 1.3,
        45: 1.1,
        55: 0.9,
        65: 1.2,
        float("inf"): 1.4  # Extra big number to account for > 64
    }
}

base_premium = 800

# Print title
print("Car Insurance Calculator")
print("========================")

# Ask user for gender, age and whether they have been in an accident
gender = input("Enter Gender [M/F]: ").upper()
age = int(input("Enter age: "))
had_accident = input("Have you been in a traffic accident before? [Y/N] ").upper() == "Y"

# Calculate insurance premium
for insurance_age, insurance_multiplier in insurance_price[gender].items():
    if age < insurance_age:
        premium_multiplier = insurance_multiplier
        break

insurance_premium = base_premium * premium_multiplier

if had_accident:
    insurance_premium += 300

# Output final premium price
print("Your annual premium is: {:.1f}".format(insurance_premium))
