#Programming I

#####################################
#            Mission 2.1            #
#    Compound Interest Calculator   #
#####################################

#Background
#==========
#Tom won a lottery amounting to $10000, and he is deciding if he should
#deposit it into a bank account to accumulate interest.

#Tom wishes to find out how much he will have in the bank account after
#a specified number of years, given his input.

#Requirements
#============
#1) Write pseudocode that sets the principal amount of $10000 to variable p,
#   annual nominal interest rate of 8% to variable r, number of times the
#   interest is compounded per year of 12 to variable n. The number of years
#   that the money will be compounded, t, is given by the user. Calculate
#   and print the final amount (up to 3 decimal places) after t years.
#   Note: Refer to the question in Coursemology for the formula.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - P (principal amount)
#   - r (annual nominal interest rate [as a decimal])
#   - n (number of times the interest is compounded per year)
#   - t (number of years)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
# 1. Set p to 10000
# 2. Set r to 8% (0.08)
# 3. Set n to 12
# 4. Prompt the number of years to be compounded and save it to t
# 5. Calculate the final amount using the equation provided in Coursemology
# 6. Round the final amount to the nearest 3 decimal place and output


#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
P = 10000
r = 0.08
n = 12
t = int(input("Enter the number of years to be compounded: "))

#Process
final = P * (1 + (r / n)) ** (n * t)

#Output
print("Your final amount after {} years would be: ${:0.3f}".format(t, final))
