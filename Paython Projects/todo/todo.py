


def display_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks in the To-Do List.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Added task: {task}")

def remove_task(task_number):
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Removed task: {removed_task.strip()}")
        else:
            print("Invalid task number. Please try again.")
    except FileNotFoundError:
        print("No tasks in the To-Do List.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_todo_list()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            display_todo_list()
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
