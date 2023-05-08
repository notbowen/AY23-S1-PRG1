# Written by: Hu Bowen
# Date: 8 May 2023
# Class: CSF02

# Dict of grades + Optional comments
grades = {
    85: "A+;Excellent!",
    80: "A;Well done.",
    75: "B+;",
    70: "B;",
    65: "C+;",
    60: "C;",
    55: "D+;",
    50: "D;",
    0: "F;See me."
}

# Ask user for their score
score_input = float(input("Enter your score: "))

# Loop through grades dict and print grade + optional comment
for score, grade in grades.items():
    if score_input >= score:
        grade = grade.split(";")
        print("Grade: {}".format(grade[0]))
        print("{}".format(grade[1])) if len(grade) > 1 else print("", end="")
        break
