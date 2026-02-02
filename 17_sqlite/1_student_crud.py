# 1 - Import sqlite3

import sqlite3

# 2 - Create a connection

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
""")

conn.commit()

## CRUD Functions
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")

    cursor.execute(
        "INSERT INTO students (name, age, email) VALUES (?,?,?)", (name,age,email)
    )
    conn.commit()

    print(f"user added with data: {(name, age, email)}")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n--- Student List ---")
    for student in students:
        print(student)

def update_student():
    student_id = int(input("Please provide student ID to update: "))
    new_email = input("Enter new email: ")

    cursor.execute(
        "UPDATE students SET email = ? WHERE id = ?", (new_email, student_id)
    )

    conn.commit()

    print("Student updated successfully!")

def delete_student():
    student_id = int(input("Please provide student ID to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE id = ?", (student_id,)
    )

    conn.commit()

    print("Student deleted successfully!")
# -------- MENU --------

while True:
    print("""
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("❌ Invalid choice")