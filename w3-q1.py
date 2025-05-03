tasks = []
deleted = []
taskNumber = 0  # Tracks task numbers

def add_task():
    global taskNumber

    if deleted:
        deletedTaskNo = deleted.pop(0)
        for task in tasks:
            if task["taskNumber"] == deletedTaskNo and task["taskStatus"] == "deleted":
                task_name = input("Enter the task: ")
                task["taskName"] = task_name
                task["taskStatus"] = "pending"
                print(f"Reused Task no: {deletedTaskNo} updated with Name: '{task_name}'.")
                return

    taskNumber += 1
    new_task_number = taskNumber
    task_name = input("Enter the task: ")
    task = {"taskNumber": new_task_number, "taskName": task_name, "taskStatus": "pending"}
    tasks.append(task)
    print(f"Task no: {new_task_number} Task Name: '{task_name}' added.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"Task no: {task['taskNumber']} Task Name: '{task['taskName']}' Status: '{task['taskStatus']}'")

def delete_task():
    if not tasks:
        print("No tasks available.")
        return

    num = int(input("Enter the task number to delete: "))
    for task in tasks:
        if task["taskNumber"] == num and task["taskStatus"] != "deleted":
            task["taskStatus"] = "deleted"
            deleted.append(num)
            print(f"Task no: {num} deleted.")
            return
    print("Task not found or already deleted.")

def complete_task():
    if not tasks:
        print("No tasks available.")
        return

    num = int(input("Enter the task number to complete: "))
    for task in tasks:
        if task["taskNumber"] == num and task["taskStatus"] == "pending":
            task["taskStatus"] = "completed"
            print(f"Task no: {num} completed.")
            return
    print("Task not found or already completed/deleted.")

def main():
    while True:
        print("\nTask Manager")
        print("Choose an option:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
