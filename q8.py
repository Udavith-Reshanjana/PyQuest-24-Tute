# Given dictionary of student grades
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 88, 'Evan': 95}

# Step 1: Find the student with the highest grade
highest_grade_student = max(grades, key=grades.get)  # Finds the key (student) with the maximum value
highest_grade = grades[highest_grade_student]        # Retrieves the highest grade

# Step 2: Calculate the average grade
average_grade = sum(grades.values()) / len(grades)  # Sums up all grades and divides by the total number of students

# Step 3: List all students who scored above 80
students_above_80 = [student for student, grade in grades.items() if grade > 80]  # Filters students with grades above 80

# Display Results
print(f"Student with the highest grade: {highest_grade_student} ({highest_grade})")
print(f"Average grade: {average_grade:.2f}")  # Formats the average grade to 2 decimal places
print(f"Students who scored above 80: {students_above_80}")
