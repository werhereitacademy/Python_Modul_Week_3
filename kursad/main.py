import os

clear_screen = lambda: print("\033[H\033[J")

tasks = []

# Sayısal girişi gecerli olarak alır.
def get_input(message="Lütfen bir işlem numarası giriniz: "):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("lütfen gecerli bir deger giriniz")

# Menu başlıgını yazdırır.
def menu_header(menu_name):
    clear_screen()
    global menu_width
    menu_width = 30
    print(menu_width*'-')
    print(f"\033[1;33m"+ menu_name.center(menu_width)+f"\033[0m")
    print(menu_width*'-')

# Ana menuyu yazdırır.
def show_main_menu():
    menu_header("Task Manager")

    print("1 - Add new task")
    print("2 - Delete task")
    print("3 - Complete task")
    print("4 - List completed tasks")
    print("5 - List all tasks")
    print("6 - Exit")
    print(menu_width*'-')

    selection = get_input()
    clear_screen()
    return selection

def get_seq_number():
    existing_numbers = {task["seq_number"] for task in tasks}
    i = 0
    while True:
        if i not in existing_numbers:
            return i
        i += 1

def add_task():
    menu_header("Add Task")

    task = {
        "seq_number": get_seq_number(),
        "task_name": input("Görev: "),
        "status":"Pending"
    }
    tasks.append(task)
    print(tasks)

    print("Görev başarıyla eklendi.")


def delete_task():
    menu_header("Delete Task")

    seq_number = get_input("Silmek istediğiniz görev numarasını girin: ")
    for task in tasks:
        if task["seq_number"] == seq_number:
            if task["status"] == "Deleted":
                print("Bu görev zaten silinmiş.")
                return
            task["status"] = "Deleted"
            task["seq_number"] = None
            print("Görev başarıyla silindi (işaretlendi).")
            return
    print("Görev bulunamadı.")

def complete_task():
    menu_header("Set Completed Tasks")

    seq_number = get_input("Tamamlamak istediğiniz görev numarasını girin: ")
    for task in tasks:
        if task["seq_number"] == seq_number:
            if task["status"] == "Completed":
                print("Bu görev zaten tamamlanmış.")
                return
            task["status"] = "Completed"
            print("Görev başarıyla tamamlandı.")
            return
    print("Görev bulunamadı.")

def list_completed_tasks():
    menu_header("Completed Tasks")

    completed_tasks = [task for task in tasks if task["status"] == "Completed"]
    if not completed_tasks:
        print("Tamamlanmış görev bulunamadı.")
    else:
        for task in completed_tasks:
            print(f"{task['seq_number']}. {task['task_name']}")
    input("\nDevam etmek için bir tuşa basın...")

def list_tasks():
    menu_header("All Tasks\nS.No\tTask\tStatus")

    if not tasks:
        print("Görev bulunamadı.")

    else:
        sorted_tasks = sorted(tasks, key=lambda x: x['seq_number']) 
        for task in sorted_tasks:
            print(f"{task['seq_number']}\t{task['task_name']}\t{task['status']}")
    input("\nDevam etmek için bir tuşa basın...")

while True:
    selection = show_main_menu()
    if selection == 1:
        add_task()
    elif selection == 2:
        delete_task()   
    elif selection == 3:
        complete_task()
    elif selection == 4:
        list_completed_tasks()
    elif selection == 5:
        list_tasks()
    elif selection == 6:
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")