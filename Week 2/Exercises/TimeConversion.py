# Written by: Hu Bowen
# Date: 24 Apr 2023
# Class: CSF02

# Input
# Accept the time from user in seconds
time = int(input("Please enter the time to be converted, in sec: "))

# Process
hour = time // 3600
time = time % 3600

minute = time // 60
time = time % 60

second = time

# Output
print("Time: {} hr, {} min {} sec".format(hour, minute, second))

