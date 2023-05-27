# Written by: Hu Bowen (S10255800)
# Date: 27 May 2023
# Class: CSF02

# Prompt user for days
# Print out Day and Tasks, and repeat header every 7 days

# Get days
days = int(input("Enter number of days: "))

# Loop thru days and print
for day in range(days):
    if day % 7 == 0:  # Print header every week
        print("{:>3} | Task(s)".format("Day"))

    print("{:>3} |".format(day+1))
