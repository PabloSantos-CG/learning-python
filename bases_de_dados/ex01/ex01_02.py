import sqlite3
from ex01 import TABLE_NAME, DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for user in cursor.fetchall():
    _id, name, weigth = user
    print(f'{_id=}, {name=}, {weigth=}')

cursor.close()
connection.close()