import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()


cursor.execute(
    """
    SELECT
        bank,
        liability_type,
        name,
        COUNT(*)

    FROM liabilities

    GROUP BY
        bank,
        liability_type,
        name

    HAVING COUNT(*) > 1
    """
)


rows = cursor.fetchall()


print("ДУБЛИ:")

for row in rows:
    print(row)


conn.close()