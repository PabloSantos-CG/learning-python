import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / "db.sqlite3"
TABLE_NAME = "customer"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)
# cursor.execute(f'DELETE FROM {TABLE_NAME}')
# connection.commit()

if __name__ == "__main__":
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(name, weigth) VALUES (?, ?)'
    )

    data = [
        ["José", 1], ["Beltrano", 2],
        ["Cicrano", 3], ["Fulano.Jr", 4],
        ["Fulano", 5], ["Beltran.Jr", 6],
        ["Jugulano", 7], ["Lidian", 8],
    ]
    cursor.executemany(sql, data)
    connection.commit()

cursor.close()
connection.close()