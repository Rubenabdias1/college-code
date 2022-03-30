import sqlite3

connection = sqlite3.connect('passwd.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS passwds
              (user TEXT, password TEXT, Year INT)''')

connection.commit()
connection.close()