class Task:
    """Model class representing a task in the to-do list."""

    def __init__(self, id, task, completed):
        self.id = id
        self.task = task
        self.completed = completed

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        """Provides a string representation of the task."""
        status = "✓" if self.completed else " "
        return f"{self.id}. [{status}] {self.task}"
