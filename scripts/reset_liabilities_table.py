import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")


conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()


cursor.execute(
    """
    DROP TABLE IF EXISTS liabilities
    """
)


conn.commit()

conn.close()


print("Таблица liabilities пересоздана")