import datetime
from os import system
from file_functions import to_do_list


def add_task():
    system('clear')
    print("ADD A TASK\n".center(40))
    name = get_task_name("New task name (or enter -1 to cancel): ")
    if name == "-1":
        system('clear')
        print("CREATE TASK CANCELLED\n".center(40))
        return
    due_date = get_due_date()
    to_do_list.append({'Task':name, 'Due':due_date})
    system('clear')
    print("TASK ADDED!\n".center(40))


def get_task_name(prompt):
    name = input(prompt)
    while not valid_name(name) or name == "":
        if name == "":
            print("\nName cannot be blank")
        else:
            print("\nTask name already exists.")
        name = input(prompt)
    return name.capitalize()
    
    
def valid_name(new_name):
    for task in to_do_list:
        name = task['Task']
        if new_name == name:
            return False
    return True


def get_due_date():
    date = input("Due date (MM-DD-YYYY): ")
    while not valid_date(date):
        print("\nInvalid format.")
        date = input("Due date (MM-DD-YYYY): ")
    return date


def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%m-%d-%Y")
        return True
    except ValueError:
        return False