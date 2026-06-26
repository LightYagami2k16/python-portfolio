# To-Do List
# Practice: lists, file I/O, functions, while loops

FILENAME = "tasks.txt"

def load_tasks():
    """Read tasks from the file. Returns a list of [task_name, is_done] pairs."""
    tasks = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    # Each line is saved as "done|task name" or "todo|task name"
                    status, name = line.split("|", 1)
                    tasks.append({"name": name, "done": status == "done"})
    except FileNotFoundError:
        pass  # No file yet — start with an empty list
    return tasks

def save_tasks(tasks):
    """Write all tasks back to the file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            status = "done" if task["done"] else "todo"
            f.write(f"{status}|{task['name']}\n")

def show_tasks(tasks):
    """Print all tasks with their numbers."""
    if not tasks:
        print("No tasks yet! Add one first.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        check = "✓" if task["done"] else " "
        print(f"  {i}. [{check}] {task['name']}")

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Quit")

# Main program
tasks = load_tasks()

while True:
    show_menu()
    choice = input("\nChoice: ").strip()

    if choice == "1":
        name = input("Enter your task: ").strip()
        if name:
            tasks.append({"name": name, "done": False})
            save_tasks(tasks)
            print("Task added!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        if tasks:
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks(tasks)
                    print(f'"{tasks[num - 1]["name"]}" marked as done!')
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        show_tasks(tasks)
        if tasks:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f'"{removed["name"]}" deleted.')
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please enter a number from 1 to 5.")
