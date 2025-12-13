# Creating a dictionary of 5 students with their marks
students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Ayesha": 95,
    "Bilal": 88
}

# Find the student with highest marks
highest_student = max(students, key=students.get)

# Calculate average marks
total_marks = sum(students.values())
average_marks = total_marks / len(students)

# Print results
print("Student with highest marks:", highest_student)
print("Average marks of all students:", average_marks)
