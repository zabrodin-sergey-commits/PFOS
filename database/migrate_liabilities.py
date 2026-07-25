import sqlite3


DB = "database/pfos.db"


conn = sqlite3.connect(DB)

cursor = conn.cursor()


# новая таблица с защитой от дублей

cursor.execute(
    """
    CREATE TABLE liabilities_new
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        bank TEXT,

        liability_type TEXT,

        name TEXT,

        owner TEXT,

        balance REAL DEFAULT 0,

        monthly_payment REAL DEFAULT 0,

        end_date TEXT,

        asset TEXT,

        purpose TEXT,

        status TEXT DEFAULT 'active',

        UNIQUE(
            bank,
            liability_type,
            name,
            owner
        )
    )
    """
)



# переносим данные

cursor.execute(
    """
    INSERT INTO liabilities_new
    (
        bank,
        liability_type,
        name,
        owner,
        balance,
        monthly_payment,
        end_date,
        asset,
        purpose,
        status
    )

    SELECT

        bank,
        liability_type,
        name,
        owner,
        balance,
        monthly_payment,
        end_date,
        asset,
        purpose,
        status

    FROM liabilities

    GROUP BY
        bank,
        liability_type,
        name,
        owner
    """
)



# удаляем старую

cursor.execute(
    """
    DROP TABLE liabilities
    """
)



# переименовываем новую

cursor.execute(
    """
    ALTER TABLE liabilities_new
    RENAME TO liabilities
    """
)



conn.commit()

conn.close()


print("liabilities migration complete")