from pip._vendor import requests
from file_functions import *
from edit_functions import *


def menu_selection():
    view_tasks()
    print(menu.center(40))
    action = input(actions)
    return action


def view_tasks():
    print("TO DO LIST:\n".center(40))
    if len(to_do_list) == 0:
        print(no_todo_tasks.center(40))
    else:
        sort_todo_list()
        print_task_list()
    print('\n')


def sort_todo_list():
    to_do_list.sort(key = lambda x: datetime.datetime.strptime(x['Due'], '%m-%d-%Y'))
    

def print_task_list():
    for item in to_do_list:
        task = item['Task']
        due = get_message(item['Due'])
        print(f'{task} –– Due {due}'.center(40))


def get_message(date):
    """
    Call to partner's microservice that sends a date and receives a
    message string that tells user when each task is due
    """
    url = f"http://localhost:8080/due/{date}"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['message']
