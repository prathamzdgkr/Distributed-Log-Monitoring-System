import sqlite3

def connect_db():
    conn = sqlite3.connect("logs.db")
    return conn

def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT,
        level TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()