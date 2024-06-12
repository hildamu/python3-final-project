import sqlite3

def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (task text, completed integer)''')
    conn.commit()
    conn.close()