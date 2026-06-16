from db_Connection import connect
from employee_crud import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee
)


def main():
    employees = connect()

    if employees is None:
        print("Database Connection Failed!")
        return

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
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()