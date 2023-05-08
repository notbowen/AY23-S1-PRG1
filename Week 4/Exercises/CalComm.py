# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Each agent is paid 10% commission for monthly sales above or equal to $10,000
# and 5% commission for monthly sales below $10,000

# Sales amount
monthly_sales = float(input("Enter monthly sales of sales agent: "))

# Calculate commission
if monthly_sales >= 10000:
    commission = monthly_sales * 0.1
    commission_rate = 10
else:
    commission = monthly_sales * 0.05
    commission_rate = 5

# Display commission rate in percentage and amount paid
print("Commission rate is : {}%".format(commission_rate))
print("Commission paid is : ${:.2f}".format(commission))
