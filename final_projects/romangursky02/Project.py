# pip install tabulate - потрібно встановити для запуску програми

import os
from tabulate import tabulate

class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        table = []
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else " "
            table.append([index, task["description"], status])
        headers = ["#", "Task Description", "Done"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    def add_task(self, description):
        task = {"description": description, "done": False}
        self.tasks.append(task)
        print(f'Task "{description}" added successfully.')

    def mark_as_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print(f'Task #{task_number} marked as done.')
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            self.display_tasks()
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. Mark Task as Done")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == "2":
                task_number = int(input("Enter task number to mark as done: "))
                self.mark_as_done(task_number)
            elif choice == "3":
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                input("Invalid choice. Press Enter to continue.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
