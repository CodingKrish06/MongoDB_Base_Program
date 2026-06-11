from db_Connection import connect  
def add_employee(employees):
    emp_id = int(input("Enter the employee ID: "))
    emp_name = input("Enter employee name: ")
    emp_email = input("Enter employee email: ")
    emp_phno = input("Enter employee phno: ")
    department = input("Enter department name: ")
    
    employee = {
        "_id": emp_id,
        "Name": emp_name,
        "email": emp_email,
        "phno": emp_phno,
        "department": department
    }

    employees.insert_one(employee)
    print("Employee Added Successfully!")

connect()
add_employee(connect())

def view_employees(employees):
    # Retrieve all documents from the collection
    data = list(employees.find())

    if len(data) == 0:
        print("No employees Found")
        return
        
    print("\nEmployee Records")
    print("-" * 50)

    for emp in data:
        # Using .get() prevents crashes if a document happens to miss a specific key
        print("ID:", emp.get('_id'))
        print("Name:", emp.get('Name'))
        print("Email:", emp.get('email'))
        print("Phone:", emp.get('phno'))
        print("Department:", emp.get('department'))
        print("-" * 48)

# 1. Establish connection (returns the collection)
conn = connect()

# 2. Safety check: Execute only if the connection didn't return None
if conn is not None:
    # Toggle these comment lines to test adding vs viewing
    # add_employee(conn)
    view_employees(conn)
else:
    print("Execution halted due to database connection issues.")


def search_employee(employees):
    emp_id = int(input("Enter the employee ID to search: "))
    employee = employees.find_one({"_id": emp_id})
    if employee:
        print("Employee found:")
        print("ID:", employee.get('_id'))
        print("Name:", employee.get('Name'))
        print("Email:", employee.get('email'))
        print("Phone:", employee.get('phno'))
        print("Department:", employee.get('department'))
    else:
        print("Employee not found.")

conn = connect()
if conn is not None:        
    search_employee(conn)
else:       
    print("Execution halted due to database connection issues.")


def update_employee(employees):
    emp_id = int(input("Enter the employee ID : "))
    employee = employees.find_one({"_id": emp_id})

    if employee is None:
        print("Employee not found.")
        return  
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    phno = input("Enter new phone number: ")
    department = input("Enter new department : ")

    employees.update_one(
            {"_id": emp_id},
            {"$set": {
                "Name": name,
                "email": email,
                "phno": phno,
                "department": department
            }}
        )
print("Employee updated successfully!")


def delete_employee(employees):
    emp_id = int(input("Enter the employee ID to delete: "))
    result = employees.delete_one({"_id": emp_id})

    if result.deleted_count > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")


conn = connect()
if conn is not None:    
    delete_employee(conn)
else:   
    print("Execution halted due to database connection issues.")