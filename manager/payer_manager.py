import sqlite3

from payer import Payer


def find_by_id(_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    query = 'SELECT * from payer WHERE id = ?'
    result = cursor.execute(query, (_id,))

    row = result.fetchone()

    if row:
        payer = Payer(*row)
    else:
        payer = None

    connection.close()

    return payer


def find_all():

    payers = []

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    query = 'SELECT * from payer'

    for row in cursor.execute(query):
        payers.append(Payer(*row))

    connection.close()

    return payers


def create(payer):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    create_payer = 'INSERT INTO payer (id, extra_data) VALUES (?, ?)'
    cursor.execute(create_payer, (payer['payer_id'], payer['extra_data']))
    connection.commit()
    connection.close()


def delete(_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    delete_payer = 'DELETE FROM payer WHERE id=?'
    cursor.execute(delete_payer, (_id,))
    connection.commit()
    connection.close()


def update(_id, extra_data):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    update_payer = 'UPDATE payer SET extra_data = ? WHERE id = ?'
    cursor.execute(update_payer, (extra_data, _id))
    connection.commit()
    connection.close()
