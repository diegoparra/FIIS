# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE ativos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    one VARCHAR(10) NOT NULL,
    three VARCHAR(10) NOT NULL,
    six VARCHAR(10) NOT NULL,
    twelve VARCHAR(10) NOT NULL); """)
conn.close()