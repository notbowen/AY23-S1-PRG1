#Programming I

#######################
#     Mission 5.1     #
#   Vitality Points   #
#######################

#Background
#==========
#To encourage their customers to exercise more, insurance companies are giving
#vouchers for the distances that customers had clocked in a week as follows:


######################################################
#     Distance (km)     #  Gift                      #
######################################################
#  Less than 25         #  eSticker                  #
#  25 <= distance < 50  #  $5 Cold Storage eVoucher  #
#  50 <= distance < 75  #  $10 Starbuck eVoucher     #
#  More than 75         #  $20 Subway eVoucher       #
######################################################


#Write a Python program to check and display the gift that customer will recieve.

#The program is to prompt user for the total distance he had travelled (by walking
#or running) in a week and check which gift he will get and display the information
#to him.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - distance
#   - gift

#START CODING FROM HERE
#======================


#Check gifts to be given to customer
def check_gift(distance):

    if distance < 25:  #Check gift and value to be given
        gift = ("eSticker", 0)
    elif 25 <= distance < 50:
        gift = ("$5 Cold Storage eVoucher", 5)
    elif 50 <= distance < 75:
        gift = ("$10 Starbucks eVoucher", 10)
    else:
        gift = ("$20 Subway eVoucher", 20)

    print("You will be awarded a {}!".format(gift[0])) #Modify to display gift to be given
    return gift[1]    #Modify to return the value of gift


#Prompt user for the total distances travelled (either by walking or running).
distance = 76
    
#Do not remove the next line
gift = check_gift(distance)

print(gift)  #Modify to print value received

#Input: 10  output: 0
#Input: 76  output: 20
