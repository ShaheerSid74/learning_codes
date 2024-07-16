# to do list
tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task'{task}' added.")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")
def display_tasks():
    if tasks:
        print("To-Do List:")
        for i,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print ("No tasks in the To-Do list.")
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. remove Task")
    print("3. display Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the To-Do list application.")
        break
    else:
        print("Invalid choice. Please select a number between 1 to 4")