# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Function to get grades of student according to their score

def obtain_grade(score: float) -> str:
    if score >= 84.5:
        return "A+"
    elif score >= 79.5:
        return "A"
    elif score >= 74.5:
        return "B+"
    elif score >= 69.5:
        return "B"
    elif score >= 64.5:
        return "C+"
    elif score >= 59.5:
        return "C"
    elif score >= 54.5:
        return "D+"
    elif score >= 49.5:
        return "D"
    else:
        return "F"


# Runner code
mark_list = [['Mary', 90.5], ['Charles', 60.4], [
    'John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

print("{:15} {:10} {:10}".format("Student Name", "mark", "Grade"))
for student, score in mark_list:
    grade = obtain_grade(score)
    print("{:15} {:<10} {:10}".format(student, score, grade))
