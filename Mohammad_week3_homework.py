tasks = []

def creat_id():
    for i in range(1, len(tasks) + 2):
        if all(task['id'] != i for task in tasks):
            return i

def add_task(name):
    task = {
        'id': creat_id(),
        'name': name,
        'status': 'Pending'
    }
    tasks.append(task)
    print(f"the add task is dane: {name} (number: {task['id']})")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id and task['status'] != 'deleted':
            task['status'] = 'Completed'
            print(f" the task number :{task_id} successful.")
            return
    print("task not found")

def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Deleted'
            print(f"{task_id}. the task is deleted ")
            return
    print("the task is not found")

def list_all_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: x['id'])
    print("\n#### list tasks ####")
    for task in sorted_tasks:
        print(f"[{task['id']}] {task['name']} - {task['status']}")
    print("---------------------\n")

def list_completed_tasks():
    completed = [task for task in tasks if task['status'] == 'Completed']
    print("\n--- tasks completed--")
    for task in completed:
        print(f"[{task['id']}] {task['name']}")
    print("------------------------\n")

def main():
    while True:
        print("select process")
        print("1. Add new task")
        print("2.Complete a task")
        print("3.Delete a task")
        print("4. List all tasks with their status")
        print("5.List completed tasks")
        print("6.Exit")

        choice = input("inter ID of task: ")

        if choice == '1':
            name = input("inter name of task: ")
            add_task(name)
        elif choice == '2':
            try:
                task_id = int(input("inter number task for completed: "))
                complete_task(task_id)
            except ValueError:
                print("pleas inter correct.")
        elif choice == '3':
            try:
                task_id = int(input("inter  task number for delet it"))
                delete_task(task_id)
            except ValueError:
                print("pleas inter correct:")
        elif choice == '4':
            list_all_tasks()
        elif choice == '5':
            list_completed_tasks()
        elif choice == '6':
            print("good bay !")
            break
        else:
            print("try agian .")
main()

