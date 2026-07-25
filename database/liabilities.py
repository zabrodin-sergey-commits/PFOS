import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")


def get_connection():

    return sqlite3.connect(DB_PATH)



def init_liabilities_table():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS liabilities
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


    conn.commit()

    conn.close()



def clear_liabilities():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM liabilities
        """
    )


    conn.commit()

    conn.close()



def add_liability(
        bank,
        liability_type,
        name,
        owner,
        balance,
        monthly_payment,
        end_date,
        asset,
        purpose
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO liabilities
        (
            bank,
            liability_type,
            name,
            owner,
            balance,
            monthly_payment,
            end_date,
            asset,
            purpose
        )

        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )

        ON CONFLICT(
            bank,
            liability_type,
            name,
            owner
        )

        DO UPDATE SET

            balance = excluded.balance,

            monthly_payment = excluded.monthly_payment,

            end_date = excluded.end_date,

            asset = excluded.asset,

            purpose = excluded.purpose

        """,

        (
            bank,
            liability_type,
            name,
            owner,
            balance,
            monthly_payment,
            end_date,
            asset,
            purpose
        )
    )


    conn.commit()

    conn.close()



def get_liabilities():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

            id,
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

        WHERE status='active'

        ORDER BY balance DESC
        """
    )


    rows = cursor.fetchall()


    conn.close()


    return rows



def total_liabilities():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

        COALESCE(
            SUM(balance),
            0
        )

        FROM liabilities

        WHERE status='active'
        """
    )


    result = cursor.fetchone()[0]


    conn.close()


    return result