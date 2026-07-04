import csv
import os

FILE_NAME = "employees.csv"

# Create CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "EmployeeID",
                "Name",
                "Department",
                "Designation",
                "Email",
                "Status"
            ])

# Add employee
def add_employee(emp_id, name, department, designation, email, status):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            emp_id,
            name,
            department,
            designation,
            email,
            status
        ])
    print("Employee added successfully.")

# Display all employees
def display_employees():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Search employee
def search_employee(emp_id):
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["EmployeeID"] == emp_id:
                print("\nEmployee Found")
                print(row)
                return
    print("Employee not found.")

# Update employee status
def update_status(emp_id, new_status):
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["EmployeeID"] == emp_id:
                row["Status"] = new_status
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Status updated successfully.")

# Delete employee
def delete_employee(emp_id):
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["EmployeeID"] != emp_id:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Employee deleted successfully.")

# Example usage
initialize_file()

add_employee(
    "EMP101",
    "John Smith",
    "IT",
    "Software Engineer",
    "john@example.com",
    "Onboarding"
)

display_employees()

search_employee("EMP101")

update_status("EMP101", "Active")

display_employees()

delete_employee("EMP101")

display_employees()