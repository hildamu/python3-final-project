# import sqlite3

# def setup_database():
#     conn = sqlite3.connect('todo.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS tasks (
#             id INTEGER PRIMARY KEY,
#             task TEXT NOT NULL,
#             completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
#         )
#     ''')
#     conn.commit()
#     conn.close()

# class Task:
#     def __init__(self, task, completed=False):
#         self.task = task
#         self.completed = completed

#     def save(self):
#         conn = sqlite3.connect('todo.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO tasks (task, completed) VALUES (?, ?)
#         ''', (self.task, self.completed))
#         conn.commit()
#         conn.close()


# class TaskList:
#     @staticmethod
#     def get_all():
#         conn = sqlite3.connect('todo.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT id, task, completed FROM tasks')
#         tasks = cursor.fetchall()
#         conn.close()
#         return tasks

#     @staticmethod
#     def mark_complete(task_id):
#         conn = sqlite3.connect('todo.db')
#         cursor = conn.cursor()
#         cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
#         conn.commit()
#         conn.close()

#     @staticmethod
#     def delete_task(task_id):
#         conn = sqlite3.connect('todo.db')
#         cursor = conn.cursor()
#         cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
#         conn.commit()
#         conn.close()

# def add_task(task):
#     new_task = Task(task)
#     new_task.save()
#     print("Task added successfully!")

# def view_tasks():
#     tasks = TaskList.get_all()
#     if tasks:
#         print("Your to-do list:")
#         for task in tasks:
#             status = "✓" if task[2] else " "
#             print(f"{task[0]}. [{status}] {task[1]}")
#     else:
#         print("Your to-do list is empty.")

# def mark_complete(task_id):
#     TaskList.mark_complete(task_id)
#     print("Task marked as complete!")

# def delete_task(task_id):
#     TaskList.delete_task(task_id)
#     print("Task deleted successfully!")

# def main():
#     setup_database()

#     while True:
#         print("\nMenu:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Complete")
#         print("4. Delete Task")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             task = input("Enter the task: ")
#             add_task(task)
#         elif choice == "2":
#             view_tasks()
#         elif choice == "3":
#             task_id = int(input("Enter the task ID to mark as complete: "))
#             mark_complete(task_id)
#         elif choice == "4":
#             task_id = int(input("Enter the task ID to delete: "))
#             delete_task(task_id)
#         elif choice == "5":
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
import sqlite3

def setup_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

class Task:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def save(self):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (task, completed) VALUES (?, ?)
        ''', (self.task, self.completed))
        conn.commit()
        conn.close()

class TaskList:
    @staticmethod
    def get_all():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, task, completed FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    @staticmethod
    def mark_complete(task_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

def add_task(task):
    new_task = Task(task)
    new_task.save()
    print("Task added successfully!")

def view_tasks():
    tasks = TaskList.get_all()
    if tasks:
        print("Your to-do list:")
        for task in tasks:
            status = "✓" if task[2] else " "
            print(f"{task[0]}. [{status}] {task[1]}")
    else:
        print("Your to-do list is empty.")

def mark_complete(task_id):
    TaskList.mark_complete(task_id)
    print("Task marked as complete!")

def delete_task(task_id):
    TaskList.delete_task(task_id)
    print("Task deleted successfully!")

def main():
    setup_database()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter the task ID to mark as complete: "))
            mark_complete(task_id)
        elif choice == "4":
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
