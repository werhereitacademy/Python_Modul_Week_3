tasks=[]
deleted_tasks=[]

def add_newtask():
    task={}
    if len(tasks)==0:
        task['sequence_number']=1
    else:
        task['sequence_number']=max([x['sequence_number'] for x in tasks]) + 1
    task['task_name']=input('Enter the name of the task that you want to add: ')
    task['task_status']=input('Enter the status of the task ( Pending / Completed / Deleted )')
    tasks.append(task)
    print('New task added succesfully...')

def update_taskstatus():
    for task in tasks:
        print(task)
    choice=input('Enter the sequence number of the task that you want to change the status:')
    new_status=input('Enter the new status... Pending / Compeleted:  ')
    for task in tasks:
        if task['sequence_number']==int(choice):
            task['task_status']=new_status
            break
    print('Task status updated succesfully...')

def delete_task():
    for i in tasks:
        print(i)
    choice=input('Enter the sequence number of the task that you want to delete:')
    for task in tasks:
        if task['sequence_number']==int(choice):
            task['task_status']='Deleted'
            deleted_tasks.append(task)
            tasks.remove(task)
            break
    print('Task deleted succesfully...')

def list_completed_tasks():
    for task in tasks:
        if task['task_status']=='Completed':
            print(task)
    
def list_all_tasks():
    for task in tasks:
        print(task)
    for task in deleted_tasks:
        print(task)
        

def sequence_number(tasks):
    if tasks==[]:
        return 1
    
    else:
    
        sequence_number_set=set([x['sequence_number'] for x in tasks])
        
        matching_set=set(range(1,max(sequence_number_set)+1))
        
        if len(matching_set.difference(sequence_number_set))==0:
            return max([x['sequence_number'] for x in tasks]) + 1
        
        else:
            return min(matching_set.difference(sequence_number_set))


while True:
    print('Task Management System')
    print('---------------------------------')
    print("Enter '1' to add a new task")
    print("Enter '2' to update a task status")
    print("Enter '3' to delete a task")
    print("Enter '4' to list the completed tasks")
    print("Enter '5' to list all the tasks")
    print("Enter '6' to exit")
    choice=input("Enter your choice: ")
    if choice=='1':
        add_newtask()
    elif choice=='2':
        update_taskstatus()
    elif choice=='3':
        delete_task()
    elif choice=='4':
        list_completed_tasks()
    elif choice=='5':
        list_all_tasks()
    elif choice=='6':
        break
    else:
        print('Wrong entry! Please try again: ')