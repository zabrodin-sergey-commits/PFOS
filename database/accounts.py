import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")



def get_connection():

    return sqlite3.connect(DB_PATH)





def init_accounts_table():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            bank TEXT NOT NULL,

            name TEXT NOT NULL,

            owner TEXT,

            account_type TEXT,

            purpose TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(bank,name,owner)
        )
        """
    )


    conn.commit()
    conn.close()





def create_account(
    bank,
    name,
    owner,
    account_type,
    purpose
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id
        FROM accounts

        WHERE
            bank=?
            AND name=?
            AND owner=?

        """,
        (
            bank,
            name,
            owner
        )
    )


    exists = cursor.fetchone()


    if exists:

        conn.close()

        return exists[0]



    cursor.execute(
        """
        INSERT INTO accounts
        (
            bank,
            name,
            owner,
            account_type,
            purpose
        )

        VALUES
        (?,?,?,?,?)

        """,
        (
            bank,
            name,
            owner,
            account_type,
            purpose
        )
    )


    account_id = cursor.lastrowid


    conn.commit()

    conn.close()


    return account_id





def get_accounts():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

            id,
            bank,
            name,
            owner,
            account_type,
            purpose

        FROM accounts

        ORDER BY id

        """
    )


    rows = cursor.fetchall()


    conn.close()


    return rows





def clear_accounts():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM accounts
        """
    )


    cursor.execute(
        """
        DELETE FROM sqlite_sequence
        WHERE name='accounts'
        """
    )


    conn.commit()

    conn.close()