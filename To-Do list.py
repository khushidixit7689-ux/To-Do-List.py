# To-Do List Application (Command Line)

tasks = []

def show_tasks():
    if not tasks:
        print("\n No tasks in the list!\n")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = " Done" if task['done'] else "Not Done"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully ")

def mark_done():
    show_tasks()
    task_no = int(input("Enter task number to mark as done: "))
    if 0 < task_no <= len(tasks):
        tasks[task_no-1]['done'] = True
        print("Task marked as done ✔")
    else:
        print("Invalid task number!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: "))
    if 0 < task_no <= len(tasks):
        removed = tasks.pop(task_no-1)
        print(f"Task '{removed['title']}' deleted ")
    else:
        print("Invalid task number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye ")
        break
    else:
        print("Invalid choice, try again!")
