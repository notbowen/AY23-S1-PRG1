# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Get year from user
year = int(input("Enter a year: "))

# Check if year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
