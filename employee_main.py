from db_Connection import connect
from employee_crud import add_employee, view_employees, search_employee, update_employee, delete_employee


def main():
    conn = connect()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(conn)
        elif choice == '2':
            view_employees(conn)
        elif choice == '3':
            search_employee(conn)
        elif choice == '4':
            update_employee(conn)
        elif choice == '5':
            delete_employee(conn)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")