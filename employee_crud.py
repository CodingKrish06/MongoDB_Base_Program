from db_Connection import connect

# Add Employee
def add_employee(employees):
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    emp_email = input("Enter Employee Email: ")
    emp_phno = input("Enter Employee Phone Number: ")
    department = input("Enter Department Name: ")

    employee = {
        "_id": emp_id,
        "Name": emp_name,
        "email": emp_email,
        "phno": emp_phno,
        "department": department
    }

    employees.insert_one(employee)
    print("Employee Added Successfully!")


# View Employees
def view_employees(employees):
    data = list(employees.find())

    if len(data) == 0:
        print("No Employees Found")
        return

    print("\n===== EMPLOYEE RECORDS =====")

    for emp in data:
        print("ID:", emp["_id"])
        print("Name:", emp["Name"])
        print("Email:", emp["email"])
        print("Phone:", emp["phno"])
        print("Department:", emp["department"])
        print("-" * 30)


# Search Employee
def search_employee(employees):
    emp_id = int(input("Enter Employee ID to Search: "))

    employee = employees.find_one({"_id": emp_id})

    if employee:
        print("\nEmployee Found")
        print("ID:", employee["_id"])
        print("Name:", employee["Name"])
        print("Email:", employee["email"])
        print("Phone:", employee["phno"])
        print("Department:", employee["department"])
    else:
        print("Employee Not Found")


# Update Employee
def update_employee(employees):
    emp_id = int(input("Enter Employee ID: "))

    employee = employees.find_one({"_id": emp_id})

    if employee is None:
        print("Employee Not Found")
        return

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    phno = input("Enter New Phone Number: ")
    department = input("Enter New Department: ")

    employees.update_one(
        {"_id": emp_id},
        {
            "$set": {
                "Name": name,
                "email": email,
                "phno": phno,
                "department": department
            }
        }
    )

    print("Employee Updated Successfully!")


# Delete Employee
def delete_employee(employees):
    emp_id = int(input("Enter Employee ID to Delete: "))

    result = employees.delete_one({"_id": emp_id})

    if result.deleted_count > 0:
        print("Employee Deleted Successfully!")
    else:
        print("Employee Not Found")


# Test Menu
if __name__ == "__main__":
    employees = connect()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_employee(employees)

        elif choice == "2":
            view_employees(employees)

        elif choice == "3":
            search_employee(employees)

        elif choice == "4":
            update_employee(employees)

        elif choice == "5":
            delete_employee(employees)

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")