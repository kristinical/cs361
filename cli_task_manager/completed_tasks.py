from datetime import date
from main_functions import *

def complete_task_header():
    system('clear')
    print("COMPLETE A TASK\n".center(40))


def complete_task():
    if no_tasks(): return
    complete_task_header()
    list_valid_tasks()
    complete_index = validate_task("What task have you completed? ")
    confirm = confirm_completion(complete_index[0])
    system('clear')
    if confirm == "y":
        save_completed_task(to_do_list[complete_index[1]])
        del to_do_list[complete_index[1]]
        print("TASK MARKED AS COMLETE!\n".center(40))
    elif confirm == "n":
        print("TASK COMPLETION ACTION CANCELLED\n".center(40))


def confirm_completion(task):
    complete = input(f'Are you sure you want to mark "{task}" as complete? (y/n) ')
    while complete != "y" and complete != "n":
        print("\nPlease press 'y' for yes or 'n' for no.")
        complete = input(f'Are you sure you want to mark "{task}" as complete? ')
    return complete


def save_completed_task(task):
    name = task['Task']
    due_date = task['Due']
    today = date.today()
    completed_date = today.strftime('%m-%d-%Y')
    completed_tasks.append({'Task':name, 'Due':due_date, 'Complete':completed_date})


def view_completed_tasks():
    system('clear')
    print("COMPLETED TASKS:\n".center(40))
    if len(completed_tasks) == 0:
        print(no_completed_tasks.center(40))
        print('\n')
    else:
        sort_completed_list()
        print_completed_list()


def sort_completed_list():
    """ 
    Sorts the completed_task list in reverse chronological order
    (most recently completed task is shown first)
    """
    completed_tasks.sort(reverse=True, key = lambda x: datetime.datetime.strptime(x['Complete'], '%m-%d-%Y'))


def print_completed_list():
    for item in completed_tasks:
        task = item['Task']
        completed_date = item['Complete']
        print(f'{task:>12} –– Completed {completed_date:<20}'.center(40))
    print('\n')
