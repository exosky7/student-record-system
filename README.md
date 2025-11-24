# Student Management System

A simple CLI-based **Student Management System** built using **Python** and **Pandas**, with JSON-based persistent storage.  
This project allows you to **add**, **update**, **delete**, **view**, and **save** student records using a clean interactive menu.

## Features
- Load & save student data automatically using JSON  
- Add new students with auto-generated IDs  
- Update any student field  
- Delete student records  
- View all students in a clean table  
- Save & exit / Exit without saving  

## How It Works
Student data is stored in a JSON file and loaded into a Pandas DataFrame with columns:

`id, name, age, grade, email, address`

If the JSON file doesn’t exist or is invalid, the program initializes an empty dataset with the required headers.

## Functions Overview
- **load_data(path):** Loads JSON data and ensures all columns exist  
- **save_data(data, path):** Writes DataFrame back to JSON  
- **create_new_rec(data):** Generates next student ID  
- **add_studentRec(...):** Adds a new student record  
- **update_student_rec(...):** Updates existing record fields  
- **delete_student_rec(...):** Deletes a student by ID  
- **print_students(data):** Displays all records  
- **main():** Runs the interactive CLI menu  

## Menu Options
- List all
- Add student
- Update student
- Delete student
- Save and exit
- Exit without saving

## Requirements
- Python 3.x
- pandas

## Installing dependencies
Simply run:
`python -m pip install pandas`

## Running the program
- Download and put all the files into one folder
- open cmd in that folder and run
`python ./main.py`

## Notes
- Handles missing or corrupted JSON gracefully  
- Ensures all default columns exist  
- Clean, beginner-friendly CRUD implementation  
- Uses Pandas for data manipulation and JSON for storage

