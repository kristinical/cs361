from completed_tasks import *

system('clear')
open_task_lists()
print(welcome_message.center(40))
action = menu_selection()

"""
Continuously prompt user to make a menu selection and process
their selected action until they choose to exit (option 6)
"""
while action != "6":
    match action:
        case "1":
            add_task()
        case "2":
            edit_task()
        case "3":
            delete_task()
        case "4":
            complete_task()
        case "5":
            view_completed_tasks()
        case _:
            system('clear')
            print("INVALID SELECTION.\n")
    action = menu_selection()

system('clear')
save_task_lists()
print(goodbye)
