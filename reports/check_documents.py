import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()


for row in cursor.execute(
    """
    SELECT id,file_name,bank
    FROM documents
    """
):
    print(row)


conn.close()