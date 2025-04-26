tasks=[]

# add a task
def add_task(tasks):
    task_name = input("Enter task: ")
    sequence_num = len(tasks) + 1
    tasks.append({'id': sequence_num, 'name': task_name, 'status': 'Pending'})
    print("Task added.")

# complete a task
def complete_task(tasks):
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['name']} - {task['status']}")
    sequence_num = int(input("Enter task ID to complete: "))
    for task in tasks:
        if task['id'] == sequence_num:
            task['status'] = 'Completed'
            print("Task completed.")
            return
    print("Task not found.")

#list all completed tasks
def list_completed_tasks(tasks):

    if not tasks:
        print("No tasks available.")
        return

    completed_tasks = [task for task in tasks if task['status'] == 'Completed']
    if not completed_tasks:
        print("No tasks completed.")
    else:
        print("\nCompleted Tasks:")
        for task in completed_tasks:
            print(f"{task['sequence_number']}. {task['task_name']}")    

# delete a task.
def delete_task(tasks):
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['name']} - {task['status']}")
    sequence_num = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task['id'] ==sequence_num:
            task['status'] = 'Deleted'
            print("Task deleted.")
            return
    print("Task not found.")

# show all tasks.
def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    print("\nTasks:")
    for task in tasks:
        print(f"{task['id']}. {task['name']} - {task['status']}")

# main function.
def main():
    tasks = []
    while True:
        print("\nTask Manager:")
        print("1. Add")
        print("2. Complete")
        print("3. Delete")
        print("4. Show")
        print("5. Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            show_tasks(tasks)
        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Invalid.")


