from db_Connection import connect

def add_department(departments):
    dept_id = int(input("Enter the department ID: "))
    dept_name = input("Enter department name: ")
    
    department = {
        "_id": dept_id,
        "Name": dept_name
    }
    
    departments.insert_one(department)
    print("Department added successfully!")

def view_departments(departments):
    print("Departments:")
    for dept in departments.find():
        print("ID:", dept.get('_id'))
        print("Name:", dept.get('Name'))
        print("-" * 20)

conn = connect()
if conn is not None:
    add_department(conn)
    view_departments(conn)
else:   
    print("Execution halted due to database connection issues.")