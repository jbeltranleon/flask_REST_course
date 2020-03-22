import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# Create Table
create_table = 'CREATE TABLE IF NOT EXISTS user (id int, username text, password text)'
cursor.execute(create_table)


insert_query = 'INSERT INTO user VALUES (?, ?, ?)'

# Add row
user = (1, 'jhon', '123')
cursor.execute(insert_query, user)

# Add multiple
users = [
    (2, 'fredy', 'qwe'),
    (3, 'pau', 'asd'),
    (4, 'polly', 'cvb'),
]
cursor.executemany(insert_query, users)
# Save
connection.commit()

# Select
select_query = 'SELECT * FROM user'

for row in cursor.execute(select_query):
    print(row)

connection.close()
