import psycopg2

# Connect to DB
conn = psycopg2.connect(
    host="localhost",
    database="nobroker_db",
    user="8484",         # <-- your actual PostgreSQL username
    password="8484" # <-- your actual PostgreSQL password
)
cur = conn.cursor()

# Search employee in DB
def get_employee(employee_id):
    cur.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
    return cur.fetchone()

# Add employee to DB
def add_employee(employee_id):
    name = input("Enter name: ")
    role = input("Enter role: ")
    sal = int(input("Enter salary: "))
    phon = input("Enter phone number: ")

    cur.execute(
        "INSERT INTO employees (employee_id, name, role, sal, phon) VALUES (%s, %s, %s, %s, %s)",
        (employee_id, name, role, sal, phon)
    )
    conn.commit()
    print("✅ New employee added to the database!")

# Main logic
employee_id = input("Enter employee ID: ").strip()

employee = get_employee(employee_id)

if employee:
    print(f"""
👤 Employee Found:
ID    : {employee[0]}
Name  : {employee[1]}
Role  : {employee[2]}
Salary: ₹{employee[3]}
Phone : {employee[4]}
""")
else:
    print("❌ Employee not found.")
    add = input("Do you want to add this employee? (yes/no): ").lower()
    if add == "yes":
        add_employee(employee_id)

# Close connection
cur.close()
conn.close()
