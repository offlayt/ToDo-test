import sqlite3


def create_todo():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Not Started'
        )''')

    connection.commit()
    connection.close()


def add_task(title, description):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
    ''', (title, description))

    connection.commit()
    connection.close()


def all_tasks():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    connection.close()
    return tasks