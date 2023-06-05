# Hu Bowen (S10255800) - CSF02

# Formula table
formulas = [
    ["1.2", "0.15 * y + 1.2"],
    ["(2 ** (x - 1)) * 0.3 + 1", "(2 ** x) * 0.15 * y + 1.2"],
]

# Prompt user for number of books and days it is late
y = int(input("Please enter the number of books that are late: "))
x = int(input("Please enter the number of days the books are late: "))

# Calculate fine based on values entered
# Makes use of list being able to be indexed by True(1) & False(0)
# values to get right formula
# 0th row indicates 1 day late, x != 1 would result in 0 if it's 1 day late
# And vice-versa. Same logic applies for the the columns
fine = eval(formulas[x != 1][y != 1])

# Display message showing the fine
print("The fine for {} book(s) for {} day(s) is ${:.2f}".format(y, x, fine))
