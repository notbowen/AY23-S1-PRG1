#Programming I

#######################################
#            Mission 3.2              #
#   Calculate Daily Total Energy Cost #
#######################################

#Background
#==========
#The total energy cost is calculated using this formula: 
#   Total Energy Cost ($) = Total Energy consumed (kW) x Electricity tariff
#Note: Electricity tariff is $0.2743 as of April 2023 for SP group

#Write a Python program that calculates and displays the total energy cost
#based on the input of usage for various appliances and their Power rating

#]entered by user and the displays a table of energy in watts/hour
#for various appliances and prompt user to enter the daily hours for
#each appliance. The program then displays the table again with the
#daily hours and calculated value of the total daily energy cost.


#Important Notes
#===============
#1) You are required to include a function called calculateEnergyCost(), which
#   accepts a list (appliance_list, which contains a list of appliances' names
#   together with their energy in watts per hour) and a string (hrs_input, which
#   contains the daily hours used for each appliances, separated in ';'),
#   calculates total daily energy cost and returns the result
#2) When testing the program in IDLE, you should prompt the user for the input
#   value. However, you must comment out the input prompt before submitting it
#   in coursemology


#START CODING FROM HERE
#======================

#Perform Calculation of Total Daily Energy Cost
def calculateEnergyCost(appliance_list,hrs_input):
    
    TARIFF = 0.2743 #define tariff
    
    #Code to parse the input string in hrs_input (Hint: Use the split() function)
    hr_list = hrs_input.split(";")


    #Display list of appliances and daily hours used
    print("List of Electrical Appliances with Energy in Watts/Hr:")
    print("{:19}".format("Name"), end="")
    print("{:16}".format("Energy(Watts/Hr)"), end="")
    print("Daily Hrs used")

    for (appliance, watt), hours in zip(appliance_list, hr_list):
        print("{:<19}".format(appliance), end="")
        print("{:<16}".format(watt), end="")
        print("{}".format(hours))

    
    #Calculate total energy of all appliances    
    total_energy = [(watt / 1000) * float(hours) for (_, watt), hours in zip(appliance_list, hr_list)]
    total_energy = sum(total_energy)

    
    #Calculate total daily energy cost
    total_energy_cost = total_energy * TARIFF
    
    #Display daily energy consumption and total daily energy cost    
    print("Total daily energy consumed (kW): {:.2f}".format(total_energy)) 
    print("Total daily energy cost ($): {:.2f}".format(total_energy_cost)) 

    #Return the total daily energy cost 
    return total_energy_cost #Do not remove/edit this line


#Create a list named appliance_list with the 3 appliances shown in the
#screenshot in Coursemology
# appliance_list = [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]]

#Display the list of appiances with energy in watts/hr
#print("List of Electrical Appliances with Energy in Watts/Hr:")
#print("{:19}".format("Name"), end="")
#print("{:16}".format("Energy(Watts/Hr)"))
#
#for appliance, watt in appliance_list:
#    print("{:<19}".format(appliance), end="")
#    print("{:<16}".format(watt))


#Prompt and obtain input for daily consumption for appliances
# hrs_input = input("Enter daily hours used for the above appliances seperated by ';' : ")
    
#Do not remove the next line that calls the function
# total_energy_cost = calculateEnergyCost(appliance_list, hrs_input)

#Modify the statement to display the decimal value
#print(   )

#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'5;4;24'
#output 2.73
#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'8;8;24'
#output 4.10
