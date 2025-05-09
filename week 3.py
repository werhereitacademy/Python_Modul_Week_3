list_tasks = {}
available_nums = []
task_counter = 1

def get_task_num():
    global task_counter
    return available_nums.pop(0) if available_nums else task_counter

while True:
    action = input("\n[A]dd  [D]elete  [Q]uit: ").strip().lower()

    if action == 'a':
        name = input("Task name: ")
        status = input("Status [C]ompleted / [P]ending: ").strip().lower()

        if status not in ['c', 'p']:
            print(" Enter C or P only.")
            continue

        stat = ("Completed", "Not pending") if status == 'c' else ("Not completed", "Pending")
        num = get_task_num()
        list_tasks[num] = {"Task Name": name, "Statuse is ": stat}
        if not available_nums: task_counter += 1
        print(f" Task {num} added.")

    elif action == 'd':
        try:
            num = int(input("Task number to delete: "))
            if num in list_tasks:
                del list_tasks[num]
                available_nums.append(num)
                available_nums.sort()
                print(f" Task {num} deleted.")
            else:
                print(" Task not found.")
        except:
            print(" Invalid number.")

    elif action == 'q':
        print(" Goodbye!")
        break

    else:
        print(" Invalid choice.")

    print("\n Task list:")
    for n in sorted(list_tasks):
        print(f"Task {n}: {list_tasks[n]}")
