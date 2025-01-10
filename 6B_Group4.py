"""
Yasin Bey,
        1 - Görev Ekleme fonksiyonu
            Fonksiyon adı: add_task
            Parametreler: tasks (list), tasks_file (str)
                tasks : Task listesi
                    task = {
                        "id": task_id,
                        "name": task_name,
                        "status": "Pending", "Completed", "Deleted"
                    }
                tasks_file : Task listesinin kaydedileceği dosya adı
            İşlev: Yeni bir görev ekler.
            İşlem:
                - Yeni bir görev oluşturulur ve tasks listesine eklenir.
                - Görev name kullanıcı tarafından girilir.
                - Yeni görevin id'si otomatik olarak atanır ve tasks listesindeki en büyük id'den bir fazla olacak şekilde oluşturulur.
                - Yeni görevin status'u "Pending" olarak ayarlanır.
                - task tasks listesine eklenir.
                - tasks dosyaya kaydedilir. save_file fonksiyonu kullanılır. save_file(tasks_file, tasks) şeklinde kullanılır.
                - Kullanıcıya görevin eklenmesi başarılı olduğu bilgisi verilir.
            Dönüş Değeri: Boolean (True)or False kayıt başarılı ise True başarısız ise False döner.
        2 - Görev Tamamlama fonksiyonu
            Fonksiyon adı: complete_task
            Parametreler: tasks (list), task_id (int), tasks_file (str)
                tasks : Task listesi
                task_id : Tamamlanacak görevin id'si
                tasks_file : Task listesinin kaydedileceği dosya adı
            işlev: Bir görevin tamamlanmasını sağlar.
            İşlem:
                - task_id ile tasks listesinde arama yapılır.
                - Eğer task_id ile eşleşen bir görev bulunamazsa, "Task not found" mesajı gösterilir ve fonksiyon sonlanır.
                - Eğer task_id ile eşleşen bir görev bulunursa, görevin status'u "Completed" olarak güncellenir.
                - tasks dosyaya kaydedilir. save_file fonksiyonu kullanılır. save_file(tasks_file, tasks) şeklinde kullanılır.
                - Kullanıcıya görevin tamamlanması başarılı olduğu bilgisi verilir.
            Dönüş Değeri: Boolean (True)or False kayıt başarılı ise True başarısız ise False döner.
    Kahraman Bey,
        3 - Görev Silme fonksiyonu
            Fonksiyon adı: delete_task
            Parametreler: tasks (list), task_id (int), tasks_file (str)
                tasks : Task Listesi
                task_id : Silinecek görevin id'si
                tasks_file : Task listesinin kaydedileceği dosya adı
            İşlev: Bir görevin statusun deleted olarak güncellenmesini sağlar.
            İşlem:
                - task_id ile tasks listesinde arama yapılır.
                - Eğer task_id ile eşleşen bir görev bulunamazsa, "Task not found" mesajı gösterilir ve fonksiyon sonlanır.
                - Eğer task_id ile eşleşen bir görev bulunursa, görevin status'u "Deleted" olarak güncellenir.
                - task_id değerine None atanır.
                - task_id si silinen task_id den büyük olan görevlerin id'leri bir azaltılır.
                - tasks dosyaya kaydedilir. save_file fonksiyonu kullanılır. save_file(tasks_file, tasks) şeklinde kullanılır.
                - Kullanıcıya görevin silinmesi başarılı olduğu bilgisi verilir.
            Dönüş Değeri: Boolean (True)or False kayıt başarılı ise True başarısız ise False döner.
    Neslihan Hanım,
        4 - Listeleme fonksiyonu
            Fonksiyon adı: list_tasks
            Parametreler: tasks (list), status (list)
                tasks : Task listesi
                status : Görevlerin listelenmek istenen durumu  örneğin status = ["Pending", "Completed"]
            İşlev: Görevleri listeler ve bir grid formatında görüntüler.
            İşlem:
                - tasks listesi içerisinde status değeri status parametresinin içinde olan görevler filtrelenir.
                - Filitrelenen görevler grid formatında görüntülenir.
                - Görevlerin id, name ve status bilgileri görüntülenir.
            Döüş Değeri: Listelediği görevlerin sayısını döner.
    Mustafa Gundoğdu:
        Ana program menüsü ile kullanıcıdan alınan seçeneklere göre fonksiyonları çağıran ve gerekli işlemleri yapan bir ana program yazınız.

"""

import json,os
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
#Yasin Sinan Code Block
def add_task(tasks, tasks_file):
    task_name = input("Enter the task name: ")
    task_id = 1

    for i in tasks:
        if i["id"] : 
            task_id = i["id"] + 1

    tasks.append({"id": task_id, "name": task_name, "status": "Pending"})

    save_file(tasks_file, tasks)

    print("Newstask added successfully")
    return True


def complete_task(tasks, task_id, tasks_file):
    for i in tasks:
        if i["id"] == task_id:
            i["status"] = "completed"

            save_file(tasks_file, tasks)

            print("Task status is changed")
            return True

    print("Task is not found")
    return False

#Kahraman Dal Code Block

def delete_task(tasks, task_id, tasks_file):
    
    task_found = False
    for task in tasks:
        if task.get("id") == task_id:
            task_found = True
            task["status"] = "Deleted"
            task["id"] = None
            break

    if not task_found:
        print("Task not found")
        return False


    for task in tasks:
        if task["id"] != None and task["id"] > task_id:
            task["id"] -= 1

    save_file(tasks_file, tasks)

    print(f"Task with ID {task_id} has been successfully deleted.")
    return True

#Neslihan Code Block
# List Tasks
def list_tasks(tasks, status=["Pending", "Completed"]):
    """
    Lists all tasks with their status in a grid format.
    """
    filtered_tasks = [task for task in tasks if task["status"] in status]
    
    #1 Print grid header
    print(f"\n{'ID':<10}{'Name':<60}{'Status':<15}")
   
    print("-" * 85)
    #* 50: Tire karakterini 50 defa tekrarlayarak bir çizgi oluşturur.
    
    for task in filtered_tasks:
        print(f"{str(task['id']):<10}{task['name']:<60}{task['status']:<15}")

#print_grid(None, filtered_tasks)
    task_count = len(filtered_tasks)
    print(f"\n Total tasks listed: {task_count}")

    return task_count



# Mustafa Gundogdu Code Block
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
            list_tasks(tasks,["Pending"])   
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
    else:
        print("Thank you for using the Task Manager. Goodbye!")
        input("Press Enter to exit...")
