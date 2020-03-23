import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_user = 'CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
cursor.execute(create_user)

create_payer = 'CREATE TABLE IF NOT EXISTS payer (id INTEGER PRIMARY KEY, extra_data TEXT)'
cursor.execute(create_payer)

connection.commit()
connection.close()