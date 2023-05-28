# Hu Bowen (S10255800) - CSF02

# Function to predict shirt size
def predict_size(bmi: float) -> str:
    if bmi <= 18.0:
        return "S"
    elif bmi <= 21.0:
        return "M"
    else:
        return "L"

# Function to calculate BMR to 2d.p. based on gender
def calculate_bmr(gender: str, weight: float, height: float, age: int) -> float:
    if gender == 'M':
        bmr = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    return round(bmr, 2)

# Variables
name_list = ["Sharon", "Mic", "Josh", "Hannah", "Hanzel"]
height_list = [172, 166, 187, 200, 166]
weight_list = [59.5, 65.6, 49.8, 64.2, 47.5]
size_list = ['M', 'L', 'S', 'M', 'S']

# Calculate BMI for each student
bmi_list = list(map(lambda w, h: round(w / (h / 100) ** 2, 2) , weight_list, height_list))
predicted_bmi= list(map(predict_size, bmi_list))

""" Part(a) """
# Print table using the 5 lists
##data_list = zip(name_list, weight_list, height_list, bmi_list, size_list)
##print("{:10} {:10} {:10} {:10} {:10}".format("Name", "Weight", "Height", "BMI", "Size"))
##for data in data_list:
##    print("{:<10} {:<10.2f} {:<10} {:<10.2f} {:<10}".format(*data))

""" Part(b) """
# Print data
##data_list = zip(name_list, bmi_list, size_list, predicted_bmi)
##print("{:10} {:10} {:10} {:10}".format("Name", "BMI", "Size", "Predicted"))
##for data in data_list:
##    print("{:<10} {:<10.2f} {:<10} {:<10}".format(*data))

# Calculate accuracy rate
##predicted_right = [1 if size == predicted else 0 for size, predicted in zip(size_list, predicted_bmi)]
##accuracy_rate = sum(predicted_right)/ len(predicted_right)
##print("Accuracy rate is {:.2f}".format(accuracy_rate * 100))

""" Part(c) """
details_list = [['Sharon', 'F', 33], ['Mic', 'M', 24], \
               ['Josh', 'M', 25], ['Hannah', 'F', 30], \
               ['Hanzel', 'M', 26]]

# Parse gender and age from list
gender_list = [gender for _, gender, _ in details_list]
age_list = [age for _, _, age in details_list]

# Calculate BMR
bmr_list = list(map(calculate_bmr, gender_list, weight_list, height_list, age_list))

# Print out details
data_list = zip(name_list, weight_list, height_list, bmi_list, gender_list, age_list, bmr_list)
print("{:10} {:10} {:10} {:10} {:10} {:10} {:10}".format("Name", "Weight", "Height", "BMI", "Gender", "Age", "BMR"))
for data in data_list:
    print("{:<10} {:<10.2f} {:<10} {:<10} {:<10} {:<10} {:<10.2f}".format(*data))

