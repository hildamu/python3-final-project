import sqlite3


class Task:

    def __init__(self, id, task, completed):
        self.id = id
        self.task = task
        self.completed = completed
        

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"{self.id}. [{status}] {self.task}"


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        for task in self.tasks:
            print(task)

    def mark_all_complete(self):
        for task in self.tasks:
            task.mark_complete()

    def delete_task(self, task_id):
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                print(f"Task with ID {task_id} deleted.")
                return  
        print(f"Task with ID {task_id} not found.")


def create_table():
    """Creates a 'tasks' table with 'id', 'task', and 'completed' columns."""
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, completed INTEGER)''')
    conn.commit()
    conn.close()


def create_task(task):
    """Adds a new task to the database, creating a Task object and storing the due date (if provided) internally."""
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()
    print("Task added successfully!")
    return Task(c.lastrowid, task, False)  


def view_tasks():
    """Retrieves and displays all tasks from the database, excluding due dates."""
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    task_list = TaskList()  
    for row in rows:
        task_list.add_task(Task(row[0], row[1], row[2]))  
    task_list.view_tasks()  
    conn.close()


def mark_complete(task_id):
    """Marks a task as completed based on its ID."""
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id =?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task with ID {task_id} marked as complete.")


def delete_task(task_id):
    """Deletes a task from the database based on its ID."""
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id =?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task with ID {task_id} deleted.")

