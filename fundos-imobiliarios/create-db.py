import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE ativos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    one VARCHAR(10),
    three VARCHAR(10),
    six VARCHAR(10),
    twelve VARCHAR(10)); """)
conn.close()