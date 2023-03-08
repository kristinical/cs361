from add_functions import *
from delete_functions import *


def edit_header():
    system('clear')
    print("EDIT A TASK\n".center(40))
    

def edit_task():
    if no_tasks(): return
    edit_header()
    edit_choice = edit_option()
    if edit_choice == "3":
        system('clear')
        print("EDIT ACTION CANCELLED\n".center(40))
    else:
        complete_edit(edit_choice)
        system('clear')
        print("TASK EDITED!\n".center(40))


def edit_option():
    option = input(edit_actions)
    while option < "1" or option > "3":
        edit_header()
        print("Invalid selection\n")
        option = input(edit_actions)
    return option


def complete_edit(choice):
    edit_header()
    list_valid_tasks()
    task_index = validate_task("What task do you want to edit? ")
    if choice == "1":
        edit_name(task_index[1])
    elif choice == "2":
        edit_date(task_index[1])


def edit_name(task_index):
    new_name = get_task_name("Updated task name: ")
    to_do_list[task_index]['Task'] = new_name


def edit_date(task_index):
    print(f"\nCurrent due date: {to_do_list[task_index]['Due']}")
    new_date = get_due_date("Updated due date (MM-DD-YYYY): ")
    to_do_list[task_index]['Due'] = new_date
    to_do_list[task_index]['Msg'] = get_message(new_date)
