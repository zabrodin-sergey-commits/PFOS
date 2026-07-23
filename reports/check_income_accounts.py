import sqlite3


conn = sqlite3.connect(
    "database/pfos.db"
)

cursor = conn.cursor()


cursor.execute(
    """
    SELECT
        a.bank,
        a.name,
        COUNT(*)

    FROM operations o

    JOIN accounts a
    ON o.account_id=a.id

    JOIN operation_flow f
    ON o.id=f.operation_id

    WHERE f.flow_type='income'

    GROUP BY
        a.bank,
        a.name
    """
)


for row in cursor.fetchall():
    print(row)


conn.close()