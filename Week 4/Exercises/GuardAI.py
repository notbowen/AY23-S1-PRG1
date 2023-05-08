# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Prompt user if the guard sees the player
sees_player = input("Does the guard see the player? (y/n) ")

# If the guard does not see the player then end the program
if sees_player == "n":
    print("The guard waits.")
    quit()

# Prompt user for distance
distance = int(input("How far away is the player? "))

# If the player is 1 unit away or less, the guard will attack
if distance <= 1:
    print("The guard attacks.")
# If the player is 2 units to 4 units away, the guard will advance
elif 2 <= distance <= 4:
    print("The guard advances.")
# If the player is 5 units or more away, the guard will wait
elif distance >= 5:
    print("The guard waits.")
