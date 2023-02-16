from pip._vendor import requests
import json
from tasks import *
from prompts import *
from functions import *

# Display prompt to user
print(welcome_message)

if not tasksToDO:
    print(no_tasks)
else:
    print(tasks.center(35))
    sort_list(tasksToDO)
    print_task_list(tasksToDO)

# View tasks in chronological order


# Mark task as complete


# View completed tasks


# Unmark task as complete (goes back to to-do list)


# Delete task


# Edit task


# Create new task


# Request & receive data from microservice
for task in tasksToDO:
    print(get_message(task['Due']))
