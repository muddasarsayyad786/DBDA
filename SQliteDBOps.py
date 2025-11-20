import sqlite3
from sqlite3 import Error


def connect_db(path):
    con = None
    try:
        con = sqlite3.connect(path)
        print('Connection successful')
    except Error as er:
        print(er)
    return con


def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print('Query executed successfully')
    except Error as er:
        print(er)


def execute_read_query(conn, query):
    results = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as er:
        print(er)
    return results


def close_connection(conn):
    try:
        if conn:
            conn.close()
            print('Connection closed')
    except Error as er:
        print(er)


create_table = """CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT);"""

add_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
fetch_users = """SELECT * from users;"""

update_user = """
UPDATE 
    users
SET
    age = 22
WHERE 
    name = 'Mike'
"""

delete_user = """
DELETE from users WHERE id = 5"""

select_females = """SELECT name, age, nationality
FROM users WHERE gender = 'female'"""


path = "E:\\DBDA_Python_Sept25\\DB\\User.sqlite3"

connection = connect_db(path)
execute_query(connection, create_table)
execute_query(connection, add_users)

records = execute_read_query(connection, fetch_users)
for record in records:
    print(record)

execute_query(connection, update_user)
records = execute_read_query(connection, fetch_users)
for record in records:
    print(record)

execute_query(connection, delete_user)
records = execute_read_query(connection, select_females)
for record in records:
    print(record)