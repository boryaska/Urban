import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    return rows

# def add_user(username, email, age):
#     cursor.execute(f'''
#     INSERT INTO Users VALUES('{username}', '{email}', {age}, 1000)
#     ''')

def add_user(username, email, age):
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))
    connection.commit()

def is_included(username):
    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    connection.commit()
    return cursor.fetchone() is not None



connection.commit()
# connection.close()