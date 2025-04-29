#task manager
# 
tasks = []
íd = 0
while True:
    print("1/ Add task")
    print("2/ Remove task")
    print("3/ Show tasks")
    print("4/ List tasks")
    print("5/ Exit")
    choice = input("Choose an option: ")
    if choice	== "1":
        name = input("Enter task name: ")
        status = input("Enter task status: ")
        due_date = input("Enter task due date: ")  
        task = {
            "id": id,
            "name": name,
            "status": status,
            "due_date": due_date
        }
        tasks.append(task)
        íd += 1
        print("Task added.")
    elif choice == "2":
        task_id = int(input("Enter task ID to remove: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task removed.")
                break
        else:
            print("Task not found.")
    elif choice == "3":
        for task in tasks:
            print(f"ID: {task['id']}, Name: {task['name']}, Status: {task['status']}, Due Date: {task['due_date']}")    
            print("Do you want to edit this task? (yes/no)")
            edit_choice = input()
            if edit_choice.lower() == "yes":
                new_name = input("Enter new task name: ")
                new_status = input("Enter new task status: ")
                new_due_date = input("Enter new task due date: ")  
                task["name"] = new_name
                task["status"] = new_status
                task["due_date"] = new_due_date
                print("Task updated.")
            elif edit_choice.lower() == "no":
                print("No changes made.")
            else:
                print("Invalid choice. No changes made.")

    elif choice == "4":
        print("List of tasks:")
        print("1/ ID\t 2/ Name\t 3/ Status\t 4/ Due Date\t 5/ Comleted Tasks")
        
        choiselist = input("Choose a task to list: ")
        if choiselist == "1":
            for task in tasks:
                print(f"ID: {task['id']}, Name: {task['name']}")
        elif choiselist == "2":
            for task in tasks:
                print(f"ID: {task['id']}, Name: {task['name']}")
        elif choiselist == "3":
            for task in tasks:
                print(f"ID: {task['id']}, Status: {task['status']}")
        elif choiselist == "4":
            for task in tasks:
                print(f"ID: {task['id']}, Due Date: {task['due_date']}")
        elif choiselist == "5":
            for task in tasks:
                if task["status"].lower() == "completed":
                    print(f"ID: {task['id']}, Name: {task['name']}")

        else:
            print("Invalid choice.")
            break
    elif choice == "5":
        print("Exiting the task manager.")
        break
    


