import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{str(i)}', f'example{str(i)}@gmail.com', f'{i*10}', '1000'))
#
# for i in range(5):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",
#                    (500, i*2+1))
#
# for i in range(4):
#     cursor.execute("DELETE FROM Users WHERE id = ?",
#                    (i*3+1,))

# cursor.execute('SELECT * FROM users WHERE age != 60')

cursor.execute("DELETE FROM Users WHERE id = ?",
               (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

# rows = cursor.fetchall()
# for row in rows:
#     print(f'Имя: {row[1]} | Почта: {row[2]} | Возраст: {row[3]} | Баланс: {row[4]}')

connection.commit()
connection.close()