from os import system
from prompts import *
from main_functions import to_do_list


def delete_header():
    system('clear')
    print("DELETE A TASK\n".center(40))
    

def delete_task():
    if no_tasks(): return
    delete_header()
    list_valid_tasks()
    delete_index = validate_task("What task do you want to delete? ")
    confirm = confirm_deletion(delete_index[0])
    system('clear')
    if confirm == "y":
        del to_do_list[delete_index[1]]
        print("TASK DELETED!\n".center(40))
    elif confirm == "n":
        print("DELETE ACTION CANCELLED\n".center(40))


def no_tasks():
    if len(to_do_list) == 0:
        system('clear')
        return True


def validate_task(message):
    name = input(message)
    task_index = valid_task(name.capitalize())
    while task_index == -1:
        delete_header()
        print("Task does not exist.\n")
        list_valid_tasks()
        name = input(message)
        task_index = valid_task(name.capitalize())
    return name.capitalize(), task_index


def valid_task(name):
    for i in range(len(to_do_list)):
        if to_do_list[i]["Task"] == name:
            return i
    return -1


def list_valid_tasks():
    """
    Displays list of current tasks on To-Do List in alphabetical order
    """
    print("Current tasks:")
    to_do_list.sort(key = lambda x: x['Task'])
    for task in to_do_list:
        print("  " + task['Task'])
    print()


def confirm_deletion(task):
    delete = input(f'Are you sure you want to delete "{task}"? (y/n) ')
    while delete != "y" and delete != "n":
        print("\nPlease press 'y' for yes or 'n' for no.")
        delete = input(f'Are you sure you want to delete "{task}"? ')
    return delete
