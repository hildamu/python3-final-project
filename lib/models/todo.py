import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'models', 'todo.db')

conn = sqlite3.connect(DB_PATH)


def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  task TEXT, 
                  completed INTEGER)''')
    conn.commit()
    conn.close()



def add_task(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()
    print("Task added successfully!")

def view_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    if rows:
        print("Your to-do list:")
        for index, row in enumerate(rows, start=1):
            status = "✓" if row[2] else " "
            print(f"{index}. [{status}] {row[1]}")
    else:
        print("Your to-do list is empty.")
    conn.close()

def mark_complete(task_index):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    if 0 < task_index <= len(rows):
        c.execute("UPDATE tasks SET completed = 1 WHERE id =?", (rows[task_index - 1][0],))
        conn.commit()
        print("Task marked as complete!")
    else:
        print("Invalid task index.")
    conn.close()

def delete_task(task_index):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    if 0 < task_index <= len(rows):
        c.execute("DELETE FROM tasks WHERE id =?", (rows[task_index - 1][0],))
        conn.commit()
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")
    conn.close()

def main():
    create_table()

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
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
