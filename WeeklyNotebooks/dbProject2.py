import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="128.198.162.191",
        user="infscompany",
        password='yeadata',
        database='company'
    )
    return conn