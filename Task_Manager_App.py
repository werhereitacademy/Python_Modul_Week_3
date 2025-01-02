tasks = [] #Task list
task_number = 1#Global Task Number for list

#task = {
#    'Task Number': task_number,
#    'Task Name': task_name,
#    'Status': 'Pending'
#}

# Function to add a new task
def add_task(task_name):
    global task_number
    task = {
        'Task Number': task_number,
        'Task Name': task_name,
        'Status': 'Pending'
    }
    tasks.append(task)
    task_number += 1
    print(f"Task '{task_name}' has been added.")

# Function to mark task as completed
def complete_task(seq_num):
    for task in tasks:
        if task['Task Number'] == seq_num:
            task['Status'] = 'Completed'
            print(f"Task {seq_num} marked as completed.")
            break
    print(f"Task {seq_num} not found.")

# Delete task function
def delete_task(seq_num):
    global tasks
    task_to_delete = None
    for task in tasks:
        if task['Task Number'] == seq_num:
            task_to_delete = task
            break
    print(f"Task {seq_num} has been deleted.")

# Function to list completed tasks
def list_completed_tasks():
    completed_tasks = [task for task in tasks if task['Status'] == 'Completed']

    if not completed_tasks:
        print("No completed tasks available.")
        return

    print("\nCompleted Tasks:")
    for task in completed_tasks:
        print(f"Task Number: {task['Task Number']}, Task Name: {task['Task Name']}")

# Function to list all tasks
def list_all_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nAll Tasks:")
    for task in tasks:
        print(f"Task Number: {task['Task Number']}, Task Name: {task['Task Name']}, Status: {task['Status']}")

# Main menu
def main():
    global task_number
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. List completed tasks")
        print("5. List all tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            seq_num = input("Enter the Task number of the task to complete: ")
            complete_task(int(seq_num))
        elif choice == '3':
            seq_num = input("Enter the Task number of the task to delete: ")
            delete_task(int(seq_num))
        elif choice == '4':
            list_completed_tasks()
        elif choice == '5':
            list_all_tasks()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Start
if __name__ == "__main__":
    main()
