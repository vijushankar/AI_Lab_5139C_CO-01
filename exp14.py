"""
EXP 14
Dictionary - 2
CO1
M1.05
Implement programs using Dictionary Manipulations
Problem : To Create a dictionary of student names and their corresponding grades.

GPCV
"""

# Create a dictionary of student names and their corresponding grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

# Print the grades of all students
for student, grade in student_grades.items():
    print(student, ":", grade)

# Add a new student and their grade
student_grades["Frank"] = 80

# Update the grade of an existing student
student_grades["Bob"] = 95

# Remove a student from the dictionary
del student_grades["Eve"]

# Calculate the average grade of all students
total_grades = sum(student_grades.values())
average_grade = total_grades / len(student_grades)

print("Average grade:", average_grade)




