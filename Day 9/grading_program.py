
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if student_scores[score] <= 70:
        student_grades[score] = "Fail"
    
    elif student_scores[score] <= 80:
        student_grades[score] = "Acceptable"

    elif student_scores[score] <= 90:
        student_grades[score] = "Exceeds Expectations"

    elif student_scores[score] <= 100:
        student_grades[score] = "Outstanding"


# 🚨 Don't change the code below 👇
print(student_grades)



# The way she did it in the example.
for student in student_scores:
    score = student_scores[student]     # Creates a variable to adjust the values.
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"