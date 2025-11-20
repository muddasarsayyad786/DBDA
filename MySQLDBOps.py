import mysql.connector
from mysql.connector import Error


def connect_db(username, password, dbname):
    con = None
    try:
        con = mysql.connector.connect(user=username,
                                      password=password,
                                      host='localhost',
                                      database=dbname,
                                      port=3306)
        print('Connection successful')
    except Error as er:
        print(er)
    return con


def execute_query(conn, query, p_data=None):
    try:
        cursor = conn.cursor()
        if p_data is None:
            cursor.execute(query)
            conn.commit()
            print(f'{cursor.rowcount} rows updated')
        else:
            cursor.execute(query, p_data)
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


insert_data = """insert into student values(4, 'Jay', 'P');"""
select_data = """select * from student;"""
insert_data_p = """insert into student values(%s,%s,%s);"""
data = (5, 'Amol', 'S')
connection = connect_db('root', 'root', 'college')
print('------Original Data-------')
records = execute_read_query(connection, select_data)
for record in records:
    print(record)

execute_query(connection, insert_data)
# Parameterized query
execute_query(connection, insert_data_p, p_data=data)
print('----------after insert--------')
records = execute_read_query(connection, select_data)
for record in records:
    print(record)
