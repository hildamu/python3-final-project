class TaskList:
    """Model class representing a collection of tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new Task object to the list."""
        self.tasks.append(task)

    def view_tasks(self):
        """Prints all tasks in the list."""
        for task in self.tasks:
            print(task)

    def mark_all_complete(self):
        """Marks all tasks in the list as completed."""
        for task in self.tasks:
            task.mark_complete()

    def delete_task(self, task_id):
        """Deletes a task from the list based on its ID."""
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                return  
        print(f"Task with ID {task_id} not found.")

