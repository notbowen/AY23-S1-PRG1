#Programming I

#######################################
#             Mission 4.1             #
#    New payment amount for seniors   #
#######################################

#Background
#==========
#To support the government initiative to help seniors with their living expenses,
#all supermarkets in Singapore will give a 5% discount for seniors who are aged 60
#and above.
#
#Write a Python program to check whether a person is eligible for discount
#and if he is, calculate the new amount he has to pay.
#
#The program is to prompt user for his age and amount to pay.
#Check his eligibility for discount and calculate the new amount to pay if
#he is eligible for discount. Display the original and new amounts to pay.
#If he is not eligible for discount, print a message to indicate so.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - age
#   - amount
#   - new_amount


#START CODING FROM HERE
#======================


#Calculate new_payment
def cal_new_payment(age, amount):

    if age >= 60:  #Check if user is eligible for discount
        new_amount = round(amount * 0.95, 2) #Calculate new payment amount, round up to integer
        print("Original Payment Amount: ${:.2f}".format(amount)) #Modify to display original payment amount
        print("New Payment Amount: ${:.2f}".format(new_amount)) #Modify to display new payment amount
        return new_amount #Do not remove this line that returns the new amount
    else:
        print("You are not entitled for the discount") #Modify to display message indicating not entitled to discount
        return amount #Do not remove this line that returns the amount


#Prompt and accept data from user
age = 50
amount = 200
    
#Do not remove the next line that calls the function
amount = cal_new_payment(age, amount)
print("The amount you have to pay is: ${}".format(amount)) #Modify to display the amount obtained from function call

#input 65,120 output 114
#input 70,200 output 190
#input 50,200 output 200
