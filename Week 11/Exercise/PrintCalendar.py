# Written by: Hu Bowen (S10255800)
# Date: 25 June 2023
# Class: CSF02

# Program to render a calendar based on starting day
# and number of days

# Variables
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Get number of days and starting day
total_days = int(input("Enter number of days: "))
start_day = input("When is the first day of the week: ")

# Print header
print(" ".join(days))

# Init calendar list
calendar = []

# Loop through each day in the calendar and calculate difference from start day
start_day = days.index(start_day)

for week in range(6):
    day_list = []
    for day in range(7):
        day_from_0 = week * 7 + day  # What day it would be if the month started from Sunday
        actual_day = day_from_0 - start_day + 1  # The difference between the start day and the day from 0 would give the actual day

        if actual_day > 0 and actual_day <= total_days:
            day_list.append("{:3}".format(actual_day))  # If days are within range
        elif actual_day <= 0:
            day_list.append("   ")  # Day is from previous month
        else:
            break  # We are done
    calendar.append(day_list)

# Convert calendar to string and display
calendar = [" ".join(week) for week in calendar]
calendar = "\n".join(calendar)

print()
print(calendar)
