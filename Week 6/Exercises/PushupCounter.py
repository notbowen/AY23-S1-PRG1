# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Prompt user for target pushups
# Keep counting pushups per day till
# they reach the target

# Ask for target pushups
target = int(input("Enter target number of pushups: "))

# Loop till target is hit
day = 0
pushups_done = 0

while pushups_done < target:
    day += 1
    pushups_done += int(input("Day {}: How many number of pushups did you do today? ".format(day)))

print("You did a total of {} pushups.".format(pushups_done))
print("You hit your target in {} days!".format(day))
