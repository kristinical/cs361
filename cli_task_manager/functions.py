from pip._vendor import requests
import datetime
from prompts import *
import json

def print_task_list(taskList):
    for item in taskList:
        task = item['Task']
        due = item['Due']
        message = item['Msg']
        print(f'{task:>15} –– Due {message:<20}'.center(35))

def sort_list(taskList):
    taskList.sort(key = lambda x: datetime.datetime.strptime(x['Due'], '%m-%d-%Y'))

def add_task():
    print("ADD A TASK:".center(35))
    name = input("Task name: ")
    while not valid_name(name):
        print("Task already exists.")
        name = input("Task name: ")
    due_date = input("Due date (MM-DD-YYYY): ")
    while not valid_date(due_date):
        print("Invalid format. Please enter again.")
        due_date = input("Due date (MM-DD-YYYY): ")
    message = get_message(due_date)
    task = {'Task':name, 'Due':due_date, 'Msg': message}
    task_list = open('tasks.txt', 'a')
    task_list.writelines([json.dumps(task), '\n'])
    task_list.close()
    print("\nTask added!".center(35))

def edit_task():
    pass

def delete_task():
    pass

def view_tasks():
    print("TO DO LIST:".center(35))
    task_list = open('tasks.txt', 'r')
    tasks = task_list.readlines()
    tasksToDO = []
    for task in tasks:
        tasksToDO.append(json.loads(task))
    if len(tasksToDO) == 0:
        print(no_tasks)
    else:
        sort_list(tasksToDO)
        print_task_list(tasksToDO)

def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%m-%d-%Y")
        return True
    except ValueError:
        return False
    
def valid_name(name):
    return True

def get_message(date):
    url = f"http://localhost:8080/due/{date}"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['message']
