def add_department(departments):
    try:
        dept_id = int(input("Enter Department ID: "))
        dept_name = input("Enter Department Name: ")
        location = input("Enter Department Location: ")

        existing = departments.find_one({"_id": dept_id})

        if existing:
            print("Department ID already exists!")
            return

        department = {
            "_id": dept_id,
            "department_name": dept_name,
            "location": location
        }

        departments.insert_one(department)
        print("Department Added Successfully")

    except ValueError:
        print("Department ID must be a number!")

    except Exception as e:
        print("Error:", e)


def view_departments(departments):
    data = list(departments.find())

    if len(data) == 0:
        print("No Departments Found")
        return

    print("\nDepartment Records")
    print("-" * 50)

    for dept in data:
        print("Department ID:", dept["_id"])
        print("Department Name:", dept["department_name"])
        print("Location:", dept["location"])
        print("-" * 50)


def search_department(departments):
    try:
        dept_id = int(input("Enter Department ID to Search: "))

        dept = departments.find_one({"_id": dept_id})

        if dept:
            print("\nDepartment Found")
            print("Department ID:", dept["_id"])
            print("Department Name:", dept["department_name"])
            print("Location:", dept["location"])
        else:
            print("Department Not Found")

    except ValueError:
        print("Department ID must be a number!")


def update_department(departments):
    try:
        dept_id = int(input("Enter Department ID to Update: "))

        dept = departments.find_one({"_id": dept_id})

        if dept is None:
            print("Department Not Found")
            return

        dept_name = input("Enter New Department Name: ")
        location = input("Enter New Location: ")

        result = departments.update_one(
            {"_id": dept_id},
            {
                "$set": {
                    "department_name": dept_name,
                    "location": location
                }
            }
        )

        if result.modified_count > 0:
            print("Department Updated Successfully")
        else:
            print("No Changes Made")

    except ValueError:
        print("Department ID must be a number!")


def delete_department(departments):
    try:
        dept_id = int(input("Enter Department ID to Delete: "))

        result = departments.delete_one({"_id": dept_id})

        if result.deleted_count > 0:
            print("Department Deleted Successfully")
        else:
            print("Department Not Found")

    except ValueError:
        print("Department ID must be a number!")