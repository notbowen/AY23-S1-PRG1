# Hu Bowen (S10255800) - CSF02
# Program to generate email address based on ID
# Different email is generated based on staff or student

# Input: Get ID from user
user_id = input("Enter an ID: ").lower()

# Process: Check if user is a student or staff,
#          and assign email accordingly

if user_id.startswith("s") and "-" not in user_id:
    # User is a student
    email_ending = "@abc.edu.sg"
else:
    # User is a staff
    dept, user_id = user_id.split('-')
    email_ending = "@{}.abc.edu.sg".format(dept)

email_address = user_id + email_ending
email_address = email_address.lower()  # Just in case it's not lowered

# Output: Display final email address
print("\nEmail Address: {}".format(email_address))
