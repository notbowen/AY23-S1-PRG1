# Prompt user for input
ct = float(input("Enter your common test marks (out of 100): "))
assessment = float(input("Enter your assessment marks (out of 100): "))
ca = float(input("Enter your continuous assessment marks (out of 100): "))

# Calculate final mark
final = 0.3 * ct + 0.3 * assessment + 0.4 * ca

# Print final mark
print("Your final mark is " + str(final) + " marks.")
