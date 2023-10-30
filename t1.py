class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

import pickle

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()

    def mark_completed(self, task):
        task.completed = True
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{index}. {task.description} (Priority: {task.priority}, Due Date: {task.due_date}, Status: {status})")

def main():
    file_path = 'tasks.pkl'
    task_manager = TaskManager(file_path)

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(description, priority, due_date)
            task_manager.add_task(task)
        elif choice == '2':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
            index = int(input("Enter the task number to remove: ")) - 1
            task_manager.remove_task(tasks[index])
        elif choice == '3':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
            index = int(input("Enter the task number to mark as completed: ")) - 1
            task_manager.mark_completed(tasks[index])
        elif choice == '4':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
