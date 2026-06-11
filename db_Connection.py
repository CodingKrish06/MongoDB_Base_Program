from pymongo import MongoClient

def connect():
    try:
        client = MongoClient('mongodb://localhost:27017')
        db = client['employee_management']
        employees = db['employees']
        print("Connection established successfully.")
        return employees
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
connect()