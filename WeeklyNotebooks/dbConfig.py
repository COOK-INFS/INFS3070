import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="128.198.162.191",
        user="infsclass",
        password='webclass',
        database='infs3070'
    )
    return conn