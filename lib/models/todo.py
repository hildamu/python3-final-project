# import sqlite3

# def create_table():
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS tasks
#                  (task TEXT, completed INTEGER)''')
#     conn.commit()
#     conn.close()

# def add_task(task):
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
#     conn.commit()
#     conn.close()
#     print(f"Task '{task}' added successfully!")

# def fetch_tasks():
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute("SELECT rowid, task, completed FROM tasks")
#     rows = c.fetchall()
#     conn.close()
#     return rows

# def view_tasks():
#     rows = fetch_tasks()
#     if rows:
#         print("\nYour to-do list:")
#         for index, row in enumerate(rows, start=1):
#             status = "✓" if row[2] else " "
#             print(f"{index}. [{status}] {row[1]}")
#     else:
#         print("\nYour to-do list is empty.")

# def mark_complete(task_index):
#     rows = fetch_tasks()
#     if 0 < task_index <= len(rows):
#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()
#         task_id = rows[task_index - 1][0]
#         c.execute("UPDATE tasks SET completed = 1 WHERE rowid = ?", (task_id,))
#         conn.commit()
#         conn.close()
#         print(f"Task '{rows[task_index - 1][1]}' marked as complete!")
#     else:
#         print("Invalid task index.")

# def delete_task(task_index):
#     rows = fetch_tasks()
#     if 0 < task_index <= len(rows):
#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()
#         task_id = rows[task_index - 1][0]
#         c.execute("DELETE FROM tasks WHERE rowid = ?", (task_id,))
#         conn.commit()
#         conn.close()
#         print(f"Task '{rows[task_index - 1][1]}' deleted successfully!")
#     else:
#         print("Invalid task index.")

# def main():
#     create_table()

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
#             if task.strip():
#                 add_task(task)
#             else:
#                 print("Task cannot be empty.")
#         elif choice == "2":
#             view_tasks()
#         elif choice == "3":
#             try:
#                 task_index = int(input("Enter the task index to mark as complete: "))
#                 mark_complete(task_index)
#             except ValueError:
#                 print("Please enter a valid number.")
#         elif choice == "4":
#             try:
#                 task_index = int(input("Enter the task index to delete: "))
#                 delete_task(task_index)
#             except ValueError:
#                 print("Please enter a valid number.")
#         elif choice == "5":
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
# import sqlite3

# def check_database():
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()

#     # Check if the table exists
#     c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
#     table_exists = c.fetchone()
#     if table_exists:
#         print("The 'tasks' table exists.")
#     else:
#         print("The 'tasks' table does not exist.")
#         conn.close()
#         return

#     # Display the table schema
#     c.execute("PRAGMA table_info(tasks);")
#     columns = c.fetchall()
#     print("Table schema:")
#     for column in columns:
#         print(column)

#     # Display the table contents
#     c.execute("SELECT * FROM tasks")
#     rows = c.fetchall()
#     print("\nTable contents:")
#     for row in rows:
#         print(row)
    
#     conn.close()

# if __name__ == "__main__":
#     check_database()
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

