from pip._vendor import requests
import json

def print_task_list(taskList):
    for item in taskList:
        task = item['Task']
        dueDate = item['Due']
        print(f'{task:<15} \t {dueDate}')
    print()

def sort_list(taskList):
    taskList.sort(key = lambda x:x['Due'])

def get_message(date):
    url = f"http://localhost:8080/due/{date}"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['message']
