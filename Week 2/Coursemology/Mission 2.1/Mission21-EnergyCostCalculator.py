#Programming I

###############################
#       Mission 2.1           #
#    Energy Cost Calculator   #
###############################

#Background
#==========
#Ever wonder the energy cost of running an appliance or electronic device?
#Here is a simple calculation to get that figure.

#Step 1:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000

#Step 2:
#Cost = Monthly electricity consumption * Electricity tariff
#                                         ($0.2743 as of April 2023 for SP group)

#Laptop computers may peak at a maximum draw of only 60 watts,
#whereas common desktops may peak around 175 watts.

#Requirements
#============
#1) Write pseudocode for the Energy Cost Calculator.
#   The solution should prompt user for the power rating of a device and the
#   number of hours used per day. After which, display the calculated cost in
#   4 decimal places.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - power_rating
#   - hours

#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
# 1. Prompt the user for power rating of a device
# 2. Prompt the user for the total number of hours used per day
# 3. Calculate the power using the formula stated above
# 4. Round the total cost to 4 decimal places and output the cost


#TYPE YOUR PYTHON CODE BELOW
#===========================

# Constants
TARIFF = 0.2743

#Input
power_rating = int(input("Enter the power rating of the device (in watts): "))
hours  = int(input("Enter the total number of hours the device is used per day: "))

#Process
monthly_electricity_consumption = (power_rating * hours) / 1000
cost = monthly_electricity_consumption * TARIFF

#Output
print("Your monthly electricity cost is: ${:0.4f}".format(cost))
