tasks = []

while True:
    print("\n1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. List Completed Tasks")
    print("5. List All Tasks")
    print("6. Exit")
    choice = input("Choose an option: ")

    #1. Add Task and with deleted id reuse
    if choice == '1':
        task_name = input("Enter task name: ")
        reused = False

        for i in range(len(tasks)):
            if tasks[i]["status"] == "Deleted":
                reused_id = tasks[i]["id"]
                tasks[i] = {
                    "id": reused_id,
                    "name": task_name,
                    "status": "Pending"
                }
                print(f"Task added using deleted slot with ID {reused_id}")
                reused = True
                break

        if not reused:
            new_id = len(tasks) + 1
            task = {
                "id": new_id,
                "name": task_name,
                "status": "Pending"
            }
            tasks.append(task)
            print(f"Task added with new ID {new_id}")

    #  2. Complete Task
    elif choice == '2':
        task_complete = int(input("Enter task ID to mark as completed: "))
        found = False

        for task in tasks:
            if task["id"] == task_complete and task["status"] != "Deleted":
                task["status"] = "Completed"
                print("Task marked as completed.")
                found = True
                break

        if not found:
            print("Task not found or already deleted.")

    # 3. Delete Task
    elif choice == '3':
        task_delete = int(input("Enter task ID to delete: "))
        found = False

        for task in tasks:
            if task["id"] == task_delete and task["status"] != "Deleted":
                task["status"] = "Deleted"
                print("Task marked as deleted.")
                found = True
                break

        if not found:
            print("Task not found or already deleted.")

    #  4. List Completed Tasks
    elif choice == '4':
        print("\n Completed Tasks:")
        for task in tasks:
            if task["status"] == "Completed":
                print(f"ID {task['id']}: {task['name']} [Completed]")

    #  5. List All Tasks and sorted by id
    elif choice == '5':
        print("\n All Tasks:")
        def get_task_id(task):
            return task["id"]

        for task in sorted(tasks, key=get_task_id):
            print(f"ID {task['id']}: {task['name']} [{task['status']}]")

    #  6. Exit
    elif choice == '6':
        print(" Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1–6.")