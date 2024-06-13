import sqlite3

def setup_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS tasks
    ''')
    cursor.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    conn.commit()
    conn.close()

class Task:
    def __init__(self, task, category_id=None, completed=False):
        self.task = task
        self.category_id = category_id
        self.completed = completed

    def save(self):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (task, completed, category_id) VALUES (?, ?, ?)
        ''', (self.task, self.completed, self.category_id))
        conn.commit()
        conn.close()

class Category:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO categories (name) VALUES (?)
        ''', (self.name,))
        conn.commit()
        conn.close()

class TaskList:
    @staticmethod
    def get_all():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT tasks.id, tasks.task, tasks.completed, categories.name
            FROM tasks
            LEFT JOIN categories ON tasks.category_id = categories.id
        ''')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    @staticmethod
    def get_by_id(task_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT tasks.id, tasks.task, tasks.completed, categories.name
            FROM tasks
            LEFT JOIN categories ON tasks.category_id = categories.id
            WHERE tasks.id = ?
        ''', (task_id,))
        task = cursor.fetchone()
        conn.close()
        return task

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

class CategoryList:
    @staticmethod
    def get_all():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM categories')
        categories = cursor.fetchall()
        conn.close()
        return categories

    @staticmethod
    def get_by_id(category_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM categories WHERE id = ?', (category_id,))
        category = cursor.fetchone()
        conn.close()
        return category

def add_task(task, category_id=None):
    new_task = Task(task, category_id)
    new_task.save()
    print("Task added successfully!")

def add_category(name):
    new_category = Category(name)
    new_category.save()
    print("Category added successfully!")

def view_tasks():
    tasks = TaskList.get_all()
    if tasks:
        print("Your to-do list:")
        for task in tasks:
            status = "✓" if task[2] else " "
            category = task[3] if task[3] else "No Category"
            print(f"{task[0]}. [{status}] {task[1]} (Category: {category})")
    else:
        print("Your to-do list is empty.")

def view_task_by_id(task_id):
    task = TaskList.get_by_id(task_id)
    if task:
        status = "✓" if task[2] else " "
        category = task[3] if task[3] else "No Category"
        print(f"Task {task[0]}: [{status}] {task[1]} (Category: {category})")
    else:
        print("Task not found.")

def view_categories():
    categories = CategoryList.get_all()
    if categories:
        print("Categories:")
        for category in categories:
            print(f"{category[0]}. {category[1]}")
    else:
        print("No categories found.")

def view_category_by_id(category_id):
    category = CategoryList.get_by_id(category_id)
    if category:
        print(f"Category {category[0]}: {category[1]}")
    else:
        print("Category not found.")

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
        print("2. Add Category")
        print("3. View Tasks")
        print("4. View Task by ID")
        print("5. View Categories")
        print("6. View Category by ID")
        print("7. Mark Task as Complete")
        print("8. Delete Task")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            category_id = input("Enter the category ID (or leave blank for no category): ")
            category_id = int(category_id) if category_id else None
            add_task(task, category_id)
        elif choice == "2":
            name = input("Enter the category name: ")
            add_category(name)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            task_id = int(input("Enter the task ID to view: "))
            view_task_by_id(task_id)
        elif choice == "5":
            view_categories()
        elif choice == "6":
            category_id = int(input("Enter the category ID to view: "))
            view_category_by_id(category_id)
        elif choice == "7":
            task_id = int(input("Enter the task ID to mark as complete: "))
            mark_complete(task_id)
        elif choice == "8":
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
