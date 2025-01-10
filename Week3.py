"""
Question 1: Task Manager Application
Project Description: In this assignment, you will create a task manager application using the Python programming language. This application will allow users to add, complete, delete, and list their tasks.

Requirements:
1- Tasks will be stored in a Python list and each task will be represented as a dictionary. Each task must have the following properties:

Sequence Number (Automatically assigned)

Task Name

Status (Completed, Pending, or Deleted)

2- Operations that the user can perform:

Add a new task

Complete a task

Delete a task

List completed tasks

List all tasks with their status

Exit

3- Tasks should automatically receive a sequence number in the order they are added.

4- New tasks should be saved in place of the numbers of deleted tasks.

5- When listing tasks, they should be sorted by their sequence number.

6- Appropriate feedback should be given to the user after each operation. For example, when a new task is added, they should see a message indicating that the task has been added.
"""
import os
import json
def create_grid(tasks, field_names, field_widths, grid_name):
    """
    Creates a grid of tasks.
    """
    start_first_row = "╔"
    end_first_row = "╗"
    start_middle_row = "╠"
    end_middle_row = "╣"
    start_last_row = "╚"
    end_last_row = "╝"
    separator_column = "║"
    separator_row = "═"
    separator_sub_row = "─"
    separator_sub_column = "│"
    grid = []
    grid_first_row = start_first_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_first_row
    grid.append(grid_first_row)
    grid_middle_row = separator_column+grid_name.center(sum(field_widths)+((len(field_widths)-1)*3)," ")+separator_column
    grid.append(grid_middle_row)
    grid_middle_row = start_middle_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_middle_row
    grid.append(grid_middle_row)
    field_counter = 0
    for field_name in field_names:
        if field_counter == 0:
            grid_middle_row = separator_column+field_name.center(field_widths[field_names.index(field_name)]," ")
            if field_counter != len(field_widths)-1:
                grid_middle_row += " "+separator_column+" "
            else:
                grid_middle_row += " "+separator_sub_column+" "
        elif field_counter == len(field_widths)-1:
            grid_middle_row += field_name.center(field_widths[field_counter]," ")+separator_column
        else:
            grid_middle_row += field_name.center(field_widths[field_names.index(field_name)]," ")+" "+separator_sub_column+" "
        field_counter += 1
    grid.append(grid_middle_row)
    grid_middle_row = separator_column+separator_sub_row*(sum(field_widths)+((len(field_widths)-1)*3))+separator_column
    grid.append(grid_middle_row)
    for task in tasks:
        field_counter = 0
        for field_name in field_names:
            if field_counter == 0:
                grid_middle_row = separator_column + str(task["id"]).center(field_widths[field_counter]," ")
                if field_counter == len(field_widths)-1:
                    grid_middle_row += " "+separator_column+" "
                else:
                    grid_middle_row += " "+separator_sub_column+" "
            elif field_counter == len(field_widths)-1:
                grid_middle_row += task[field_name].center(field_widths[field_counter]," ")+separator_column
            else:
                grid_middle_row += task[field_name].center(field_widths[field_names.index(field_name)]," ")+" "+separator_sub_column+" "
            field_counter += 1
        grid.append(grid_middle_row)
        if tasks.index(task) != len(tasks)-1:
            grid_middle_row = separator_column+separator_sub_row*(sum(field_widths)+((len(field_widths)-1)*3))+separator_column
            grid.append(grid_middle_row)
    grid_last_row = start_last_row+separator_row*(sum(field_widths)+((len(field_widths)-1)*3))+end_last_row
    grid.append(grid_last_row)
    return grid

def save_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # print(f"Data was successfully written to file: {file_path}")
    except Exception as e:
        print(f"Error: Data could not be written to file. Details: {e}")
def load_file(file_path):   
    """
    Reads a list from a file in JSON format.
    """
    if not os.path.exists(file_path):
        save_file(file_path, [])
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON format is invalid.")
        return []
    except Exception as e:
        print(f"Error: File could not be read. Details: {e}")
        return []
    
def add_task(tasks, tasks_file):
    """
    Adds a new task to the task list.
    """
    task_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    task_name = input("Enter the task name: ")
    task = {
        "id": task_id,
        "name": task_name,
        "status": "Pending"
    }
    tasks.append(task)
    save_file(tasks_file, tasks)
    print(f"Task {task_name} added successfully.")
    return True

def complete_task(tasks, task_id, tasks_file):
    """
    Completes the task with the given id.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_file(tasks_file, tasks)
            print(f"Task {task["name"]} completed successfully.")
            return True
    return False

def delete_task(tasks, task_id, tasks_file):
    """
    Deletes the task with the given id.
    """
    finding_task = False
    for task in tasks:
        if task["id"] != None:
            if task["id"] == task_id:
                task["id"] = None
                task["status"] = "Deleted"
                finding_task = True
            elif task["id"] > task_id:
                task["id"] -= 1
    if finding_task:
        save_file(tasks_file, tasks)
    else:
        print("Task not found.")
    return finding_task

def list_tasks(tasks, statatus = ["Pending"]):
    """
    Lists all tasks with their status.
    """
    listed_tasks = [task for task in tasks if task["status"] in statatus]
    grid = create_grid(listed_tasks, ["id", "name", "status"], [5, 50, 12], "Tasks List")
    for row in grid:
        print(row)
    return len(listed_tasks)
        

if __name__ == "__main__":
    tasks_file = "tasks.json"
    tasks = load_file(tasks_file)
    incorrectly_entered = False
    exit_confirmation = True
    main_menu = ["╔════════════════════════════════════════════════════════════╗ ",
                "║                  WELCOME TO TASK MANAGER                   ║ ",
                "╠════════════════════════════════════════════════════════════╣ ",
                "║                                                            ║ ",
                "║               (1) Add a new task                           ║ ",
                "║               (2) Complete a task                          ║ ",
                "║               (3) Delete a task                            ║ ",
                "║               (4) List commpleted tasks                    ║ ",
                "║               (5) List all tasks with their status         ║ ",
                "║                                                            ║ ",
                "╠════════════════════════════════════════════════════════════╣ ",
                "║                     (Q) Quit / Exit                        ║ ",
                "╚════════════════════════════════════════════════════════════╝ "
                ]
    while exit_confirmation:
        os.system("cls" if os.name == "nt" else "clear")
        if tasks :
            list_tasks(tasks)   
        for i in main_menu:
            print(i)
        if incorrectly_entered:
            print("Incorrect choice. Please try again.")
            incorrectly_entered = False
        
        choice = input("Enter your choice: ")
        if choice in ["q", "Q", "exit", "EXIT", "6"]:
            exit_confirmation = False
        elif choice == "1":
            if not add_task(tasks, tasks_file):
                print("Error: Task could not be added.")
            input("Press Enter to continue...")
        elif choice == "2":
            task_id = int(input("Enter the task id: "))
            if not complete_task(tasks, task_id, tasks_file):
                print("Error: Task could not be completed.")
            input("Press Enter to continue...")
        elif choice == "3":
            task_id = int(input("Enter the task id: "))
            if not delete_task(tasks, task_id, tasks_file):
                print("Error: Task could not be deleted.")
            input("Press Enter to continue...")
        elif choice == "4":
            tasks_count = list_tasks(tasks, ["Completed"])
            input(f"{tasks_count} tasks completed. Press Enter to continue...")
        elif choice == "5":
            tasks_count = list_tasks(tasks,["Pending", "Completed", "Deleted"])
            input(f"All missions total {tasks_count}. Press Enter to continue...")
        else:
            incorrectly_entered = True