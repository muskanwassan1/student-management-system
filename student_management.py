"""
Student Management System - Python CRUD Project
Developer: Muhammad Nabeel | BSSE - Indus University
"""

import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_data(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_data()
    print("\n--- Add New Student ---")
    sid = input("Student ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    gpa = input("GPA: ")
    students.append({"id": sid, "name": name, "department": dept, "gpa": gpa})
    save_data(students)
    print(f"Student {name} added!")

def view_students():
    students = load_data()
    if not students:
        print("No records found!")
        return
    print("\n--- All Students ---")
    print(f"{'ID':<10} {'Name':<15} {'Dept':<10} {'GPA'}")
    print("-"*40)
    for s in students:
        print(f"{s['id']:<10} {s['name']:<15} {s['department']:<10} {s['gpa']}")

def search_student():
    students = load_data()
    sid = input("\nEnter ID to search: ")
    for s in students:
        if s['id'] == sid:
            print(f"Found: {s}")
            return
    print("Not found!")

def delete_student():
    students = load_data()
    sid = input("\nEnter ID to delete: ")
    new_list = [s for s in students if s['id'] != sid]
    if len(new_list) == len(students):
        print("ID not found!")
    else:
        save_data(new_list)
        print("Deleted!")

def update_student():
    students = load_data()
    sid = input("\nEnter ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input(f"New Name ({s['name']}): ") or s['name']
            s['gpa'] = input(f"New GPA ({s['gpa']}): ") or s['gpa']
            save_data(students)
            print("Updated!")
            return
    print("Not found!")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student\n2. View All\n3. Search\n4. Update\n5. Delete\n6. Exit")
        ch = input("Choose: ")
        if ch == '1': add_student()
        elif ch == '2': view_students()
        elif ch == '3': search_student()
        elif ch == '4': update_student()
        elif ch == '5': delete_student()
        elif ch == '6': break
        else: print("Invalid!")

if __name__ == "__main__":
    main()
