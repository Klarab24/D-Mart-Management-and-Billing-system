import mysql.connector as mysql

def connect():
    conn = mysql.connect(host="localhost", user="root", passwd="root", database="d_mart")
    cursor = conn.cursor()
    return conn, cursor

def close(conn, cursor):
    cursor.close()
    conn.close()

def commit(conn):
    conn.commit()

def main()