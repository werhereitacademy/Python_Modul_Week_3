# week3 huiswerk :TASK MANAGER APPLICATION

# version1

def display_menu():
    print("\n***TASK MANAGER***")
    print("1.Add task")
    print("2.Complete task")
    print("3.Delete task")
    print("4.Completed list")
    print("5.List all")
    print("6.Exit")

def add_task(tasks, sequence_number):
    if not sequence_number:
        print("Cannot add task. No sequence numbers available")
        return
    task_name=input("Enter task name:").strip()
    seq_num=sequence_number.pop(0)
    task={
        "sequence number": seq_num,
        "task name": task_name,
        "status": "pending"
    }
    tasks.append(task)
    print(f"Task {task_name} added successfully with sequence number {seq_num}\n")

def complete_task(tasks):
    seq_num=int(input("Enter the sequence number of the task to completed:"))
    for task in tasks:
        if task["sequence number"]==seq_num and task["status"]!="deleted":
            task["status"]="completed"
            print(f"task '{task['task name']}' marked as completed")
            return
    print("Task is not found or already deleted")
def deleted_task(tasks, sequence_number):
    seq_num=int(input("Enter the sequence number of the task to deleted:"))
    for task in tasks:
        if task["sequence number"]==seq_num and task["status"]!="deleted":
            task["status"]="deleted"
            sequence_number.append(seq_num)
            sequence_number.sort()
            print(f"task '{task['task name']}' deleted successfully")
            return
    print("Task is not found or already deleted")
def list_completed_task(tasks):
    completed_tasks=[task for task in tasks if task["status"]=="completed"]
    if not completed_tasks:
        print("No completed task")
    else:
        print("Completed task:")
        for task in completed_tasks:
            print(f"{task['sequence number']}. {task['task name']}")
def list_all_task(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("\nAll tasks:")
        for task in sorted(tasks, key=lambda x:x["sequence number"]):
            print(f"{task['sequence number']}:{task['task name']}-{task['status']}")

def main():
    tasks=[]
    sequence_number=list(range(1,101))
    while True:
        display_menu()
        choice=input("\nEnter your choice:").strip()
        if choice=="1":
            add_task(tasks,sequence_number)
        elif choice=="2":
            complete_task(tasks)
        elif choice=="3":
            deleted_task(tasks, sequence_number)
        elif choice=="4":
            list_completed_task(tasks)
        elif choice=="5":
            list_all_task(tasks)
        elif choice=="6":
            print("\nExiting task manager")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()




# version 2

# Görev listesi
gorevler = []

# Yeni görev ekleme fonksiyonu
def yeni_gorev_ekle(gorev_adi):
    gorev = {
        'sira_numarasi': len(gorevler) + 1,
        'gorev_adi': gorev_adi,
        'durum': 'Beklemede'
    }
    gorevler.append(gorev)
    print(f"{gorev_adi} gorevi basariyla eklendi")

# Tum gorevleri listeleme fonksiyonu
def tum_gorevleri_listele():
    print('\nTum Gorevler:')
    if len(gorevler) == 0:
        print('Henuz bir gorev eklemediniz...')
        return False
    for gorev in gorevler:
        print(f"{gorev['sira_numarasi']}. {gorev['gorev_adi']} - Durum: {gorev['durum']}")
    return True

# Tamamlanmıs gorevleri listeleme fonksiyonu
def tamamlanmis_gorevleri_listele():
    print('\nTamamlanmis görevler:')
    tamamlanmis = []
    for gorev in gorevler:
        if gorev['durum'] == 'Tamamlandi':
            tamamlanmis.append(gorev)
    if len(tamamlanmis) > 0:
        for gorev in tamamlanmis:
            print(f"{gorev['sira_numarasi']}. {gorev['gorev_adi']}")
    else:
        print('Henuz tamamlanmis gorev yok.')

# Gorev tamamlama fonksiyonu
def gorev_tamamla():
    tum_gorevleri_listele()
    try:
        sira_numarasi = int(input('\nTamamlamak istediginiz gorevin sira numarasini girin: '))
        for gorev in gorevler:
            if gorev['sira_numarasi'] == sira_numarasi:
                gorev['durum'] = 'Tamamlandi'
                print(f"{sira_numarasi}. siradaki görev tamamlandi.")
                return
        print(f"{sira_numarasi}. siradaki görev bulunamadi.")
    except ValueError:
        print('Gecersiz giris. Lutfen gecerli bir numara girin.')


# Görev silme fonksiyonu
def gorev_sil():
    tum_gorevleri_listele()
    try:
        sira_numarasi = int(input('\nSilmek istediginiz gorevin sira numarasini girin: '))
        for gorev in gorevler:
            if gorev['sira_numarasi'] == sira_numarasi:
                gorevler.remove(gorev)
                for i, g in enumerate(gorevler):
                    g['sira_numarasi'] = i + 1
                print(f"{sira_numarasi}. siradaki gorev silindi.")
                return
        print(f"{sira_numarasi}. siradaki gorev bulunamadi.")
    except ValueError:
        print('Gecersiz! Lutfen gecerli bir numara girin.')

# Menü
while True:
    print('\nMENU')
    print('1 - Yeni görev ekle')
    print('2 - Bir görevi tamamla')
    print('3 - Bir görevi sil')
    print('4 - Tamamlanmis gorevleri listele')
    print('5 - Tum gorevleri listele')
    print('6 - QUIT')

    secim = input('\nNe yapmak istersiniz (1-6): ')
    if secim == "1":
        gorev_adi = input("Yeni gorev adini giriniz: ")
        yeni_gorev_ekle(gorev_adi)
    elif secim == "2":
        gorev_tamamla()
    elif secim == "3":
        gorev_sil()
    elif secim == "4":
        tamamlanmis_gorevleri_listele()
    elif secim == "5":
        tum_gorevleri_listele()
    elif secim == "6":
        print("Programdan cikiliyor...")
        break
    else:
        print("Gecersiz secim! Lutfen 1-6 arasinda bir secenek giriniz.")
