import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL, username text PRIMARY KEY, password text, date_joined text)')
cur.execute("INSERT OR IGNORE INTO users VALUES (87, 'user1', '1234', '2022-01-02')")
cur.execute("INSERT OR IGNORE INTO users VALUES (92, 'user3', 'abcd', '2022-02-01')")
con.commit()
con.close()