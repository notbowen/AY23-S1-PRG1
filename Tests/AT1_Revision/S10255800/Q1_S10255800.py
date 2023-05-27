# Hu Bowen (S10255800) - CSF02
# Date: 8 May 2023

# Notes:
# Interest Rate: (L + C) / (S + A * Y)
# where L is the loan amount, A is the annual income, C is the current loans, 
# S is the total savings and Y is the years to pay back loan

# Input: Get data from user
L = int(input("What is your desired loan amount? "))
A = int(input("What is your annual income? "))

C = int(input("What is the total value of your current loans? "))
S = int(input("What is the total of your savings? "))
Y = int(input("How many years do you want to pay back this loan? "))

# Process: Calculate the interest rate using formula
interest_rate = (L + C) / (S + A * Y)

# Output: Tell the user the interest rate
print("Your interest rate is {:.1f}%".format(interest_rate * 100))
