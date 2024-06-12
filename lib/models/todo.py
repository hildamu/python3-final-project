import sqlite3

def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (task text, completed integer)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()
    print("Added successfully!") 

def view_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    if rows:
        print("Your to-do list:")
        for index, row in enumerate(rows, start=1):
            status = "✓" if row[1] else " "
            print(f"{index}. [{status}] {row[0]}")
    else:
        print("Your to-do list is empty.")
    conn.close() 

def mark_complete(task_index):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    if 0 < task_index <= len(rows):
        c.execute("UPDATE tasks SET completed = 1 WHERE task =?", (rows[task_index - 1][0],))
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
        c.execute("DELETE FROM tasks WHERE task =?", (rows[task_index - 1][0],))
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


