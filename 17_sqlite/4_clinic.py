import sqlite3
from datetime import datetime

# ---------------- DATABASE CONNECTION ----------------
def connect_db():
    return sqlite3.connect("clinic.db")

# ---------------- CREATE TABLES ----------------
def create_tables():
    con = connect_db()
    cur = con.cursor()

    # Patients table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        age INTEGER,
        created_at TEXT
    )
    """)

    # Appointments table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor TEXT,
        appointment_date TEXT,
        status TEXT,
        created_at TEXT,
        FOREIGN KEY(patient_id) REFERENCES Patients(id)
    )
    """)

    con.commit()
    con.close()

# ---------------- VALIDATION ----------------
def valid_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def valid_age(age):
    return age.isdigit() and int(age) > 0

def valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# ---------------- REGISTER PATIENT ----------------
def register_patient():
    name = input("Enter Name: ").strip()
    mobile = input("Enter Mobile: ").strip()
    age = input("Enter Age: ").strip()

    if name == "":
        print("Name cannot be empty")
        return
    if not valid_mobile(mobile):
        print("Mobile must be 10 digits")
        return
    if not valid_age(age):
        print("Age must be greater than 0")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO Patients (name, mobile, age, created_at)
        VALUES (?, ?, ?, ?)
    """, (name, mobile, int(age),
          datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    con.commit()
    con.close()
    print("Patient registered successfully")

# ---------------- BOOK APPOINTMENT ----------------
def book_appointment():
    patient_id = input("Enter Patient ID: ").strip()

    if not patient_id.isdigit():
        print("Invalid Patient ID")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT id FROM Patients WHERE id=?", (patient_id,))
    records = cur.fetchall()
    if not records:
        print("Patient not found")
        con.close()
        return

    doctor = input("Enter Doctor Name: ").strip()
    date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()

    if not valid_date(date):
        print("Invalid date format. Please use YYYY-MM-DD")
        con.close()
        return

    cur.execute("""
        INSERT INTO Appointments
        (patient_id, doctor, appointment_date, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (patient_id, doctor, date, "Pending",
          datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    con.commit()
    con.close()
    print("Appointment booked successfully")

# ---------------- VIEW APPOINTMENTS ----------------
def view_appointments():
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        SELECT A.id, P.name, A.doctor, A.appointment_date, A.status
        FROM Appointments A
        JOIN Patients P ON A.patient_id = P.id
    """)
    rows = cur.fetchall()
    con.close()

    if not rows:
        print("No appointments found")
        return

    print("\n--- Appointments ---")
    for row in rows:
        print(f"ID: {row[0]} | Patient: {row[1]} | Doctor: {row[2]} | Date: {row[3]} | Status: {row[4]}")
    print("-------------------")

# ---------------- UPDATE APPOINTMENT STATUS ----------------
def update_status():
    app_id = input("Enter Appointment ID: ").strip()
    status = input("Enter Status (Pending / Completed): ").strip().capitalize()

    if status not in ["Pending", "Completed"]:
        print("Invalid status")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("UPDATE Appointments SET status=? WHERE id=?", (status, app_id))
    con.commit()
    con.close()
    print("Status updated successfully")

# ---------------- CANCEL APPOINTMENT ----------------
def cancel_appointment():
    app_id = input("Enter Appointment ID to cancel: ").strip()

    if not app_id.isdigit():
        print("Invalid Appointment ID")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM Appointments WHERE id=?", (app_id,))
    con.commit()
    con.close()
    print("Appointment cancelled successfully")

# ---------------- MAIN MENU ----------------
def menu():
    create_tables()

    while True:
        print("\n--- Clinic Appointment Management System ---")
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. Update Appointment Status")
        print("5. Cancel Appointment")
        print("0. Exit")  # Changed to 0 as per instructions

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            book_appointment()
        elif choice == "3":
            view_appointments()
        elif choice == "4":
            update_status()
        elif choice == "5":
            cancel_appointment()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

# ---------------- START PROGRAM ----------------
menu()
