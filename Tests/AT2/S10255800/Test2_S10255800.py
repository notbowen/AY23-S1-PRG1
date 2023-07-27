# Hu Bowen (S10255800) - CSF02

# Libraries
import os
import math

# Get file
current_folder = os.path.dirname(__file__)
data_file = os.path.join(current_folder, "trip_prices.txt")

# Load data
with open(data_file) as f:
    data = f.read().splitlines()
    trip_prices_list = [x.split(",") for x in data]

"""========== Part A =========="""
print("Trip prices:")
print(trip_prices_list[1:])
print("\n========================\n")

"""========== Part B =========="""
# Get number of adults, children and extensions
adults = 5
children = 2
extensions = 3

# Calculate number of adult twins and adult singles
adult_twins = adults // 2
adult_single = int(adults % 2)

# Calculate number of rooms for extension per night
total_pax = adults + children
rooms = math.ceil(total_pax / 2)

# Display the calculated results
print("Number of adults: {}".format(adults))
print("Number of children: {}".format(children))
print("Number of extension: {}".format(extensions))
print("Number of adult-twin for the tour package / land tour: {}".format(adult_twins))
print("Number of adult-single for the tour package / land tour: {}".format(adult_single))
print("Number of children for the tour package / land tour: {}".format(children))
print("Number of rooms for extension per night: {}".format(rooms))
print("\n========================\n")

"""========== Part C =========="""
# calculate the total amt
total_amt_list = [["Total Amount", "Amount w Land Tour"]]
for hotel, a_twn, a_sgl, chd, ext, land_a_twn, land_a_sgl, land_chd in trip_prices_list[1:]:
    total_amt = adult_twins * int(a_twn) + adult_single * int(a_sgl) + \
                children * int(chd) + rooms * int(ext) * extensions
    
    total_land_tour = total_amt + adult_twins * int(land_a_twn) + \
                      adult_single * int(land_a_sgl) + children * int(land_chd)

    total_amt_list.append([total_amt, total_land_tour])

# display
for trips, total_amts in zip(trip_prices_list, total_amt_list):
    hotel, a_twn, a_sgl, chd, ext, land_a_twn, land_a_sgl, land_chd = trips
    total_amt, total_land_tour = total_amts
    
    print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<10} {:<10} {:<10} {:<15} {:<15}".format(hotel, a_twn, a_sgl, chd, ext, land_a_twn, land_a_sgl, land_chd, total_amt, total_land_tour))

print("\n========================\n")

"""========== Part D =========="""
print("Options Available for SGD$25000 budget:")
for i, amounts in enumerate(total_amt_list[1:]):
    for j, amt in enumerate(amounts):
        if amt > 25000:
            continue

        print("\tHotel " + trip_prices_list[i+1][0], end=" ")

        if j:
            print("w land tour")
        else:
            print("w/o land tour")
