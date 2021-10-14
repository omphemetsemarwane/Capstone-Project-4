# Capstone-Project-IV
# Lists, Functions and String Handling : Task Manager Part 2
# Project Information
# Description

This Task Manager is a programme written in Python programming language. This project was designed to help a small business in managing tasks assigned to each member of a team.
This programme assist a small business to create, store, display and edit tasks and other information to and from text files.

# Features (How it works)

When running the programme, the user will be presented with different fuctions that are used to perform certain actions when called out based on the user's choice from the menu. These functions are blocks of code that store certain information and then output certain results based on actions defined in that function.

After functions are declared, dictionaries and lists are used to store the user's and task's information from the programme. The text files ('user.txt' and 'tasks.txt') are opened and the existing information is stored in specific lists and dictionaries in the programme.

The programme is exercuted, allowing the user to login using with their username and password credentials. The programme also check if the user's credentials are correct by making sure that their 'username' and 'password' they entered matches the corresponding information in the specific 'passwords' and 'usernames' lists. If the 'username' and 'password' entered is incorrect, an appropriate error message is displayed and the programme will repeatedly ask the user to enter their credentials until they match the 'username' and 'password' information stored in the appropriate 'passwords' and 'usernames' lists.

Once the user's details are correct, a successful login message is displayed to the user and the user is presented with the menu options:
 > register users
 > add tasks
 > view all tasks
 > view tasks assigned to the user specifically
 > generate reports
 > or exit the program

Only the 'Admin' user has an extra option in their specific menu that allows them to 'display statistics' and 'generate reports'. These options are not available on other users menu. Specific letters are displayed with each menu option that the user can choose to select an option from the menu (the user can type vm to view my tasks):

> r - register a user
> a - add task
> va = view all tasks
> vm = view my tasks
> e - exit

A while loop is used to display the menu to the user, this is done so that after each option chosen by the user, the user will be able to go back to the main menu in order to select another option if they want or to exit the programme. The corresponding functions to the options in the menu are called out to perform certain actions when the user input the letter that matches to that menu option. 

EXAMPLE:

If the user input 'a' to add task, the fuction 'add_task()' is exercuted. This function ask the user to input all the information related to the task they want to add, (e.g the user is asked to input the username of the person the task is assigned to, the title of the task, the description of the task, the due date of the task, the date the task was assigned, whether or not the task is completed). This information is then added to a specific tasks dictionary and is written from the dictionary to a text file ('tasks.txt'). The same process is followed if the user chooses 'r' to register a user, the reg_user() fuction is exercuted. This function ask the user to input information related to the new user they wish to register(e.g the user is asked to enter a new username and password), if the new user credentials are correct (doesn't exist) they are stored in the appropriate 'usernames' and 'passwords' lists in the program. The users details are then written in the text file ('user.txt'). If they try to register an existing user, an appropriate error message is displayed



# Capstone-Project-III
# Files: Task Manager
# Project Information
# Description

This Task Manager is a programme written in Python programming language. This project was designed to help a small business in managing tasks assigned to each member of a team.
This programme assist a small business to create, store, display and edit tasks and other information to and from text files.

# Features (How it works?)

When running the programme, the user will be presented with different fuctions that are used to perform certain actions when called out based on the user's choice from the menu. These functions are blocks of code that store certain information and then output certain results based on actions defined in that function.

After functions are declared, dictionaries and lists are used to store the user's and task's information from the programme. The text files ('user.txt' and 'tasks.txt') are opened and the existing information is stored in specific lists and dictionaries in the programme.

The programme is exercuted, allowing the user to login using with their username and password credentials. The programme also check if the user's credentials are correct by making sure that their 'username' and 'password' they entered matches the corresponding information in the specific 'passwords' and 'usernames' lists. If the 'username' and 'password' entered is incorrect, an appropriate error message is displayed and the programme will repeatedly ask the user to enter their credentials until they match the 'username' and 'password' information stored in the appropriate 'passwords' and 'usernames' lists.

Once the user's details are correct, a successful login message is displayed to the user and the user is presented with the menu options:
 > register users
 > add tasks
 > view all tasks
 > view tasks assigned to the user specifically
 > generate reports
 > or exit the program

Only the 'Admin' user has an extra option in their specific menu that allows them to 'display statistics' and 'generate reports'. These options are not available on other users menu. Specific letters are displayed with each menu option that the user can choose to select an option from the menu (the user can type vm to view my tasks):

> r - register a user
> a - add task
> va = view all tasks
> vm = view my tasks
> e - exit

A while loop is used to display the menu to the user, this is done so that after each option chosen by the user, the user will be able to go back to the main menu in order to select another option if they want or to exit the programme. The corresponding functions to the options in the menu are called out to perform certain actions when the user input the letter that matches to that menu option. 

EXAMPLE:

If the user input 'a' to add task, the function 'add_task()' is exercuted. This function ask the user to input all the information related to the task they want to add, (e.g the user is asked to input the username of the person the task is assigned to, the title of the task, the description of the task, the due date of the task, the date the task was assigned, whether or not the task is completed). This information is then added to a specific tasks dictionary and is written from the dictionary to a text file ('tasks.txt'). The same process is followed if the user chooses 'r' to register a user, the reg_user() function is exercuted. This function ask the user to input information related to the new user they wish to register(e.g the user is asked to enter a new username and password), if the new user credentials are correct (doesn't exist) they are stored in the appropriate 'usernames' and 'passwords' lists in the program. The users details are then written in the text file ('user.txt'). If they try to register an existing user, an appropriate error message is displayed

If the user input 'va' to view all tasks, the view_all() function is exercuted. The user is not asked to input any information because all the tasks stored in 'tasks.txt' file are displayed to the user in a friendly easy-to-read manner in appropriate order. If the user input 'vm' to view tasks assigned to them, the view_mine() function is exercuted. Only tasks assigned to them(based on their username) are displayed to them from the 'tasks.txt' file. The user is given an option to edit one of their tasks listed by typing it's number and this is followed by several questions, if they don't want to edit any task they can type '-1' to go back to the main menu

If the user input 'gr' to generate reports, the generate_reports() function is exercuted. This function generates two text files('task_overview.txt' and the 'user_overview.txt'), the new text files which are created when this programme run. These text files store information relating to statistics of tasks and users information. An appropriate message is displayed to inform the user that the reports were generated successfully.

Only the 'Admin' user can input 'ds' to display statistics, the display_stats() function is exercuted. This function is used to view the reports that have been generated in the previous menu option. The reports with all the relevant statistics are displayed to the user in a friendly-manner 

# How to use this Task Manager? 

* To run this programme, you need to download the Python interpreter program onto your computer operating system so that this Task Manager programme can be exercuted.
* Link to download Python on your computer(e.g Mac, Linux, Windows etc.) https://www.python.org/downloads/
* The existing text files ('tasks.txt' and 'user.txt') and generated text files('task_overview.txt' and the 'user_overview.txt') can be viewed with a simple Notepad app. This     app comes with Windows OS
* Link to download an appropriate Notepad app to view text file, https://notepad-plus-plus.org/downloads/
* Once you have 'tasks.txt' and 'user.txt'(Task Manager files to use), and Notepad and Python are downloaded successfully, you need IDLE(An Intergrated Development Environment).   IDLE is a safe environment to view and run your code. Python comes with built-in IDLE that can be accessed easily by opening the IDLE files from the program with the Python     interpreter
* Once IDLE is opened it will display a "Shell" window, from the window, click "File", then click "Open" from the Toolbar(top of the Window) to open the Task Manager.
* To run the Task Manager, click "Run" from the top Toolbar and check the output that shows in the Python shell Window.
* If the user choose 'gr' to generate reports, the text files will be created in the same folder and you can view then in the Notepad

# Contributers

I worked on this project on my own and it was reviewed and commented on by my mentor at Hyperion Development

