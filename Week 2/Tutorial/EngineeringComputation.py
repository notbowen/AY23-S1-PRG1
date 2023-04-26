# Written by: Hu Bowen
# Date: 26 April 2023
# Class: CSF02

"""
Question Overview:
- User inputs:
    - Radius & Height of cylinder
    - Radius of sphere
    - Mass of 2 objects & Distance in between

- Find volume of cylinder (2dp)
- Find surface area of sphere (2dp)
- Force of gravity (2dp, scientific notation)
"""

# Libraries
import math

# Constants
G = 6.6743e-11

# Input
c_radius = float(input("Enter the radius of the cylinder (in m): "))
c_height = float(input("Enter the height of the cylinder (in m): "))

s_radius = float(input("Enter the radius of the sphere (in m): "))

m1 = float(input("Enter the mass of object 1 (in kg): "))
m2 = float(input("Enter the mass of object 2 (in kg): "))
r = float(input("Enter the distance between the objects (in m): "))

# Process
c_volume = math.pi * (c_radius ** 2) * c_height
s_surface = 4 * math.pi * (s_radius ** 2)
force = (G * m1 * m2) / (r ** 2)

# Output
print("Results:")
print("\tVolume of the cylinder: {:.2f} cubic meters".format(c_volume))
print("\tSurface area of the sphere: {:.2f} square meters".format(s_surface))
print("\tForce of gravity between the objects: {:.2e} Newtons".format(force))
