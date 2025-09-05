tasks=[]
def add_task():
    task=input("ENter your task:")
    tasks.append(task)
    print(f"Task {task} Added!!!")
def view_task():
    if not tasks:
        print("No tasks to view....!!!")
    else:
        print("your tasks are:")
        for i,t in enumerate(tasks,start=1):
            print(f"{i}.{t}")
def remove_task():
    if  not tasks:
        print("No tasks to remove.....!!")
    else:
        print("your tasks are:")
        for i,t in enumerate(tasks,start=1):
            print(f"{i}.{t}")
        num= int(input("ENter the task number to remove:"))
        removed=tasks.pop(num-1)
        print(f"Removed the {removed} task Sucessfully")
def exit():
    print("GoodBye.....!!!!")

while True:
    print("----To Do List----")
    print("1-Add task:")
    print("2-View task:")
    print("3-Remove task:")
    print("4-Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        remove_task()
    elif choice=='4':
        exit()
        break
    else:
        print("INVALID CHOICE")
    
