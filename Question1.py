#Project Description: In this assignment, you will create a task manager application using the Python programming language.
#This application will allow users to add, complete, delete, and list their tasks.
#Requirements:
#1-Tasks will be stored in a Python list and each task will be represented as a dictionary. Each task must have the following properties:
#Sequence Number (Automatically assigned). Task Name. Status (Completed, Pending, or Deleted)
#2- Operations that the user can perform:
#Add a new task. Complete a task. Delete a task. List completed tasks. List all tasks with their status. Exit
#3- 4- 5- 6

def greet_user():
    print("Welcome to Task Manager")
greet_user()  # Call the function

tasks = []          #task list will store all tasks
next_sequence = 1   #this will increase with each new task

# Function to add a new task
def add_task(name):  # name is a parameter
    global next_sequence
    task = {
        "Sequence": next_sequence,  #automatically assigned number
        "Name": name,               #task name entered by user
        "Status": "Pending"         #default status
    }
    tasks.append(task)
    print(f"Task '{name}' added with number {next_sequence}.")
    next_sequence += 1    #increase the task number for next task
    

# Function to complete a task
def complete_task(task_number):
    for task in tasks:
        if task["Sequence"] == task_number and task["Status"] == "Pending":  #find the task by its number and make sure it's not already done
            task["Status"] = "Completed"    #change status
            print(f"Task {task_number} marked as Completed.")
            return
    print("Task not found or cannot be completed.")     #if not found

# Function to delete a task
def delete_task(task_number):
    for task in tasks:
        if task["Sequence"] == task_number and task["Status"] != "Deleted":
            task["Status"] = "Deleted"
            print(f"Task {task_number} marked as Deleted.")
            return
    print("Task not found or already deleted.")

# Function to list all tasks
def list_tasks():
    print("\n Task List")
    for task in tasks:
        print(f"{task['Sequence']}: {task['Name']} - [{task['Status']}]")
    print()  # Empty line for spacing. extra space after list

# Main function to show the menu and take user input
def main():
    while True:
        print("Task Manager Menu")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. List All Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter the task name: ")
            add_task(name)
        elif choice == "2":
            number = int(input("Enter the task number to complete: "))
            complete_task(number)
        elif choice == "3":
            number = int(input("Enter the task number to delete: "))
            delete_task(number)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()