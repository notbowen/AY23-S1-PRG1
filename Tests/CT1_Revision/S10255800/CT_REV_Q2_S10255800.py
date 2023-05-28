# Hu Bowen (S10255800) - CSF02

# Variables
total = 0
ace_count = 0

# Ask user for 3 card values
for i in range(3):
    value = int(input("Enter card {}: ".format(i+1)))

    # Clamp max value to 10 as 11, 12 and so on correspond to value 10
    if value > 10:
        value = 10

    if value == 1:
        # Count number of aces received
        ace_count += 1
    else:
        # Increment total if it's not an ace
        total += value

# Try adding the aces to the value and check if it exceeds 21
for ace in range(ace_count):
    if total + 11 < 21:
        total += 11
    else:
        total += 1

# Output total card value
print("Total value is {}".format(total))
