import sqlite3
from pathlib import Path
from datetime import datetime


DB_PATH = Path("database/pfos.db")



def get_connection():
    return sqlite3.connect(DB_PATH)





def init_balances_table():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS account_balances
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            account_id INTEGER NOT NULL,

            balance REAL NOT NULL DEFAULT 0,

            currency TEXT DEFAULT 'RUB',

            updated TEXT NOT NULL,

            source TEXT
        )
        """
    )


    conn.commit()
    conn.close()





def clear_balances():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM account_balances"
    )

    conn.commit()
    conn.close()





def set_balance(
        account_id,
        balance,
        source="manual"
):

    conn = get_connection()
    cursor = conn.cursor()


    now = datetime.now().strftime(
        "%Y-%m-%d"
    )


    cursor.execute(
        """
        INSERT INTO account_balances
        (
            account_id,
            balance,
            updated,
            source
        )

        VALUES
        (
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            account_id,
            balance,
            now,
            source
        )
    )


    conn.commit()
    conn.close()





def get_balances():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

        ab.account_id,
        a.bank,
        a.name,
        ab.balance,
        ab.updated,
        ab.source


        FROM account_balances ab


        JOIN accounts a

        ON a.id = ab.account_id


        ORDER BY a.id
        """
    )


    rows = cursor.fetchall()

    conn.close()


    return rows





def total_balance():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        COALESCE(
            SUM(balance),
            0
        )

        FROM account_balances
        """
    )


    result = cursor.fetchone()[0]


    conn.close()


    return result