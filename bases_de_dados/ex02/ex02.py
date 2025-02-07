import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'customers'
connection = pymysql.connect(
    host=os.environ['HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL)'
        )
    with connection.cursor() as cursor:
        sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        data = ("Fulano", 110)
        cursor.execute(sql, data)
    connection.commit()

