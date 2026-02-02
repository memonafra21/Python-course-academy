import sqlite3

# Connect and create table
conn = sqlite3.connect("company.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    salary REAL
)
""")
conn.commit()

# CREATE
def add_employee():
    id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    cur.execute("INSERT INTO employee VALUES (?, ?, ?)", (id, name, salary))
    conn.commit()
    print("Employee added successfully")

# READ
def view_employee():
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    print("\nID  Name  Salary")
    for row in rows:
        print(row)

# UPDATE
def update_employee():
    id = int(input("Enter Employee ID to update: "))
    new_salary = float(input("Enter new salary: "))
    cur.execute("UPDATE employee SET salary = ? WHERE emp_id = ?", (new_salary, id))
    conn.commit()
    print("Employee updated successfully")

# DELETE
def delete_employee():
    id = int(input("Enter Employee ID to delete: "))
    cur.execute("DELETE FROM employee WHERE emp_id = ?", (id,))
    conn.commit()
    print("Employee deleted successfully")

# MENU
while True:
    print("\n--- Employee CRUD Menu ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employee()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Program Ended")
        break
    else:
        print("Invalid choice")

conn.close()