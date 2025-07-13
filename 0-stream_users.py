import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='makgomoshayi',
            password='anie@1245'
        )
        if conn.is_connected():
            print("Connected to MySQL Server")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.execute("USE ALX_prodev")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id VARCHAR(50) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL ,
            
            )
        """)
        conn.commit()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        yield row
    cursor.close()
    conn.close()