import json
import os
import pandas as pd
from sys import exit
from methods import load_data, save_data, add_studentRec, update_student_rec, delete_student_rec, print_students

save_file = "C:\\vit py\\vityarthi project\\savedata.json"
    

def main():
    data = load_data(save_file)
    menu = "\nStudent Management\n1) List all\n2) Add student\n3) Update student\n4) Delete student\n5) Save and exit\n6) Exit without saving\nEnter an option :D\n "

    while True:
        userInp = input(menu)

        if userInp == "1":
            print_students(data)
        elif userInp == "2":
            name = input("Enter name: ").strip()
            age = input("Enter age (optional): ").strip() or None
            grade = input("Enter grade (optional): ").strip() or None
            email = input("Enter email (optional): ").strip() or None
            address = input("Enter address (optional): ").strip() or None
            data = add_studentRec(data, name, age, grade, email, address)
            print("Student added :D")
        elif userInp == "3":
            studentID = input("Enter student ID to update: ").strip()
            if studentID.isdigit() == False:
                print("Invalid Input")
                continue
            studentID = int(studentID)
            fields = {}
            for field in ["name", "age", "grade", "email", "address"]:
                val = input(f"Enter new {field} (leave blank to skip): ").strip()
                if val != "":
                    fields[field] = val
            try:
                data = update_student_rec(data, studentID, **fields)
                print("Student updated :D")
            except KeyError as p:
                print(p)
            
        elif userInp == "4":
            studentID = input("Enter student ID to delete: ").strip()
            if studentID.isdigit() == False:
                print("Invalid Input")
                continue
            studentID = int(studentID)
            try:
                data = delete_student_rec(data, studentID)
                print("Student deleted :D")
            except KeyError as q:
                print(q)

        elif userInp == "5":
            save_data(data, save_file)
            print("Data saved :D")
            exit()

        elif userInp == "6":
            print("Exiting without saving :D")
            exit()

        else:
            print("Invalid option, try again :(")

main()