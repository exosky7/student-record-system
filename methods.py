import os
import pandas as pd

default_headers = ["id", "name", "age", "grade", "email", "address"]

def load_data(path):
    # if path doesn't exist, return empty dataframe
    if os.path.exists(path) == False:
        return pd.DataFrame(columns=default_headers)
    try:
        data = pd.read_json(path, orient="records")
        # make sure that dataframe always has all the default headers
        for c in default_headers:
            if c not in data.columns:
                data[c] = pd.NA
        data = data[default_headers]
        return data
    except ValueError:
        # if the file is invalid
        return pd.DataFrame(columns=default_headers)
    
def save_data(data, path):
    data.to_json(path, orient="records", indent=2, force_ascii=False)
    print(path)

def create_new_rec(data):
    if data.empty:
        return 1
    try:
        return int(data["id"].max()) + 1
    except Exception:
        return 1
    
def add_studentRec(data, name, age=None, grade=None, email=None, address=None):
    studentID = create_new_rec(data)
    new_student = {"id": studentID, "name": name, "age": age, "grade": grade, "email": email, "address": address}
    data = pd.concat([data, pd.DataFrame([new_student])], ignore_index=True)
    return data

def update_student_rec(data, student_id, **fields):
    thingy = data["id"] == student_id
    if thingy.any() == False:
        raise KeyError(f"Student id {student_id} not found")
    for k, v in fields.items():
        if k in data.columns:
            data.loc[thingy, k] = v
    return data

def delete_student_rec(data, student_id):
    if (data["id"] == student_id).any() == False:
        raise KeyError(f"Student id {student_id} not found")
    return data[data["id"] != student_id].reset_index(drop=True)

def print_students(data):
    if data.empty:
        print("No records found.")
    else:
        print(data.to_string(index=False))

