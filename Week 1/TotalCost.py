# Hu Bowen, S10255800B

# Prompt user for price and GST percentage
price = float(input("Enter the price of the item: "))
gst = float(input("Enter the GST's percentage value (e.g. 8% -> 8): "))

# Calculate total cost
total = price * (1 + (gst / 100))
print("$" + str(total))