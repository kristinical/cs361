from pip._vendor import requests
import json
from prompts import *
from functions import *

print(welcome_message)
view_tasks()
print(menu)
action = input(actions)
while action != "5":
    match action:
        case "1":
            add_task()
        case "2":
            edit_task()
        case "3":
            delete_task()
        case "4":
            view_tasks()
        case _:
            print("\nInvalid selection. Please try again:")
            action = input(actions)
    print(menu)
    action = input(actions)

print(goodbye)

# Mark task as complete


# View completed tasks


# Unmark task as complete (goes back to to-do list)


# Delete task


# Edit task


# Create new task


# Request & receive data from microservice
# for task in tasksToDO:
#     print(get_message(task['Due']))
