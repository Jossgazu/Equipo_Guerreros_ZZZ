import sqlite3
conn = sqlite3.connect ('pedidos.db')
conn = sqlite3.connect (r'c/users/namar/documents/ucsm/lab8/orders.db')
conn = sqlite3.connect ('c/')
cur = conn.cursor ()
cur.execute ("SELECT * FROM estudiantes")
