import sqlite3


DB_PATH = "database/pfos.db"


connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS operations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    date TEXT,

    description TEXT,

    amount REAL,

    currency TEXT,

    direction TEXT,

    counterparty TEXT,

    account TEXT,

    bank TEXT

)
""")


connection.commit()

connection.close()


print("Database initialized")