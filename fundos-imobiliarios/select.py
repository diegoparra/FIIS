import sqlite3
# conn = sqlite3.connect("app.db")
# cursor = conn.cursor()
# cursor.execute("""
#     SELECT name, one, three, six, twelve FROM ativos ORDER BY id DESC; """)
# parra = cursor.fetchall()

# conn.close()

# print(parra)



conn = sqlite3.connect("app.db")
cursor = conn.cursor()
sql_select_Query = "select name from ativos"
cursor.execute("select name from ativos")
records = cursor.fetchall()
# compare = []
if records == []:
    print({'BRCR11': ['0,55%', '1,43%', '3,01%', '16,77%']})
else:
    for item in records:
        # compare = ''.join(item)
        print(item)
# for row in records:
#         print(row[1])
# # cursor.execute("""
# #     SELECT name FROM ativos; """)
conn.close()
