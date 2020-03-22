import sqlite3

from user import User


def find_by_username(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    query = 'SELECT * from user WHERE username = ?'
    result = cursor.execute(query, (username,))

    row = result.fetchone()

    if row:
        user = User(*row)
    else:
        user = None

    connection.close()

    return user


def find_by_id(_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    query = 'SELECT * from user WHERE id = ?'
    result = cursor.execute(query, (_id,))

    row = result.fetchone()

    if row:
        user = User(*row)
    else:
        user = None

    connection.close()

    return user
