import sqlite3

with sqlite3.connect("time.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Account(
ID INTEGER PRIMARY KEY,
Account VARCHAR(20) NOT NULL,
Mail VARCHAR(20) NOT NULL,
Password VARCHAR(20) NOT NULL);
'''
)

cursor.execute("""
INSERT INTO Account (Account, Mail, Password)
VALUES ("MAn", "makr", "hentai")
""")
db.connect()

cursor