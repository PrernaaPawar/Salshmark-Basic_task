class Task:
    def __init__(self, description, priority=1):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Priority: {self.priority})"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority=1):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print("Task removed successfully.")
        except IndexError:
            print("Invalid task number.")

    def list_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def prioritize_task(self, task_number, new_priority):
        try:
            task = self.tasks[task_number - 1]
            task.priority = new_priority
            print(f"Task {task_number} priority updated to {new_priority}.")
        except IndexError:
            print("Invalid task number.")

    def recommend_tasks(self, keyword):
        recommended_tasks = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if recommended_tasks:
            print("Recommended tasks:")
            for task in recommended_tasks:
                print(task)
        else:
            print("No tasks found matching the keyword.")
def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management App")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Prioritize task")
        print("5. Recommend tasks")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-5): "))
            task_manager.add_task(description, priority)
        elif choice == "2":
            task_number = int(input("Enter task number to remove: "))
            task_manager.remove_task(task_number)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            task_number = int(input("Enter task number to prioritize: "))
            new_priority = int(input("Enter new priority (1-5): "))
            task_manager.prioritize_task(task_number, new_priority)
        elif choice == "5":
            keyword = input("Enter keyword to search for: ")
            task_manager.recommend_tasks(keyword)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()