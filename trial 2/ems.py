import psycopg2

DB_NAME = "employee_db"
DB_PASSWORD = "even@gods!"
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT
    )
    print("Connection established")
except Exception as e:
    print("Failed to connect to database")
    print(f"Error: {e}")

cur = conn.cursor()

try: 
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id SERIAL PRIMARY KEY ,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        department VARCHAR(100) NOT NULL
    )
    """)
except Exception as e:
    print("Failed to create table")
    print(f"Error: {e}")
conn.commit()

name  = input("Enter full name: ")
age = int(input("Enter age: "))
department = input("Enter name of department: ")

employee_input = (name,age,department)
insert_query = ("INSERT INTO employees(name,age,department) VALUES (%s, %s, %s)")
try:
    def add_employee():
        cur.execute(insert_query,employee_input)
    add_employee()
    print(f"Employee '{name}' has been added")
    conn.commit()
except Exception as e:
    print(e)

try:
    def view_employee_info():
        cur.execute("SELECT * FROM employees")
        employee_list = cur.fetchall()
        print("List of all employees\n")
        for employee in employee_list:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Age: {employee[2]}, Department: {employee[3]}")
    view_employee_info()
except Exception as e:
    print("Failed to retrieve employee list")
    print(f"Error: {e}")


def update_employee_records():
    pass
    # update_employee_records()



def main():
    print("=== Employee Management System ===\n")
    print("Menu\n1. Add Employee\n2. View Employees\3. Update Employee \4. Delete Employee\5. Exit")
try:
    user_input = input("Enter option(1-5): ")
    if user_input == "1":
        add_employee()
    elif user_input == "2":
        view_employee_info()
    else:
        print("Wrong input! Enter options 1-5")
except ValueError:
    print("Numbers only!")



if __name__ == "__main__":
    main()

cur.close()
conn.close()