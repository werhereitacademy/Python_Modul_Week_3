
Id_tracking=[]

tasks = [
    {"sequence_number": 1, "task_name": "Task 1", "status": "Pending"},
    {"sequence_number": 2, "task_name": "Task 2", "status": "Completed"},
    {"sequence_number": 3, "task_name": "Task 3", "status": "Pending"},
]


#MR E 
def add_task():
    
    Id_tracking.sort() 
    
    task=input("Please enter the task:")
    if len(Id_tracking)==0:
        
        id_temp=len([x  for x in tasks if x["status"]!="Deleted"])+1
        tasks.append({"sequence_number":id_temp,"task_name":task,"status":"pending"})
        
    else:
        tasks.append({"sequence_number":Id_tracking[0],"task_name":task,"status":"pending"})
        Id_tracking.pop(0)

    tasks.sort(key=lambda x: (x['sequence_number'] is None, x['sequence_number']))
    print (f'"{task}" is added')


#Mrs I
def list_completed_tasks():

    completed_tasks = list(filter(lambda task: task["status"] == "Completed", tasks))

    if completed_tasks:

        print("Completed Tasks:")
        
        for task in completed_tasks:   
        
            print( f'ID number:{task["sequence_number"]}-{task["task_name"]}')

    else: 
        print("No completed tasks found!")

#Mrs I
def list_all_tasks():

    all_tasks = list(filter(lambda tasks: tasks["status"] != "Deleted", tasks))

    if all_tasks:
        
        print("---All Tasks---")

        for task in all_tasks:
            print(task["sequence_number"], "-", task["task_name"], "Status:",task["status"])

    else:
       
        print("No tasks found!")
#Mrs E
def compleet_a_task():
    if tasks:
        user=int(input("Please enter an ID number: "))
        task_control=False
        for task in tasks:
            if task['sequence_number']==user:
                if task["status"]=="Completed":
                    print("It is already completed")
                    task_control=True
                if task["status"]=="Pending":
                    task["status"]="Completed"
                    task_control=True
                    
                    
                    print(f'Task "{task["task_name"]}" is completed')
        if not task_control:
            print("Id is not found")
    else:
        print("There is no task")

# Mr N 
def delete_task():
    """Delete a task from the system."""
    if tasks:
        try:
            sequence_number = int(input("Enter the ID number of the task to delete: "))
            for task in tasks:
                if task["sequence_number"] == sequence_number:
                    confirm = input(f"Are you sure you want to delete the task '{task['task_name']}'? (Y/N): ").strip().upper()
                    if confirm == "Y":
                        task["status"] = "Deleted"
                        Id_tracking.append(sequence_number) 
                        task["sequence_number"]=None
                        print(f"Task deleted successfully: {task['task_name']}")
                    elif confirm == "N":
                        print("Task deletion canceled.")
                    else:
                        print("Invalid choice. Task deletion canceled.")
                    return
            print("Task is not found")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("There is no task")



while True:
    print("\n\n1-Add task")
    print("2-Delete task")
    print("3-List all completed task")
    print("4-List all tasks")
    print("5-Complete the task")
    print("6-Logout\n\n")

    chs=int(input("Please enter your choice:"))

    if chs==1:
        add_task()
    elif chs==2:
        delete_task()
    elif chs==3:
        list_completed_tasks()
    
    elif chs==4:
        list_all_tasks()
    elif chs==5:
        compleet_a_task()
    else:
        print("You are logged out")
        break
