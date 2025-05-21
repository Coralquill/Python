def to_do():
    print("Welcome.This is Your To-Do list! ")


to_do()
print(""" What would you like:
      1. Add a new task
      2. Mark finished task
      3. View all tasks
      4. View unfinished tasks 
      5. View finished tasks
      6. Remove a task
      7. Quit""")

task=[]
completed_task=[]
while True:
    action=input("Choice : ").strip()
    if action =="1":
        add=input("Enter task: ")
        task.append(add)
        print("Task added")
    elif action=="2":
        try:
            if not task:
                print("No unfinished tasks to mark :")
                continue
            for x,y in enumerate(task,1):
                print(x,y)
            c=int(input("Which task to be marked :"))
            if 0<c<=len(task):
                entry=task.pop(c-1)
                completed_task.append(entry)
                print("Task marked finished")
            else:
                print("invalid task number")
                continue
        except ValueError:
            print("enter a proper index")
            continue
    elif action=="3":
        for x in task:
            print(x)
        for x in completed_task:
            print(x)
    elif action=="4":
        for x in task:
            print(x)
    elif action=="5":
       for x in completed_task:
            print(x)       
    elif action=="6":
        if not task:
            print("No tasks to remove!")
            continue
        try:
            for x,y in enumerate(task,1):
                print(x,y)
            b=int(input("which task to remove: "))
            if 0<b<=len(task):
                task.pop(b-1)
                print("Task removed")
        except ValueError:
            print("Enter a valid index")
    elif action=="7":
        print("You have exited the program. Goodbye!")
        break
    else:
        print("ERROR: Enter a proper action!")
        continue