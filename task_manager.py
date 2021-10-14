#this program helps a small business to manage the tasks assigned to each member of the team#

#the user is asked to enter a username and password#

#the usernames and passwords are stored in a text f called "user.txt" in the order of (username, comma, space, password)#

#an error message is displayed if the user enters a username that is not listed in "user.txt"#

#an error message is displayed if the user enters a valid username but not a valid password#

#if the user enters incorrect credentials, the user is repeatedly asked to enter valid username and password until ther enter correct credentials#

#with open("user,txt","r") as f: (this opens the text f user.txt and stores the username and password provided by the user#

with open("user.txt", "r") as f:
    f = f.read()
    username = input("Enter username:")
    password = input("Enter password:")
    if username in f and password in f:
        print("Your are now signed in")

#once the user is logged in they are provided with a menu that allows them to register user, add task, view all tasks, view my tasks or exit#

menu = (input("""
Please select one of the following options:
r - register a user
a - add task
va = view all tasks
vm = view my tasks
e - exit
"""))

choice = "x"

#if the user chooses "r"(to register a user): the user should be prompted for a new username and password#

#the user is asked to confirm the password#

#If the value entered to confirm the password matches the value of the password, both the username and password are stored in a text f called "user.txt" #

#to store the username and password in a user.txt f, with open("user.txt", "a+") as f: is used to open the user.txt f and "a+" is used to add the data to the user.txt f#

while choice != "e":
    choice = input("Please enter your choice:")
    if choice == "r":
        username = input("Enter a username:")
        password = input("Enter a password:")
        with open("user.txt", "a+") as f:
            f.write(str(username) + "," + " " + str(password) + "\n")
            f.close()
            print()

#if the user chooses "a" (to add a task): the user should be prompted to enter#

#1, the username of the person the task is assigned to#

#2, the title of the task#

#3, the description of the task#

#4, the due date of the task#

#5, the date on which the task was assigned (this should be the current date)#

#6, wether or not the task has been completed and this value should be "No" #

#all these data is stored in a text f called "tasks.txt" #

#to store these data with open("tasks.txt", "a+") as f: is used to open the tasks.txt f and "a+" is used to add the data to tasks.txt f#

    elif choice == "a":
        username_person = input("Enter the username of the person the task is assigned to:")
        title_task = input("Enter the title of the task:")
        description = input("Enter the desription of the task:")
        duedate = input("Enter the due date of the task:")
        date_assigned = input("Enter the date the task was assigned, this should be the current date:")
        completed = "No"
        with open("tasks.txt", "a+") as f:
            f.write(str(username_person) + "," + str(title_task) + "," + str(description) + "," + str(duedate) + "," + str(date_assigned) + "," + str(completed) + "\n")
            f.close()
        print()

#if the user choose "va" (view all tasks): the information for each task is displayed on the screen in an easy to read format#

#to view all tasks the task.txt f is opened using, with open("tasks.txt", "r") as f: and a for loop is used to loop over the lines#

#the information on each line is the displayed on a screen using the print() function#

    elif choice == "va":
        with open("tasks.txt", "r") as f:
            for line in f:
                print(line)
        print()

#if the user choose "vm" (view my tasks):only the tasks assigned to the user that is currently logged-in will be displayed in a user-friendly, easy to read manner#

#to do this "tasks.txt" f must be opened using with open("tasks.txt", "r") as f:, "r" reads the tasks f#

#readlines() function is used to read the lines in tasks.txt f#

#split() function is used to split the line that holds information for the tasks meant for the loggin user from the tasks of other users#

#this tasks are username specific, therefor only tasks for the specific username(of the user currently logged in) will be displayed#

#the print() function is used to display the tasks on screen#

    elif choice == "vm":
        with open("tasks.txt", "r") as f:
            f = f.readlines()
            for line in f:
                username_person, title_task, description, duedate, date_assigned, completed = line.split(",")
                if username == username_person:
                    print(line)


#if the user choose "e" (exit): the program will stop#

    elif choice == "e":
        print("",)
    else:
        print("Unrecognized option.")






