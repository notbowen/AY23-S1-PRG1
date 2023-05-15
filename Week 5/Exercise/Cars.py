# Written by: Hu Bowen
# Date: 12 May 2023
# Class: CSF02

# Libraries
import os

# Get folder where this script is stored
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "cars.txt")

# Read data from file
with open(data_file) as f:
    cars = f.read().splitlines()[-4:]
    cars = [x.split(" : ") for x in cars]

# Print choices of cars
for i, (model, price) in enumerate(cars):
    print("{}. {} : {}".format(i+1, model, price))

# Enter order information
order_number = input("Enter the order number: ")
name = input("Customer Name: ")
car_choice = int(input("Enter car choice: ")) - 1

# Structure output
output = "{} ordered the {} at the price of {}".format(name, cars[car_choice][0], cars[car_choice][1])

# Write to customer order file
data_file = os.path.join(current_folder, "{}.txt".format(order_number))
with open(data_file, "w") as f:
    f.write(output)

# Confirm with user
print("Car has been successfully ordered.")
