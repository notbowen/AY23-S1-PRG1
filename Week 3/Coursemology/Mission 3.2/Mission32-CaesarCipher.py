#Programming I

####################################
#           Side Quest 3.2         #
#           Caesar Cipher          #
####################################

#Background
#==========
#The encryption of a plaintext by Caesar Cipher is:
#En(Mi) = (Mi + n) mod 26 

#Write a Python program that prompts user to enter a plaintext
#and displays the encrypted result using Caesar Cipher.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - plaintext
#   - n (to represent number of shifts in int)
#   - ciphertext

#START CODING FROM HERE
#======================


#Function to perform the encryption of given plaintext
def caesarEncrypt(plaintext, n):
    #Code to do the conversion
    ciphertext = ""

    for char in plaintext:
        code = ord(char) - 65
        code = (code + n) % 26
        ciphertext += chr(code + 65)

    return ciphertext #Do not remove this line

# print(caesarEncrypt("HELLOWORLDTHESECRETISOUT", 5))