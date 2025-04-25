# List to hold tasks
tasks = []
next_number = 1

# Function to add a new task
def add_task():
    global next_number
    name = input("Enter the task name: ")
    
    # Check for any task marked as 'removed' to reuse the slot
    for t in tasks:
        if t['status'] == 'Removed':
            t['name'] = name
            t['status'] = 'Not Done'
            print("Task added at slot", t['number'])
            return
    
    # Add a new task if no 'removed' tasks
    tasks.append({'number': next_number, 'name': name, 'status': 'Not Done'})
    print("Task added with number", next_number)
    next_number += 1

# Function to mark a task as finished
def finish_task():
    num = int(input("Enter task number to mark as finished: "))
    for t in tasks:
        if t['number'] == num and t['status'] == 'Not Done':
            t['status'] = 'Completed'
            print("Task", num, "is now completed.")
            return
    print("Task not found or already completed.")

# Function to remove a task
def remove_task():
    num = int(input("Enter task number to remove: "))
    for t in tasks:
        if t['number'] == num and t['status'] != 'Removed':
            t['status'] = 'Removed'
            print("Task", num, "has been removed.")
            return
    print("Task not found or already removed.")

# Function to display completed tasks
def show_completed_tasks():
    print("\nCompleted Tasks:")
    for t in tasks:
        if t['status'] == 'Completed':
            print(t['number'], t['name'])

# Function to display all tasks
def show_all_tasks():
    print("\nAll Tasks:")
    for t in tasks:
        print(t['number'], t['name'], "-", t['status'])

# Main loop for user interaction
while True:
    print("\nChoose an option:")
    print("1- Add Task")
    print("2- Finish Task")
    print("3- Remove Task")
    print("4- Show Completed Tasks")
    print("5- Show All Tasks")
    print("6- Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        finish_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        show_completed_tasks()
    elif choice == '5':
        show_all_tasks()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")