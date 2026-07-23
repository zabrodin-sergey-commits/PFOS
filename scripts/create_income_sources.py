import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS income_sources
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation_id INTEGER,
        source TEXT,
        confidence REAL DEFAULT 1.0
    )
    """
)


conn.commit()

conn.close()


print("income_sources создана")