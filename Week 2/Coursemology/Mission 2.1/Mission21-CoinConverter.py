#Programming I

#####################################
#            Mission 2.1            #
#           Coin Converter          #
#####################################

#Background
#==========
#Tom has 2 50-cent coins, 4 20-cent coins, 6 10-cent coins and 9 5-cent coins.
#He would like calculate the total amount in dollars.

#Requirements
#============
#Develop a pseudocode and Python program to solve the following problem:
#   -Given a number of 50-cent coins, 20-cent coins, 10-cent coins
#    and 5-cent coins, calculate the amount in dollars, print the
#    output with proper description and the amount in proper format

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of your program.
#2) You MUST (at least) use the following variables:
#   - cent50 (number of 50-cent coins)
#   - cent20 (number of 20-cent coins)
#   - cent10 (number of 10-cent coins)
#   - cent5  (number of 5-cent coins)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
# 1. Get the number of 50-cent, 20-cent, 10-cent and 5-cent coins
# 2. Calculate the total amount using the formula:
#   - cent50 * 0.5 + cent20 * 0.2 + cent10 + 0.1 + cent5 * 0.05
# 3. Output the total amount in the format ${amount}, where amount is the total rounded to 2 decimal places



#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
cent50 = int(input("Enter the number of 50 cent coins: "))
cent20 = int(input("Enter the number of 20-cent coins: "))
cent10 = int(input("Enter the number of 10-cent coins: "))
cent5 = int(input("Enter the number of 5-cent coins: "))

#Process
total = cent50 * 0.5 + cent20 * 0.2 + cent10 * 0.1 + cent5 * 0.05

#Output
print("The total amount of cash you have is: ${}".format(total))
