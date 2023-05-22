#Programming I

#############################
#     Side Quest 6.1        #
#   Driverless Vehicle 2    #
#############################

#Background
#==========
#Tom would like to enhance the safety of his driverless vehicle by applying braking when
#the vehicle is less than 50 meters from an object. 

#Write a Python program that prompts the user to enter a set of round trip times
#(similar to previous question, each value to be separated by commas, and speed of sound
#at 344 m/s), and returns True if the vehicle is too near an object or False if the
#vehicle is within safe margin of other objects.



#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - roundTrips
#   - tooNear



#START CODING FROM HERE
#======================

# Function to get distance in (m)
def distance(time: str) -> float:
    return 344 * (float(time) / 2)

# Find closest object
def closest_object(roundTrips):
    #Perform the parsing of roundTrips input here
    roundTrips = roundTrips.split(",")

    # Ensure round trips have a min length of 5
    if len(roundTrips) < 5:
        return [-1, -1]
    
    # Calculate distances
    distances = []

    i = 0
    while i < len(roundTrips):
        distances.append(distance(roundTrips[i])) 
        i += 1

    # Find the closest + index
    least_distance = min(distances)
    least_index = distances.index(least_distance)

    closestObject = [least_index, least_distance]
    return closestObject#Do not remove this line

#Check closest object
def fail_safety_distance(roundTrips):
    #Perform the parsing of roundTrips input here
    closest = closest_object(roundTrips)[1]
            
    #Check whether vehicle is too near an object, return True if so, False otherwise
    tooNear = closest < 50
    
    return tooNear#Do not remove this line

#Prompt user to enter a minimum of 5 round trip times separated with commas
roundTrips = "0.1,2.0,1.6,.5,1"
    
result = fail_safety_distance(roundTrips)

#Modify to display if vehicle is too near an object 
print("The vehicle {} too close to other objects.".format("is" if result else "is not"))

#input 0.5,2.1,0.3,1.8,2.3  output False
#input 0.1,2.0,1.6,.5,1     output True
