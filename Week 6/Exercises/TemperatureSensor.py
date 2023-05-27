# Written by: Hu Bowen (S10255800)
# Date: 22 May 2023
# Class: CSF02

# Read the data from the text file and store the values in a list;
# Display all the data with a warning message if the temperature is above 29 degrees;
# Calculate and display the average temperature

# Libraries
import os

# Get file
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "temperature.txt")

# Load data into list
with open(data_file) as f:
    temperatures = f.read().split(",")
    temperatures = [float(x.strip()) for x in temperatures]  # Remove spacing and convert to float

# Display data with warning msg
print("The temperatures are")
idx = 0
while idx < len(temperatures):
    print("  ", temperatures[idx]) if temperatures[idx] < 29.0 else print("  ", temperatures[idx], "** higher than 29!!!")
    idx += 1

# Display number of readings & avg temp
print("\nNumber of readings: {}".format(len(temperatures)))
print("Average temperature: {:.2f}".format(sum(temperatures) / len(temperatures)))
