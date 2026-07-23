import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()



cursor.execute(
    """
    SELECT
        account_id,
        COUNT(*)

    FROM operations

    GROUP BY account_id

    ORDER BY account_id
    """
)


print(
    "Операции по счетам:"
)


for row in cursor.fetchall():

    print(row)



print()


cursor.execute(
    """
    SELECT
        COUNT(*)

    FROM operations

    WHERE account_id IS NULL
    """
)


print(
    "Без привязки:",
    cursor.fetchone()[0]
)


conn.close()