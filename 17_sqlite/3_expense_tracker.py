import sqlite3
from datetime import datetime

#------------Create Connection----------------
conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

#-----------Table ----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT,
    date TEXT NOT NULL,
    is_active INTEGER DEFAULT 1
)
""")

conn.commit()

#------------Helper Functions --------

def get_float_input(message):
    try:
        value = float(input(message))
        if value <= 0:
            print("❌ Amount must be greater than 0")
            return None
        return value
    except ValueError:
        print("❌ Invalid number")
        return None
    
def get_date_input(message):
    date_str = input(message)
    try:
        entered_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        if  entered_date > today:
            print("❌ Date cannot be in the future")
            return None

        return date_str

    except ValueError:
        print("❌ Date must be in YYYY-MM-DD format")
        return None
    

#------------CRUD Functions -----------

def add_expense():
    amount = get_float_input("Enter amount: ")
    if amount is None:
        return
    
    category = input("Emyer category (Food/Travel/etc): ").strip()
    if not category:
        print("❌ Category cannot be empty")
        return
    

    note = input("Enter note (optional): ").strip()

    date = get_date_input("Enter date (YYYY-MM-DD): ")
    if date is None:
        return

    cursor.execute("""
        INSERT INTO expenses (amount, category, note, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, note, date))

    conn.commit()

def view_expenses():
    cursor.execute("""
        SELECT id, amount, category, note, date
        FROM expenses
        WHERE is_active = 1
        ORDER BY date DESC
    """)

    rows = cursor.fetchall()
    if not rows:
        print("⚠ No expenses found")
        return

    print("\n--- Expenses ---")
    for row in rows:
        print(row)

def delete_expense():
    try:
        expense_id = int(input("Enter the expense ID to delete: "))
    except ValueError:
        print("❌ Invalid ID")
        return
    
    cursor.execute(
        "SELECT id FROM expenses WHERE id = ? AND is_active = 1",
        (expense_id,)
    )

    if cursor.fetchone() is None:
        print("❌ Expense not found")
        return

    cursor.execute(
        "UPDATE expenses SET is_active = 0 WHERE id = ?",
        (expense_id,)
    )
    conn.commit()
    print("✅ Expense deleted (soft delete)")

def search_by_category():
    category = input("enter the category: ").strip()

    if not category:
        print("Category cannot be empty")
        return
    
    cursor.execute("""
        SELECT id, amount, note, date
        FROM expenses
        WHERE category = ? AND is_active = 1
        ORDER BY date DESC
    """, (category,))

    rows = cursor.fetchall()

    if not rows:
        print("⚠ No expenses found for this category")
        return

    print(f"\n--- Expenses in category: {category} ---")
    for row in rows:
        print(row)


def search_by_note():
    keyword = input("Enter keyword to search in note: ").strip()

    if not keyword:
        print("❌ Keyword cannot be empty")
        return

    cursor.execute("""
        SELECT id, amount, category, date
        FROM expenses
        WHERE note LIKE ? AND is_active = 1
        ORDER BY date DESC
    """, ('%' + keyword + '%',))  # tea -> I like tea , good tea , tea was good, it was a great tea I liked it

    rows = cursor.fetchall()

    if not rows:
        print("⚠ No expenses found matching the note")
        return

    print(f"\n--- Expenses matching note: '{keyword}' ---")
    for row in rows:
        print(row)

def total_spending():
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE is_active = 1
    """)

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"💰 Total Spending: {total}")

def spending_by_category():
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        WHERE is_active = 1
        GROUP BY category
    """)

    rows = cursor.fetchall()

    if not rows:
        print("⚠ No expenses found")
        return

    print("\n--- Spending by Category ---")
    for category, total in rows:
        print(f"{category} : {total}")


# ---------------- MENU ----------------
while True:
    print("""
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search by Category
5. Search by Note
6. Total Spending
7. Spending by Category
8. Exit
""")

    choice = input("Choose option: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        search_by_category()
    elif choice == "5":
        search_by_note()
    elif choice == "6":
        total_spending()
    elif choice == "7":
        spending_by_category()
    elif choice == "8":
        print("Goodbye 👋")
        break
    else:
        print("❌ Invalid choice")