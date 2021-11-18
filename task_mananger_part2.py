# this program is a continuation of the previous capstone project 20#

# in this program the code is modified using functions to improve the modularity of the code#

# the program includes four functions : reg_user, add_task, view_all and view_mine#

# the function reg_user was modified to make sure that it doesn't duplicate usernames that exists in user.txt#

# an error message is displayed if the user enters a username that is not listed in "user.txt"#

# the username and password provided by the user was stored in a text f(user.txt)#

# This program make us of dictionaries and functions to improve the functionality of the code#

# Datatime module was imported for date comparison(to check tasks that are overdue)#

from datetime import date
import datetime

# This block of code checks if there is any content in the 'user.txt' file
# If there is no content, the sign_up() function will be executed
file = open('user.txt', 'r').readlines()
user_count = [line for line in file]


# Function 1: This function, sign_up() allow's the admin to sign up only if its the first time the program is being run
def sign_up():
    # Printing the welcome message and giving instructions to the first user(admin)
    print("||===========| WELCOME TO THE TASK MANAGER |==============||")
    print("\t\t>>>>>>THE FIRST USER MUST BE THE ADMIN<<<<<<")
    print("\n>>>Create ADMIN user PROFILE:")
    print("\n||==========| Your Username is set to 'Admin' by default |==========||")

    username_admin = 'admin'  # This set up the admin username as default
    password_admin = input('Confirm your new password: ')  # This request the admin to enter their new password
    password2_admin = input('Re-type your new password: ')

    while password_admin != password2_admin:
        print("Password do not match, Retry Again!")
        password_admin = input('Confirm your new password: ')  # This request the admin to enter their new password
        password2_admin = input('Re-type your new password: ')

    # The admin username and password are written to the user.txt file
    file = open('user.txt', 'w')
    file.write(f"{username_admin}, {password_admin}")
    file.close()
    print("\nAdmin profile Successfully created!")


# Executing the signup function if its the first time the program is being ran
if len(user_count) == 0:
    sign_up()

# This welcome the user and ask them to give their username and password
print("||============| TASK MANAGER |=============||")
print()
print("||==================| LOGIN |==============||")
print("\nPlease follow the instructions below and enter your login details.\n")

# This the ask user to enter their username so they can login
user_name = input("Enter your username: ")
user_name = user_name + ','  # This adds (',') charecter to match username like it is saved in the 'user.txt' file
user_name = user_name.lower()

# This ask the user to enter their password so they can login
password = input("Enter password: ")
password = password.lower()


# Function 2: This fuction is for logging in, it checks if user is registered to use task manager
def credentials_check():
    """ This function check login details """
    # This block runs if the password and username are diffent as stated by the program
    info_user = open("user.txt", "r")  # This extract password and username from the 'user.text' file
    username_password = ''  # This variable is used to hold password and username

    for line in info_user:
        username_password += line
    info_user.close
    username_password = username_password.split()  # This split the lines in the 'user.text' file so it is easy to find password/username

    global user_name  # The 'Global' keyword is used in order to use the variables that are assigned out of the function

    global password

    # This make sure that password and username are different
    while user_name == password + ',':  # A while loop run's until the password and username entered are not the same
        print("\nThe Username and Password cannot be similar!!\nTry Again!.")  # If password and username are the same,
        # the user will be asked to re-enter the username and password
        print()  # Empty space
        user_name = input("Enter username: ")
        password = input("Enter password: ")

    while user_name not in username_password or password not in username_password:
        print("\nInvalid Login Details!!\n\nTry Again!!")
        user_name = input("Enter username: ")
        user_name = user_name + ','  # This adds a (',') charecter in order to match the username saved in the 'user.txt' file
        user_name = user_name.lower()

        # This ask the user to enter their password so they can login
        password = input("Enter password: ")
        password = password.lower()


# Function 3:  This  function is called to register a user
# This ask the user to enter a new username and password

def reg_user():
    """ This Function is used to register a user """
    # This ensures that the new username does not exist already
    print(
        "Hint: Make sure that the username and password are not the same!")  # This give the user a hint to enter password and username that are not the same
    name_available = True
    while name_available:  # A while loop run's until the user enter's a new username
        username = input("\nEnter the new username: ")
        username = username.lower()

        # This code extract username/password and store in a string
        file = open("user.txt", "r")
        password_username = ''
        for line in file:
            password_username += line
        file.close()
        password_username = password_username.split()  # This seperates the passowords & usernames

        # This code validates username, checks if the new username does not exist already
        available_username = 0  # This hold the existing name for later use
        user_name_available = False
        for name in password_username:  # The for loop is used to search for the username
            if name.lower() in username + ',':
                available_username = name
                user_name_available = True  # If the new username entered is found, the user is asked to enter
                # a different one
        if user_name_available:  # This code run's if the new username entered exist's already
            print("Sorry!")
            print(f"Username '{available_username}' already exists! Enter a different one")
        else:
            break  # The code will break, move to the next stage if the new username entered new username does not exist

    # This ask the user for the new password and adds the new user details to the 'user.txt' file
    password = input("Enter the new password: ")
    password = password.lower()

    # This code adds the new user's password to the 'user.txt' file
    file = open("user.txt", 'a')
    file.write('\n{0}, {1}'.format(username, password))  # This writes the username and password to the 'user.txt' file
    file.close()

    # This tell's the user that their account was created successfully
    print(" Your account was created successful!")


# Function 4: This function is called out when the user want to add a task
def add_task():
    """ This Function is to add a task"""
    username_taskowner = input(
        "Enter the username of user the task is being assigned to: ")  # This ask for the username of the user the task is assigned to
    username_taskowner = username_taskowner.lower()
    task_title = input("Enter the title of the task: ")
    task_title = task_title.lower()
    description = input("Enter the description of the task: ")
    description = description.lower()
    due_date = input("Enter the due date of the task (yyyy-mm-dd)(e.g 2021-02-26): ")
    due_date = due_date.lower()
    current_date = datetime.date.today()
    current_date = str(current_date)
    current_date = current_date.lower()
    task_completed = 'No'

    # This writes the provided information about the task to the 'task.txt' file
    file = open('tasks.txt', 'a')
    file.write(
        f"\n{username_taskowner},{task_title},{current_date},{due_date},"
        f"{task_completed},{description}")
    file.close()

    # This informs the user that task information has been recorded successfully
    print("\nThe task information has been recorded successfully.\n")


# Function 5: This fuction is called out if the user want to to view all tasks
def view_all():
    """ This Function is used to view all tasks"""
    print("*********\tThese are all the tasks recorded********")

    # This calculates the number of lines, in order to print the tasks in order
    line_count = 0
    file = open('tasks.txt', 'r')
    for line in file:
        line_count += 1
    file.close()

    # This display's out all tasks in a friendly-manner
    file2 = open('tasks.txt', 'r')

    new_list = []
    new = [line.split('\n') for line in
           file2]  # This splits the lines in tasks.txt file in order to print a specific information
    for i in new:  # This then split the lines further
        new_list.append(str(i).split(','))
    file2.close()

    for i in range(line_count):  # This prints the tasks in friendly_manner
        print(f"Task:\t\t\t{new_list[i][1]}")
        print("Assigned to:\t\t{}".format(new_list[i][0].replace("['", '')))
        print(f"Date Assigned:\t\t{new_list[i][2]}")
        print(f"Due date:\t\t{new_list[i][3]}")
        print(f"Task Completed?:\t{new_list[i][4]}")
        description1 = new_list[i][5].replace("]", '')
        description2 = new_list[i][5].replace("'", '')
        description3 = description2.replace(description2[-1], '')
        print(f"Task Description:\t{description3}")
        print()


# Function 6: This function is called out when the user want to view tasks assigned the user that is currently logged in
def view_mine():
    """ This Function is used to view tasks assigned to current user"""
    global user_name  # The global keyword is used so that the function can use globally defined username variable
    newname = user_name.replace(',', '')
    username = newname

    # Function 7: This function is called when the user want to edit tasks, this function will be used at a later stage
    def replace_line(file_name, line_num, text):
        """ This Function is used to replace words in the text file"""
        lines = open(file_name, 'r').readlines()  # This opens a file
        lines[line_num] = text  # This use's a line number that will be provided when the function is executed
        out = open(file_name, 'w')
        out.writelines(lines)  # This writes the newly provided information to the file
        out.close()

    # This calculates the number of lines in the 'tasks.txt' file
    line_count = 0
    file = open('tasks.txt', 'r')
    for line in file:
        line_count += 1
    file.close()

    # This print out tasks in friendly-manner
    file2 = open('tasks.txt', 'r')
    new_list = []
    new = [line.split('\n') for line in file2]  # This splits the lines in txt file
    for i in new:
        new_list.append(str(i).split(','))  # This splits the lines further in order to extract a specific information
    file2.close()

    # This search for the username and display/print the tasks
    print("\nHint: IF NO INFORMATION IS PRINTED, YOU CURRENTLY HAVE NO TASKS!.")
    print("\t*****This Are Your Tasks:****\n")
    task_number = []  # This keeps track of task count to allocate numbers to tasks
    for i, value in enumerate(new_list):
        username_provided = str(new_list[i][0]).replace(' ', '')  # This removes blank space
        username_provided = username_provided.replace("['", '')  # This removes ([')
        username_provided = username_provided.replace(":", '')  # This removes semicolon (:)
        if username_provided == username:  # This checks the current user so that their tasks are printed
            task_number.append(i)
            print(f"Task number: {i}")
            print(f"Task:\t\t\t{new_list[i][1]}")
            print("Assigned to:\t\t{}".format(new_list[i][0].replace("['", '')))  # This removes ([')
            print(f"Date Assigned:\t\t{new_list[i][2]}")
            print(f"Due date:\t\t{new_list[i][3]}")
            print(f"Task Completed?:\t{new_list[i][4]}")
            description1 = new_list[i][5].replace("]", '')  # This removes ('])
            description2 = new_list[i][5].replace("'", '')  # This removes blank space
            description3 = description2.replace(description2[-1], '')  # This  removes char ] at the end
            print(f"Task Description:\t{description3}")
            print()

    # This code block allow the user to select and edit a Task
    print("If you want to edit a task, Please enter the Task Number, or enter -1 to go back to the Menu\n")

    # This code ensures that the user input is correct.
    for i in range(4):  # This gives the user only 4 attempts before asking them to restart
        try:
            user_tasknumber = int(input("please enter the task number or -1 to go back to the Menu: "))
        except:
            print(
                "Invalid input!, Retry Again!")  # This line is for error handling(catch error) if user enters an incorrect input
            continue

        if user_tasknumber == -1:
            break

        elif user_tasknumber not in task_number:  # This check's if the user input a number not corresponding to any task
            print("You have entered an invalid task number!, Retry Again!")
        else:
            break

    run = True
    while run:
        if user_tasknumber != -1:  # This code run's if the user does not choose to go back to the Menu or exit, if the user has selected a task
            print(f"\nYou have choose to edit Task {user_tasknumber}")
            print("\nSelect 1 of the options below.\n\n1 - Mark the task as complete.\n2 - Edit the task.")

            # This ask the user to choose whether to mark or edit one of their task's
            user_choice = int(input("\nEnter either 1 or 2.\nEnter your option here: "))

            # This code run's ff the user has selected to mark their task complete
            if user_choice == 1:
                file20 = open('tasks.txt', 'r').readlines()
                file21 = [line.split(',') for line in file20]

                if (file21[user_tasknumber][4]) == 'Yes':
                    print("The task is already marked as complete!\n")
                    break

                status_task = input("\nIs the task completed? (y/n): ")

                # This updates the chosen line in the file in order to mark the task as complete
                if status_task.lower() == 'y':
                    task_lines = open('tasks.txt', 'r').readlines()
                    exact_tasknumber = user_tasknumber
                    line_split = task_lines[exact_tasknumber].split(
                        ',')  # This splits the line corresponding to the chosen task
                    line_split[4] = 'Yes'

                    # The Lambda function is used to change a list into a string to write to the file
                    list_to_string = lambda a, str1='' + ',': str1.join(a)
                    string_new = list_to_string(line_split)

                    # Writing the updated file line to our text file
                    replace_line('tasks.txt', exact_tasknumber, string_new)
                    print("\nThe task has been marked as complete!")


            # This code changes the task due date, and user task is assigned to a specific user
            elif user_choice == 2:
                # This check first if the chosen task is not yet marked as complete
                task_lines = open('tasks.txt', 'r').readlines()
                line_split = task_lines[user_tasknumber].split(',')
                if 'yes' in line_split or 'Yes' in line_split:  # This checks if task is not yet completed
                    print("\nHINT! The Task is marked as complete it cannot be edited!")
                    break

                # The user can edit the task if the task is not marked as complete
                elif 'yes' not in line_split or 'Yes' not in line_split:
                    print(
                        "\nWhich part of the task do you want to alter?")  # This ask the user to enter a part of the task they want to change
                    print("N - Username to whom task is assigned\nD - Due Date\nB - Both")
                    answer_user = input("\nPlease enter your answer here: ")

                    if answer_user.lower() == 'n':  # This code changes the username
                        newtask_username = input("Please enter the new username: ")

                        # This updates the chosen line in the file to alter the username to which the task is assigned
                        task_lines = open('tasks.txt', 'r').readlines()
                        exact_tasknumber = user_tasknumber
                        line_split = task_lines[exact_tasknumber].split(',')
                        line_split[0] = newtask_username

                        # The Lambda function is used to turn list into string to write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        string_new = list_to_string(line_split)  # This converts list into a string

                        # This writes the updated file line in a text file, this replace the old username with the new one
                        replace_line('tasks.txt', exact_tasknumber, string_new)
                        print("\nThe username has been successfully changed")
                        break

                    elif answer_user.lower() == 'd':  # This code changes the due date of the task
                        new_duedate = input("\nPlease enter the new Due Date (dd/mm/yyyy)(e.g 26/02/2021): ")

                        # This updates the chosen line in the file to alter the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines()  # This opens the task.txt file
                        exact_tasknumber = user_tasknumber
                        line_split = task_lines[exact_tasknumber].split(',')
                        line_split[3] = new_duedate

                        # The Lambda function is used to turn list into string to write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        string_new = list_to_string(
                            line_split)  # This converts list into a string to write to the txt file

                        # This writes the updated file line to the text file, this replaces the old username with the new one
                        replace_line('tasks.txt', exact_tasknumber, string_new)
                        print("\nThe due date of the Task has been changed successfully")
                        break

                    # This code run's if the user chooses to alter both the due date and user task is assigned to
                    elif answer_user.lower() == 'b':

                        # This code changes the username to whom a task is assigned to
                        newtask_username = input("Enter the new Username here: ")

                        # This updates the chosen line in the file to alter the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines()
                        exact_tasknumber = user_tasknumber
                        line_split = task_lines[exact_tasknumber].split(',')
                        line_split[0] = newtask_username

                        # The Lambda function is used to turn list into string to write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        string_new = list_to_string(line_split)  # This converts list into a string

                        # This writes the updated file line to the text file, this replaces the old username with the new one
                        replace_line('tasks.txt', exact_tasknumber, string_new)
                        print("\nThe username was changed successfully")

                        # This code changes the due date of the selected task
                        new_duedate = input("\nPlease enter the new Due Date (dd/mm/yyyy)(e.g 26/02/2021): ")

                        # This updates the chosen line in the file to alter the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines()  # This opens the task.txt file
                        exact_tasknumber = user_tasknumber
                        line_split = task_lines[exact_tasknumber].split(',')
                        line_split[3] = new_duedate

                        # The Lambda function is used to turn list into string to write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        string_new = list_to_string(
                            line_split)  # This converts list into a string to write to the txt file

                        # This writes the updated file line to the text file, this replaces the old username with the new one
                        replace_line('tasks.txt', exact_tasknumber, string_new)
                        print("\nThe Task due date was changed successfully")
                        break

                    else:
                        print(
                            "\nInvalid Input! Please read the instructions carefully!")  # This is for error handling(catch error- If user enters invalid input)
                else:
                    print(
                        "Invalid Input! Please enter the CORRECT number or Option")  # This is for error handling(catch error- If user enters invalid input)

            else:
                print(
                    "Invalid Input! Please enter a Valid number or Option")  # This is for error handling(catch error- If user enters invalid input)


##################|| STATISTICS SECTION ||###################
def display_stats():  # Function 8: This function is called when the user want to calculate and display statisticts
    """ This Function is used to display statistics in the text file"""
    # This calculates the number of tasks
    task_count = 0
    file = open('tasks.txt', 'r')
    for line in file:
        task_count += 1
    file.close()

    # This calculatesthe number of users
    user_count = 0
    file = open('user.txt', 'r')
    for line in file:
        user_count += 1
    file.close()

    # This print out the statistics
    print("\nWELCOME ADMIN! the statistics are as follows:\n")
    print(f"The total number of the registered users is: {user_count}")
    print(f"The total number of the tasks is: {task_count}")


# Function 9: This function is called out when the user want generates reports linked to tasks
def generate_reports():
    # This counts the tasks
    lines_task = open('tasks.txt', 'r').readlines()
    tasks_count = len([line for line in lines_task])

    # This writes the tasks total to the task_overview.txt file
    out = open('task_overview.txt', 'w')
    out.write(f"tasks, {str(tasks_count)}")
    out.close()

    # This count the completed tasks
    completed_task_count = 0
    comp_task = open('tasks.txt', 'r').readlines()
    lines_split = [line.split(',') for line in comp_task if 'Yes' in line]  # This collects all the completed tasks
    completed_task_count = len([line for line in lines_split])

    # This writes the completed tasks total to the task_overview.txt file
    with open('task_overview.txt', 'a') as out1:
        out1.write(f"\ncompleted task, {str(completed_task_count)}")

    # This counts the incomplete tasks
    comp_task2 = open('tasks.txt', 'r').readlines()
    lines_split = [line.split(',') for line in comp_task2 if 'No' in line]  # This collects all the incomplete tasks
    incomplete_task_count = len([line for line in lines_split])

    # This writes the incomplete tasks total to the 'task_overview.txt' file
    with open('task_overview.txt', 'a') as out2:
        out2.write(f"\nincomplete task, {str(incomplete_task_count)}")

    # This calculates the number of tasks that haven't been completed and are overdue
    today = str(date.today())  # This is used to get the current date and change it into a string

    # This collects all incomplete tasks
    comp_task2 = open('tasks.txt', 'r').readlines()
    line2_split = [line.split(',') for line in comp_task2 if 'No' in line]

    # This counts the tasks that are due
    due_tasks_count = len([task for task in line2_split if task[3] < today])

    # This writes overdue tasks to the file 'task_overview.txt'
    with open('task_overview.txt', 'a') as out3:
        out3.write(f"\ndue tasks, {str(due_tasks_count)}")

    # This calculates the percentage of tasks that are incomplete
    task_percentage = open('task_overview.txt', 'r').readlines()  # This opens the tasks overview file
    line4_split = [line.split(',') for line in task_percentage]  # This splits the lines in 'task_overview.txt'
    all_tasks = [line[1] for line in line4_split if
                 line[0] == 'tasks']  # This splits the lines in 'task_overview.txt' further
    all_tasks = int(all_tasks[0])  # This collects the number of all tasks
    incomplete_tasks = [line[1] for line in line4_split if
                        line[0] == 'incomplete task']  # This collects incomplete tasks
    incomplete_tasks = int(incomplete_tasks[0])  # This collects the exact number of incomplete tasks
    incomplete_task_percentage = (
                (incomplete_tasks * all_tasks) / 100)  # This calculates the percentage of incomplete tasks
    incomplete_task_percentage = round(incomplete_task_percentage, 2)  # This rounds off the total to 2 decimal places

    # This writes the percentage of the tasks that are incomplete to the 'task_overview.txt' file
    with open('task_overview.txt', 'a') as out4:
        out4.write(f"\nincomplete task percentage, {str(incomplete_task_percentage)}")

    # This calculates the percentage of tasks that are due
    task_percentage = open('task_overview.txt', 'r').readlines()  # This openthe 'task_overview.txt' file
    line5_split = [line.split(',') for line in task_percentage]  # This splits lines in 'task_overview.txt'
    all_tasks = [line[1] for line in line5_split if
                 line[0] == 'tasks']  # This look for a "tasks" title to find number of tasks
    all_tasks = int(all_tasks[0])  # This sssign number of tasks to the variable all-tasks
    due_tasks = [line[1] for line in line5_split if
                 line[0] == 'due tasks']  # This look for a "tasks" title to find number of tasks
    due_tasks = int(due_tasks[0])  # This assign number of due tasks to the variable due_tasks
    due_task_percentage = ((due_tasks * incomplete_tasks) / 100)  # This calculates the percentage of due tasks
    due_task_percentage = round(due_task_percentage, 2)  # This rounds off the total to 2 decimal places

    # This writes the percentage of the tasks that are incomplete to the 'task_overview.txt' file
    with open('task_overview.txt', 'a') as out5:
        out5.write(f"\ndue task percentage, {str(due_task_percentage)}")

    # This print out results from the 'task_overview.txt' file
    print(f"\nTotal tasks: {str(tasks_count)}")
    print(f"\nTotal of completed tasks: {str(completed_task_count)}")
    print(f"\nIncomplete Tasks: {str(incomplete_task_count)}")
    print(f"\nTotal of Due Tasks: {str(due_tasks_count)}")
    print(f"\nIncomplete Tasks Percentage: {str(incomplete_task_percentage)}%")
    print(f"\nDue Tasks Percentage: {str(due_task_percentage)}%")


# Function 10: This function is called to generate reports linked to users
def generate_reports():
    with open('user_overview.txt', 'w+'):  # This line of code ensure that file is overwriten everytime code is run

        # =======================================
        # This counts the total of tasks
        with open('tasks.txt', 'r') as tasks_num:
            task_total = len([line for line in tasks_num])

        # This adds total users to the 'user_overview.txt' file
        with open('user_overview.txt', 'a') as file:
            file.write(f"Total Users,{task_total}")

        # ===============================================================
        def total_tasks_per_user():  # Function 11: This function is called out to calculate total tasks per user
            with open('tasks.txt', 'r') as file:
                name_carrier = [line.split(',')[0] for line in file]

                tasks_num_per_user = []

                for i in range(len(name_carrier)):
                    track = (f"\nThe Total Tasks Assigned To,{name_carrier[i]},{name_carrier.count(name_carrier[i])}")
                    if track not in tasks_num_per_user:
                        tasks_num_per_user.append(track)

                        # ----------------------------------------------------------------
                        # This adds number of tasks assigned to user to the 'user_overview.txt'
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)

        total_tasks_per_user()

        # ===================================================
        def percentage_tasks_per_user():  # Function 12: This function is used to calculate percentage of tasks assigned to each user
            # This code extract all names to count their occurrence, that why we determine tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_carrier = [line.split(',')[0] for line in file]

                tasks_num_per_user = []  # This variable is declared to avoid printong duplicate lines

                for num in range(len(name_carrier)):
                    track = (
                        f"\nThe Total Percentage of Tasks Assigned To,{name_carrier[num]},{int((name_carrier.count(name_carrier[num]) * 100) / task_total)}%")
                    if track not in tasks_num_per_user:  # This ensures that lines are not duplicated
                        tasks_num_per_user.append(track)

                        # -----------------------------------------------------------
                        # this adds number of tasks assigned to user to the 'user_overview.txt'
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)

        percentage_tasks_per_user()

        # ==========================================================
        def percentage_completed_tasks_per_user():  # Function 13: This fuction called out to calculate the percentage of completed tasks
            # This extract all names tocount their occurrence, that's why we determine tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_carrier = [line.split(',')[0] for line in file]

                # This extract names linked to complete tasks to count their occurrence, that's why we determine Percentage of Complete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    complete_task_user = [line.split(',')[0] for line in file2 if line.split(',')[4] == 'Yes']

                tasks_num_per_user = []  # This variable is declared to avoid printing duplicate lines
                for num in range(len(complete_task_user)):
                    track = (
                        f"\nThe Total Percentage of Complete Tasks Assigned To,{complete_task_user[num]},{int((complete_task_user.count(complete_task_user[num]) * 100) / name_carrier.count(complete_task_user[num]))}%")

                    if track not in tasks_num_per_user:  # This ensures that lines are not duplicated
                        tasks_num_per_user.append(track)
                        # -------------------------------------------------
                        # This adds number of tasks assigned to user to the 'user_overview.txt'
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)

        percentage_completed_tasks_per_user()

        # =======================================================
        def percentage_incomplete_tasks_per_user():  # Function 14: This function is called out to calculate percentage of incomplete tasks assigned per user
            # This extract all names to count their occurrence, that's why we determine tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_carrier = [line.split(',')[0] for line in
                                file]  # This line of code provide us with the number of tasks assigned to each user

                # This extract names linked to complete tasks to count their occurrence, that's why we determining Percentage of inomplete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    incomplete_task_user = [line.split(',')[0] for line in file2 if line.split(',')[4] == 'No']

                tasks_num_per_user = []  # This variable is declared to avoid duplicating lines
                for num in range(len(incomplete_task_user)):
                    track = (
                        f"\nThe Total Percentage of Incomplete Tasks Assigned To,{incomplete_task_user[num]},{int((incomplete_task_user.count(incomplete_task_user[num]) * 100) / name_carrier.count(incomplete_task_user[num]))}%")

                    if track not in tasks_num_per_user:  # This ensures that lines are not duplicated
                        tasks_num_per_user.append(track)
                        # ---------------------------------------------------
                        # This adds number of tasks assigned to user to the 'user_overview.txt'
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)

        percentage_incomplete_tasks_per_user()

        # ===================================================
        def percentage_incomplete_due_tasks_per_user():  # Function 15: This function is called out to calculate percentage of incomplete due tasks assigned per user
            # This extract all names tocount their occurrence, that why we determine tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_carrier = [line.split(',')[0] for line in
                                file]  # This line of code provide us with the number of tasks assigned to each user

                # This extract names linked to incomplete due tasks to count their occurrence, that's why we determine Percentage of inomplete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    incomplete_task_user = [line.split(',')[0] for line in file2 if
                                            line.split(',')[4] == 'No' and line.split(',')[3] < str(date.today())]

                tasks_num_per_user = []  # This variable is declared to avoid duplicate lines
                for num in range(len(incomplete_task_user)):
                    track = (
                        f"\nTotal Percentage of Incomplete Due Tasks Assigned To,{incomplete_task_user[num]},{int((incomplete_task_user.count(incomplete_task_user[num]) * 100) / name_carrier.count(incomplete_task_user[num]))}%")

                    if track not in tasks_num_per_user:  # This ensures that lines are not duplicated
                        tasks_num_per_user.append(track)

                        # ------------------------------------------------------
                        # This adds number of tasks assigned to user to the 'user_overview.txt'
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
    percentage_incomplete_due_tasks_per_user()


generate_reports()  # This executes the function for generating reports


# ============================================================================

# Function 16: This function is called out to display reports in a friendly_manner
def generate_reports():
    with open('user_overview.txt', 'r') as file:
        info_splitted = [line.split(',') for line in file]  # This splits data in order to use specific parts/sections

        print("=================================================================================")
        print("   DESCRIPTION             ||        NAME         ||            INFORMATION       ")
        print("========================== ||=====================||==============================")
        for line in info_splitted:
            if line[0] == 'Total Users':  # This prints out Total Users
                print(f"Total Users                        ||             N\A                         {line[1]}")
                print("____________________________________||___________________________||______________________")

            elif line[0] == 'The Total Tasks Assigned To':  # This prints out Total Tasks per user
                print(
                    f"Total Number of Tasks Assigned To           ||            {line[1]}                            {line[2]}")
                print(
                    "_____________________________________________||________________________________||_________________________")
        print()
        print(
            "==================================================================================================================")
        for line in info_splitted:
            if line[0] == 'The Total Percentage of Tasks Assigned To':  # This printsout Total Percentage of Tasks
                print(
                    f"Percentage of Tasks Assigned To            ||             {line[1]}                            {line[2]}")
                print(
                    "____________________________________________||_________________________________||_________________________")

        print()
        print(
            "=================================================================================================================")
        for line in info_splitted:  # This prints out Total Percentage of Complete Tasks per user
            if line[0] == 'The Total Percentage of Complete Tasks Assigned To':
                print(
                    f"Percentage of Complete Tasks Assigned To      ||            {line[1]}                            {line[2]}")
                print(
                    "______________________________________________||________________________________||__________________________")

        print()
        print(
            "==================================================================================================================")
        for line in info_splitted:  # This prints out Total Percentage of Incomplete Tasks per user
            if line[0] == 'Total Percentage of Incomplete Tasks Assigned To':
                print(
                    f"Percentage of Inomplete Tasks Assigned To      ||            {line[1]}                            {line[2]}")
                print(
                    "________________________________________________||_______________________________||__________________________")

        print()
        print(
            "==================================================================================================================")
        for line in info_splitted:  # This prints out Total Percentage of Incomplete Due Tasks per user
            if line[0] == 'Total Percentage of Incomplete Due Tasks Assigned To':
                print(
                    f"Percentage of Incomplete Due Tasks Assigned To ||            {line[1]}                            {line[2]}")
                print(
                    "________________________________________________||_______________________________||________________________||")


# IN THIS SECTION OF THE CODE

# This ask the user to log in, the program will only allow user to proceed only if their details are correct

credentials_check()  # This calls the credential checker() function to ensure that the inputed details are correct
print("\nYou have logged in successfully!")
print(' ')  # Empty space

go_on = True

while go_on:

    # This prints out a welcome message
    print("\n||======================| TASK MANAGER |======================||")

    # This prints out the Main Menu
    print("Please select one of the following options:\n")
    if user_name == 'admin,':  # Only the user with the username 'Admin' can register user
        print("r  - register user")
    print("a  - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    if user_name == 'admin,':  # Only the user with the username 'Admin' can  generate reports
        print("gr - generate reports")
    if user_name == 'admin,':  # Only the user with the username 'Admin' can  view stats
        print("vs - view statistics")
    print("e  - exit")

    # This asks the user to select an option
    print()
    user_option = input("\nPlease enter your option: ")
    user_option = user_option.lower()

    # This function is called if user the option is to register user
    if user_option == 'r':
        if user_name == 'admin,':  # Only the user with the username 'Admin' can  register users
            reg_user()

    # This function is called if the user choice is to add a task
    if user_option == 'a':
        add_task()

    # This function is called if user option is to view all task
    if user_option == 'va':
        view_all()

    # This function is called if user option is to view their task
    if user_option == 'vm':
        view_mine()

    # This function is called if user option is to view statistics
    if user_option == 'vs':
        if user_name == 'admin,':
            display_stats()  # Only the user with the username 'Admin' can  view stats

    # If user option is to view statistics
    if user_option == 'gr':
        if user_name == 'admin,':  # Only the user with the username 'Admin' can  generate reports
            generate_reports()

    # If user option is to exit
    if user_option == 'e':
        go_on = False
print("\nThank You! :)")
print("\nGoodbye!")
