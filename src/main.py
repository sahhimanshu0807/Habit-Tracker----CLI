# This application adds, removes, marks as completed, and delete daily habits as requested by the user. 
# It shows what percentage of the days those habits where followed in the current month as well as in the current year.

from datetime import datetime
import json

import os

def clear():
    _ = os.system('cls' if os.name == 'nt' else 'clear')

# Call it whenever you need
clear()

USERS_FILE = "src/data/users.json"
HABITS_FILE = "src/data/habits.json"

# Creating a class for the user.
class User:
    def __init__(self, username, password, name, email):
        self.username = username.strip()
        self.password = password
        self.name = name
        self.email = email

    def check_input(self):
        if(len(self.username) < 6):
            print("Username is not valid!")
            return False
        if(len(self.password) < 6):
            print("Password is invalid!")
            return False
        if(len(self.name) < 2):
            print("Name is invalid!")
            return False
        if(len(self.email) < 4 or '@' not in self.email or '.com' not in self.email):
            print("Email is invalid!")
            return False
        return True

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def load_json_file(file_path):
    """Safely loads a JSON file or returns an empty list if it doesn't exist."""
    if(os.path.exists(file_path)):
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: {file_path} was corrupted. Starting fresh.")
            return []
        return []
    
def save_json_file(file_path, data):
    """Saves a Python data structure directly to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        return True
    return False

def create_account():
    username = input("Please enter your username! (At least 6 digits) ")
    password = input("Please enter your password! (At least 6 digits) ")
    name = input("Please enter your name! (ex. John Doe) ")
    email = input("Please enter your email! (ex. johndoe@gmail.com) ")

    newUser = User(username, password, name, email)
    if(newUser.check_input()):
        if(store_new_account(newUser)):
            print("Your account has been created. Please sign in!")
        else:
            print("Data storage issue")
        input()
    else:
        print("Please try again with the updated information!")
        input()

def store_new_account(newUser):
    users = load_json_file(USERS_FILE)
    users.append({
        "username": newUser.username,
        "password": newUser.password,
        "name": newUser.name,
        "email": newUser.email
    })
    if(save_json_file(USERS_FILE, users)):
        return True
    else:
        return False
    pass

program_running = True
        
while(program_running == True):
    print(f"Welcome to the habit tracker!")
    print(f"Please select one of the options below!")
    print(f"1. Login.")
    print(f"2. Create a new user.")
    print(f"3. Exit.")
    option1 = int(input("Enter your choice(1-3) "))
    if(option1 == 1):
        pass
    elif(option1 == 2):
        create_account()
        pass
    elif(option1 == 3):
        program_running = False
        pass
    else:
        print(f"Invalid option. Please try again!")
        pass


