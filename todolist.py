class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task updated: '{old_task}' -> '{new_task}'")
        else:
            print("Invalid task number.")

    def mark_as_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task marked as done: {self.tasks[task_number - 1]['task']}")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task description: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to mark as done: "))
                todo_list.mark_as_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            try:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
