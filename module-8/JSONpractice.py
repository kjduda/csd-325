# Kristopher Duda. November 2, 2025. Assignment 8.2: JSON Practice.

""" This program uses the JSON load() function to load a student class list file into Python.
A function loops through the class list and prints each student's data. Output notifies the user
that this is the original class list. Next, an additional student's data (mine) is added to the
class list using append(). The JSON dump() function also appends the new student data to the .json
file itself. Output notifies the user that the .json file was updated."""


import json

class Student:
    def __init__(self, first_name, last_name, student_id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email

    def __str__(self):
        return f"{self.last_name}, {self.first_name} : ID = {self.student_id}, Email = {self.email}"

def load_students(filename):
    """A list of Student objects is loaded from the JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
        students = []
        for item in data:
            student = Student(
                item["F_Name"],
                item["L_Name"],
                item["Student_ID"],
                item["Email"]
            )
            students.append(student)
        return students, data

def display_students(students):
    """Data for each student is printed."""
    for student in students:
        print(student)

def add_student(students, json_data):
    """The lists for both the Python and JSON files are updated with a new student's data."""
    # The new student's (my) data
    new_student = Student("Kristopher", "Duda", 15213, "kduda@my365.bellevue.edu")

    # New student data is added to Python class list
    students.append(new_student)

    # New student data is added to JSON class list
    json_data.append({
        "F_Name": new_student.first_name,
        "L_Name": new_student.last_name,
        "Student_ID": new_student.student_id,
        "Email": new_student.email
    })

    return new_student

def save_students(filename, json_data):
    """JSON file is updated with new student data."""
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)

# Main program

if __name__ == "__main__":
    # Data loaded from JSON file
    students, json_data = load_students('student.json')

    # Display original list
    print()
    print("The Original Student List: ")
    print()
    display_students(students)

    # New student is added
    new_student = add_student(students, json_data)

    # Display updated list
    print()
    print("Updated Student List:")
    print()
    display_students(students)
    print()
    
    # JSON file updates are saved and user is notified
    save_students('student.json', json_data)
    print("The JSON file has been updated.")
