tasks_info={}
delete_numbers=[]
seq_num=0

def get_next_sequence_number():
    global seq_num
    if delete_numbers:
        return delete_numbers.pop(0)
    else:
        seq_num+=1
        return seq_num
    
def add_task():
    global seq_num 
    task_name=input('enter the task: ')
    task_status='pending'
    seq_num=get_next_sequence_number()
    tasks_info[seq_num]={'name':task_name,'status':task_status}
    print(f'Task {seq_num} is added')
  

def complete_task():
    task_num=int(input('Enter the task number to complete: '))
    if task_num in tasks_info and tasks_info[task_num]['status']!='Delete':
        tasks_info[task_num]['status']='Complete'
        print(f'Task {task_num} is completed')
    else:
        print(f'The task {task_num} is not found or already deleted')

def delete_task():
    task_num=int(input('Enter the task number to delete: '))
    if task_num in tasks_info and tasks_info[task_num]['status']!='Delete':
        tasks_info[task_num]['status']='Delete'
        delete_numbers.append(task_num)
        print(f'Task {task_num} is deleted')
    else:
        print(f'Task {task_num} is not found or already deleted')

def list_task():
    print('Task List')
    if tasks_info:
        for seq,task in tasks_info.items():
            if task['status']!='Delete':
                print(f'{seq} : {task['name']} - {task['status']}')
    else:
        print('No tasks available')

def list_complete():
    if tasks_info.items():
        for seq,task in tasks_info.items():
            if task['status']=='Complete':
                print(f'{seq}: {task['name']} is completed')
            else:
                print('No tasks are completed.')


def main():
    while True:
        print("Task Manager ")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. List All Tasks")
        print("5. List Completed Tasks")
        print("6. Exit")

        user_input=input('choise number: ')
        if user_input=='1':
            add_task()
        elif user_input=='2':
            complete_task()
        elif user_input=='3':
            delete_task()
        elif user_input=='4':
            list_task()
        elif user_input=='5':
            list_complete()
        elif user_input=='6':
            break
        else:
            print('Invalid choise, please Try again')
        
main()
