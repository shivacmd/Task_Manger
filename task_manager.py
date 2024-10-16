import json

# Task class definition
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.id}: {self.title}"

# Function to load tasks from a file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)

# Function to add a task
def add_task(tasks):
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    task = Task(task_id, title)
    tasks.append(task)
    print(f"Task '{title}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks available.")

# Function to delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    task_found = False
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            print(f"Task '{task.title}' deleted.")
            task_found = True
            break
    if not task_found:
        print(f"Task with ID {task_id} not found.")

# Function to mark a task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    task_found = False
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task '{task.title}' marked as complete.")
            task_found = True
            break
    if not task_found:
        print(f"Task with ID {task_id} not found.")

# Main function to run the CLI
def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
