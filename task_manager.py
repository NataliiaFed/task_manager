# =====importing libraries==================================================================
# datetime library to get current date and convert dates from strings into objects and backwards
from datetime import datetime

#====GLOBAL VARIABLES======================================================================
# dictionary-variable to store usernames and corresponding passwords
users = {}

# variables for current date as a string- and as a date-objects (will be needed in several functions)
current_date = datetime.today().strftime('%d %b %Y')
current_date_obj = datetime.now()

#====Functions=============================================================================
# presenting the main menu to a user
def print_main_menu():
    # based on if the user is admin or not, print out the relevant menu
    if username == "admin":
        print('OPTIONS:')
        print('r  - Registering a user')
        print('a  - Adding a task')
        print('va - View all tasks')
        print('vm - View my task')
        print('gr - Generate reports')
        print('ds - Display statistics')
        print('e  - Exit')
    else:
        print('OPTIONS:')
        print('a  - Adding a task')
        print('va - View all tasks')
        print('vm - View my task')
        print('e  - Exit')

# registering a new user
def reg_user():
    # request a username, password and password confirmation from a user,
    # check if the username entered is in users dict, and if password is confirmed,
    # based on the checks add a new pair username:password to users dict and to the user.txt file
    # otherwise display a relevant message and request inputs again
    while True:
        new_username = input("Username: ")
        new_password = input("Password: ")
        new_password2 = input("Confirm password: ")

        if new_username in users:
            print(f"User {new_username} already exists. Try another username.")
            continue

        if new_password == new_password2:
            users[new_username] = new_password
            with open("user.txt", "a+") as f:
                f.write(f"\n{new_username}, {new_password}")
            print(f"User {new_username} has been registered.")
            break
        else:
            print("Passwords do not match.Try again.")

# adding a new task
def add_task():
    # request a username of the person whom the task is going to be assigned to and check if it is in users dict
    # request inputs about the task
    # add the data to the file task.txt, including current date in relevant format and 'No' to indicate if the task is complete
    while True:
        task_username = input("Username: ")
        if task_username in users:
            break
        else:
            print("A user with that username doesn't exist.")

    task_title = input("Title of a task: ")
    task_description = input("Description of the task: ")
    due_date = due_date_input()
    task_complete = "No"

    with open("tasks.txt", "a+") as f:
        f.write(f"\n{task_username}, {task_title}, {task_description}, {current_date}, {due_date}, {task_complete}")

    print(f"New task for user {task_username} has been added.")

# getting due date from a user
def due_date_input():
    # request a due date of a task from a user and convert it into a date-object, and check if it is in the future
    # if error is raised or check failed, print the relevant message and request input again
    while True:
        due_date = input("Due date of the task in 'dd Mon yyyy' format: ")
        try:
            due_date_obj = datetime.strptime(due_date, '%d %b %Y')
        except ValueError:
            print("Invalid date format. Try again.")
        else:
            if due_date_obj >= current_date_obj:
                break
            else:
                print("Due date can't be in the past.")
    return due_date

# printing out all the tasks listed in the task.txt file
def view_all():
    # read the file, iterate through each task, split each task where there is comma and space and store the data in separate variables
    # print out the data in a user-friendly format
    with open("tasks.txt", "r") as f:
        for pos, task in enumerate(f, 1):
            task_split = task.split(", ")

            task_username = task_split[0]
            task_title = task_split[1]
            task_description = task_split[2]
            due_date = task_split[4]
            assign_date = task_split[3]
            task_complete = task_split[5].strip("\n")

            output = f"[ №{pos} ]———————————————————————————————————————————————————————————————\n"
            output += f"Task:             {task_title}\n"
            output += f"Assigned to:      {task_username}\n"
            output += f"Date assigned:    {assign_date}\n"
            output += f"Due date:         {due_date}\n"
            output += f"Task complete?    {task_complete}\n"
            output += f"Task description:\n\t{task_description}"
            print(output)
        print("—————————————————————————————————————————————————————————————————————")

# printing out the tasks listed in the task.txt file and assigned to logged-in user to the console
def view_mine():
    # read the file, iterate through each task, split each task where there is comma and space and store the data in separate variables
    # define if username in the task is the same as username of logged-in user,
    # if yes, print out the data in a user-friendly format
    # store indexes of the tasks assigned to the user in a list and return the list for further usage
    with open("tasks.txt", "r") as f:
        task_indexes = []

        for pos, task in enumerate(f, 1):
            task_split = task.split(", ")

            task_username = task_split[0]
            task_title = task_split[1]
            task_description = task_split[2]
            due_date = task_split[4]
            assign_date = task_split[3]
            task_complete = task_split[5].strip("\n")

            if username == task_username:
                task_indexes.append(pos - 1)

                output = f"[ №{pos} ]———————————————————————————————————————————————————————————————\n"
                output += f"Task:             {task_title}\n"
                output += f"Assigned to:      {task_username}\n"
                output += f"Date assigned:    {assign_date}\n"
                output += f"Due date:         {due_date}\n"
                output += f"Task complete?    {task_complete}\n"
                output += f"Task description:\n\t{task_description}"
                print(output)

        if len(task_indexes) == 0:
            output = "—————————————————————————————————————————————————————————————————————\nYou have no tasks."
            print(output)

        print("—————————————————————————————————————————————————————————————————————")

    return task_indexes

# presenting the edit menu to a user
def print_task_edit_menu():
    print('EDIT OPTIONS:')
    print('1 - Mark the task as complete')
    print('2 - Edit the task')
    print('3 - Back to the previous menu')

# presenting the task edit menu to a user
def print_task_edit_menu2():
    print('TASK EDIT OPTIONS:')
    print('1 - Change username')
    print('2 - Change due date')
    print('3 - Back to the previous menu')

# marking a task as complete
def mark_as_complete():
    # check if the last value in the list with task data is No, then replace is with Yes (take \n into account)
    # join all the value in the list back into a string separated by commas, update this task in the list with all tasks
    # overwrite the tasks.txt file with updated list of tasks

    if edit_task_split[-1] == "No\n" or edit_task_split[-1] == "No":
        if edit_task_split[-1] == "No\n":
            edit_task_split[-1] = "Yes\n"
        elif edit_task_split[-1] == "No": # if this is the last file in the file
            edit_task_split[-1] = "Yes"

        updated_task = ", ".join(edit_task_split)
        tasks[task_choice] = updated_task
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task)
        print(f"Task №{task_choice + 1} has been marked as complete.")

    else:
        print("The task has been already completed.")

# reassigning a task to another user
def change_user():
    # request a username of a person to whom the task needs to be reassigned to and check if the username is in users
    # replace username in the list (index 0) with the new value
    # join all the value in the list back into a string separated by commas, update this task in the list with all tasks
    # overwrite the tasks.txt file with updated list of tasks
    while True:
        new_task_user = input("Enter a user you want to reassign the task to: ")
        if new_task_user in users:
            edit_task_split[0] = new_task_user
            updated_task = ", ".join(edit_task_split)
            tasks[task_choice] = updated_task
            with open("tasks.txt", "w") as f:
                for task in tasks:
                    f.write(task)
            print(f"Task №{task_choice + 1} has been reassigned to user '{new_task_user}'.")
            break
        else:
            print(f"No such user found.")

# changing due date of a task
def change_due_date():
    # call a function for due date input and replace due date in the list with task data (index 4) with the new value
    # join all the value in the list back into a string separated by commas, update this task in the list with all tasks
    # overwrite the tasks.txt file with updated list of tasks
    edit_task_split[4] = due_date_input()
    updated_task = ", ".join(edit_task_split)
    tasks[task_choice] = updated_task
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task)
    print(f"Due date in task №{task_choice + 1} has been changed.")

# generating task report as a text file
def gen_task_report():
    # read the file with tasks, store list with all tasks in a variable
    # store the task user want to edit in a list splited where there is comma and space
    with open("tasks.txt", 'r') as f:
        tasks = f.readlines()

    # store the length of list with all tasks as the total number of all tasks
    tasks_total = len(tasks)

    # declare variables for the total numbers of completed, uncompleted and overdue tasks
    completed_total = 0
    uncompleted_total = 0
    overdue_total = 0

    # iterate through each task, split it,
    # check if it is completed or not, increment by 1 the value of correcponding variable
    # for uncompleted tasks retrieve its due date, convert it into date-object, compare with the current date,
    # and increment by 1 the value of overdue tasks if due date is in the past
    for task in tasks:
        task_split = task.split(", ")
        task_complete = task_split[-1].strip("\n")
        if task_complete == "Yes":
            completed_total += 1
        else:
            uncompleted_total += 1

            due_date = task_split[4]
            due_date_obj = datetime.strptime(due_date, '%d %b %Y')
            if due_date_obj < current_date_obj:
                overdue_total += 1

    # call a relevant function to calculate percentage and store the results in variables
    incomplete_percentage = percentage(uncompleted_total, tasks_total)
    overdue_percentage = percentage(overdue_total, tasks_total)

    # create a variable and store the results of calculations in a user-friendly format
    output = f"TASK OVERVIEW REPORT\n"
    output += f"Generated on: {current_date}\n"
    output += f"--------------------------------------------------\n"
    output += f"Total number of tasks:                       {tasks_total}\n"
    output += f"Total number of completed tasks:             {completed_total}\n"
    output += f"Total number of uncompleted tasks:           {uncompleted_total}\n"
    output += f"Total number of overdue tasks:               {overdue_total}\n"
    output += f"Percentage of tasks that are incomplete:     {incomplete_percentage}%\n"
    output += f"Percentage of tasks that are overdue:        {overdue_percentage}%\n"
    output += f"--------------------------------------------------"

    # create a text-file and write the output into it
    with open("task_overview.txt", 'w') as f:
        f.write(output)

    print("File 'task_overview.txt' has been generated.")

# generating user report as a text file
def gen_user_report():
    # store the length of users dictionary as the total number of all users
    users_total = len(users)

    # read the file with tasks, store list with all tasks in a variable
    # store the task user want to edit in a list splited where there is comma and space
    with open("tasks.txt", 'r') as f:
        tasks = f.readlines()

    # store the length of list with all tasks as the total number of all tasks
    tasks_total = len(tasks)

    # create a variable and store the data in a user-friendly format
    output = f"USER OVERVIEW REPORT\n"
    output += f"Generated on: {current_date}\n"
    output += f"---------------------------------------------------\n"
    output += f"Total number of users:                       {users_total}\n"
    output += f"Total number of tasks:                       {tasks_total}\n"
    output += f"---------------------------------------------------"

    # create a text-file and write the output into it
    with open("user_overview.txt", 'w') as f:
        f.write(output)

    # iterate through each user
    for user in users:

        # declare variables for the total numbers of all tasks, completed tasks, uncompleted tasks and overdue tasks
        user_tasks_total = 0
        user_completed_total = 0
        user_uncompleted_total = 0
        user_overdue_total = 0

        # iterate through each task, split it,
        # check if it is completed or not, increment by 1 the value of correcponding variable
        # for uncompleted tasks retrieve its due date, convert it into date-object, compare with the current date,
        # and increment by 1 the value of overdue tasks if due date is in the past
        for task in tasks:
            task_split = task.split(", ")
            task_user = task_split[0]
            if user == task_user:
                user_tasks_total += 1

                task_complete = task_split[-1].strip("\n")
                if task_complete == "Yes":
                    user_completed_total += 1
                else:
                    user_uncompleted_total += 1

                    due_date = task_split[4]
                    due_date_obj = datetime.strptime(due_date, '%d %b %Y')
                    if due_date_obj < current_date_obj:
                        user_overdue_total += 1

        # call a relevant function to calculate percentage and store the results in variables
        user_total_percentage = percentage(user_tasks_total, tasks_total)
        user_completed_percentage = percentage(user_completed_total, user_tasks_total)
        user_uncompleted_percentage = percentage(user_uncompleted_total, user_tasks_total)
        user_overdue_percentage = percentage(user_overdue_total, user_tasks_total)

        # store the results of calculations in a user-friendly format into 'output' variavle
        output = f"\n[ User: {user} ]\n"
        output += f"Total tasks assigned:                        {user_tasks_total}\n"
        output += f"Percentage of tasks assigned:                {user_total_percentage}%\n"
        output += f"Percentage of completed tasks assigned:      {user_completed_percentage}%\n"
        output += f"Percentage of uncompleted tasks assigned:    {user_uncompleted_percentage}%\n"
        output += f"Percentage of overdue tasks assigned:        {user_overdue_percentage}%\n"
        output += f"---------------------------------------------------"

        # open created earlier text-file and add new output into it
        with open("user_overview.txt", 'a') as f:
            f.write(output)

    print("File 'use_overview.txt' has been generated.")

# calculating a percentage
def percentage(value, total_value):
    # divide the value by the total value and then multiply the resultant by 100
    # if the total value is equal to 0, the percentage should be equal to 0
    # return the rounded value of percentage
    try:
        percentage = value / total_value * 100
    except ZeroDivisionError:
        percentage_short = 0.0
    else:
        percentage_short = round(percentage, 0)
    return percentage_short

# printing out the data from reports to the console
def display_statistics():
    # read the files with reports and print the data from the file out
    # if the files don't exist yet, generate them using the relevant function and then print the data from the file out
    try:
        with open("task_overview.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        gen_task_report()
        with open("task_overview.txt", "r") as f:
            print(f.read())

    try:
        with open("user_overview.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        gen_user_report()
        with open("user_overview.txt", "r") as f:
            print(f.read())

#====Login Section=========================================================================
# read usernames and password from the user.txt file, store them as username:password pairs to the dictionary
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip("\n").split(", ")
        users[username] = password

# request username and password for a user who wants to log in,
# check if the username is in users dict and if password matches this username
# based on the checks, print out the relevant message and request the input again if needed
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and password == users[username]:
        print(f"Welcome, {username}!")
        break
    else:
        print("You've entered invalid username or password. Try again.")

#====Main Section==========+===============================================================
# display the main menu (different for admin and other users)
print_main_menu()
while True:
    # request an option selection from a user, convert the input to lower case
    menu = input("Select an option: ").lower()

    if menu == 'r':
        # registering a new user:
        # check if the username is 'admin', based on check call the reg_user function or display a relevant message
        # then display the main menu to make the next selection
        if username == "admin":
            reg_user()
        else:
            print("Sorry, only the user with the username 'admin' is allowed to register users.")
        print_main_menu()

    elif menu == 'a':
        # add a new task: call a relevant function, and then display the main menu
        add_task()
        print_main_menu()

    elif menu == 'va':
        # printing out all the tasks: call a relevant function, and then display the main menu
        view_all()
        print_main_menu()

    elif menu == 'vm':
        # printing out the tasks assigned to logged-in user to the console:
        # call a relevant function, store in a variable a list of indexes of tasks assigned to the user that the function returns
        user_tasks = view_mine()

        while True:
            # request a number of a task that user wants to edit and check if the number is in the list of indexes
            # request a number again if the user enters a number which is not in the list
            task_choice = int(input("Enter a number of a task to edit or '-1' to exit to the main menu: ")) - 1

            if task_choice in user_tasks:

                # read the file with tasks, store list of all tasks in a variable
                # store the task user want to edit in a list splited where there is comma and space
                with open("tasks.txt", "r") as f:
                    tasks = f.readlines()
                edit_task = tasks[task_choice]
                edit_task_split = edit_task.split(", ")

                # display the edit menu and request a selection of an edit option from a user
                print_task_edit_menu()
                while True:
                    edit_choice = input("Select an option: ")

                    if edit_choice == '1':
                        # marking the task as complete
                        mark_as_complete()
                        print_task_edit_menu()

                    elif edit_choice == '2':

                        # make sure the task is not complete, display the next edit menu and request a selection of an edit option from a user
                        # otherwise display a relevant message and display the edit menu again and repeat the input request
                        task_complete = edit_task_split[-1].strip("\n")
                        if task_complete == "No":
                            print_task_edit_menu2()
                            while True:
                                task_edit_choice = input("Select an option: ")

                                if task_edit_choice == '1':
                                    # reassigning a task to another user: call a relevant function and then display the menu
                                    change_user()
                                    print_task_edit_menu2()

                                elif task_edit_choice == '2':
                                    # changing due date of a task: call a relevant function and then display the menu
                                    change_due_date()
                                    print_task_edit_menu2()

                                elif task_edit_choice == '3':
                                    print_task_edit_menu()
                                    break

                                else:
                                    print("You have made a wrong choice, Please Try again")
                                    print_task_edit_menu2()

                        else:
                            print("The task has been completed and can't be edited.")
                            print_task_edit_menu()

                    elif edit_choice == '3':
                        break

                    else:
                        print("You have made a wrong choice, Please Try again")

            elif task_choice == -2:
                print_main_menu()
                break

            else:
                print("You've entered invalid number. Try again.")

    elif menu == 'gr':
        # generating task and user reports as a text file: call a relevant function and then display the menu
        gen_task_report()
        gen_user_report()
        print_main_menu()

    elif menu == 'ds':
        # displaying statistics: call a relevant function and then display the menu
        display_statistics()
        print_main_menu()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")