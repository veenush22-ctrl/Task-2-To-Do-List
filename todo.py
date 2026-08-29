FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    task = input("\nEnter a new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    if not tasks:
        print("\nNo tasks available to remove.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Thank you for using the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
