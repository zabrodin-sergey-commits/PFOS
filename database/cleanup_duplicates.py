import sqlite3


DB = "database/pfos.db"


conn = sqlite3.connect(DB)

cursor = conn.cursor()


cursor.execute(
    """
    DELETE FROM liabilities

    WHERE id NOT IN
    (
        SELECT MIN(id)

        FROM liabilities

        GROUP BY
            bank,
            liability_type,
            name,
            owner
    )
    """
)


deleted = cursor.rowcount


conn.commit()

conn.close()


print(
    f"Удалено дублей: {deleted}"
)