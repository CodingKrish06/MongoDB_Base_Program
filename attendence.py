from datetime import date
from db_Connection import connect


def mark_attendance(attendance, employees):
    emp_id = int(input("Enter Employee ID: "))

    emp = employees.find_one({"_id": emp_id})

    if emp is None:
        print("Employee Not Found")
        return

    today = str(date.today())

    existing = attendance.find_one({
        "emp_id": emp_id,
        "date": today
    })

    if existing:
        print("Attendance Already Marked")
        return

    status = input("Enter Status (Present/Absent): ")

    attendance.insert_one({
        "_id": f"{emp_id}_{today}",
        "emp_id": emp_id,
        "date": today,
        "status": status
    })

    print("Attendance Marked Successfully")


def view_today_attendance(attendance, employees):
    today = str(date.today())

    data = list(attendance.find({"date": today}))

    if len(data) == 0:
        print("Attendance Not Found")
        return

    print("\nToday's Attendance")
    print("-" * 50)

    for att in data:
        emp = employees.find_one({"_id": att["emp_id"]})

        if emp:
            print("ID:", att["emp_id"])
            print("Name:", emp["name"])
            print("Status:", att["status"])
            print("Date:", att["date"])
            print("-" * 50)


def update_attendance(attendance):
    emp_id = int(input("Enter Employee ID: "))
    att_date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter New Status (Present/Absent): ")

    res = attendance.update_one(
        {
            "emp_id": emp_id,
            "date": att_date
        },
        {
            "$set": {
                "status": status
            }
        }
    )

    if res.modified_count > 0:
        print("Attendance Updated Successfully")
    else:
        print("Record Not Found")


def delete_attendance(attendance):
    emp_id = int(input("Enter Employee ID: "))
    att_date = input("Enter Date (YYYY-MM-DD): ")

    res = attendance.delete_one({
        "emp_id": emp_id,
        "date": att_date
    })

    if res.deleted_count > 0:
        print("Attendance Deleted Successfully")
    else:
        print("Record Not Found")


# Connection
db = connect()

employees = db["Employee"]
attendance = db["Attendance"]

# Test
mark_attendance(attendance, employees)
view_today_attendance(attendance, employees)