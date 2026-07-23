import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS operation_flow
    (
        operation_id INTEGER PRIMARY KEY,
        flow_type TEXT,
        comment TEXT
    )
    """
)


conn.commit()
conn.close()


print(
    "operation_flow создана"
)