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

def show_message(message):
    print(message)
    input("\nDevam etmek için bir tuşa basın...")
    
# Menu başlıgını yazdırır.
def menu_header(menu_name, menu_width=30):
    clear_screen()

    print(menu_width*'-')
    print(f"\033[1;33m"+ menu_name.center(menu_width)+f"\033[0m")
    print(menu_width*'-')

# Ana menuyu yazdırır.
def show_main_menu():
    menu_width = 30
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
    show_message("Görev başarıyla eklendi.")



def delete_task():
    menu_header("Delete Task",50)
    seq_number = get_input("Silmek istediğiniz görev numarasını girin: ")
    for task in tasks:
        if task["seq_number"] == seq_number:
            if task["status"] == "Deleted":
                show_message("Bu görev zaten silinmiş.")
                return
            task["status"] = "Deleted"
            task["seq_number"] = None
            show_message("Görev başarıyla silindi.")
            return
    show_message("Görev bulunamadı.")

def complete_task():
    menu_header("Complete Task",50)
    seq_number = get_input("Tamamlamak istediğiniz görev numarasını girin: ")
    for task in tasks:
        if task["seq_number"] == seq_number:
            if task["status"] == "Completed":
                show_message("Bu görev zaten tamamlanmış.")
                return
            
            task["status"] = "Completed"
            show_message("Görev başarıyla tamamlandı.")
            return
        
    show_message("Görev bulunamadı.")

def list_completed_tasks():
    menu_header("Completed Tasks", 50)

    completed_tasks = [task for task in tasks if task["status"] == "Completed"]
    if not completed_tasks:
        show_message("Tamamlanmış görev bulunamadı.")
    else:
        for task in completed_tasks:
            print(f"{task['seq_number']}. {task['task_name']}")
            input("\nDevam etmek için bir tuşa basın...")

def list_tasks():
    menu_header("All Tasks\nS.No\tTask\tStatus", 30)

    if not tasks:
        show_message("Görev bulunamadı.")

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