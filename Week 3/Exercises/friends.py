# Written by: Hu Bowen
# Date: 3 May 2023
# Class: CSF02

# Initialise friends list
friends = ["Izzat", "Bryan", "Dalton", "Ethan", "Isaac"]

# Get new friend from user
new_friend = input("What is the name of your new friend? ")
friends.append(new_friend)

print("My friends are: {}".format(friends))

# Prompt user to input existing name
friendzoned = input("Who do you want to friendzone? ")
while friendzoned not in friends:
    print("Friend not found!")
    friendzoned = input("Who do you want to friendzone? ")

# Show the index of the name in the list
friend_index = friends.index(friendzoned)
print("{} was in position {}. He will be friendzoned.".format(friendzoned, friend_index))

# Remove the name from friends
del friends[friend_index]

# Print out new friends list
print("My eligible friends are now: {}".format(friends))
