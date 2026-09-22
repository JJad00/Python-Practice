"""Calculate the student's final grade."""

# Define the weights for each category
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Get the scores from the user
midterm_exam_grade = float(input("Please enter midterm grade 0 - 100: "))
final_exam_grade = float(input("Please enter final exam grade 0 - 100: "))
assignment_one = float(input("Please enter first assignment grade 0 - 30: "))
assignment_two = float(input("Please enter second assignment grade 0 - 30: "))
quiz_one = float(input("Please enter first quiz grade 0 - 20: "))
quiz_two = float(input("Please enter second quiz grade 0 - 20: "))

# Validate exam grades
if (0 <= midterm_exam_grade <= 100 and
    0 <= final_exam_grade <= 100):

    exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT

else:
    print("Invalid input. Please enter exams within the 0 - 100 range.")
    exam_grade = 0

# Validate assignment grades
if (0 <= assignment_one <= 30 and
    0 <= assignment_two <= 30):

    assignment_grade = (assignment_one + assignment_two) / 2 / 30 * 100 * ASSIGNMENT_WEIGHT

else:
    print("Invalid input. Please enter assignments within the 0 - 30 range.")
    assignment_grade = 0

# Validate quiz grades
if (0 <= quiz_one <= 20 and
    0 <= quiz_two <= 20):

    quiz_grade = (quiz_one + quiz_two) / 2 / 20 * 100 * QUIZ_WEIGHT

else:
    print("Invalid input. Please enter quizzes within the 0 - 20 range.")
    quiz_grade = 0

# Calculate the final grade
final_grade = exam_grade + assignment_grade + quiz_grade

# Display the final grade
print(f"The student's final grade is {final_grade:.2f}%")