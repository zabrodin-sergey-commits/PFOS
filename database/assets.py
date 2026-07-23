import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")


def get_connection():
    return sqlite3.connect(DB_PATH)



def init_assets_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assets
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            asset_type TEXT NOT NULL,

            owner TEXT,

            value REAL NOT NULL,

            currency TEXT DEFAULT 'RUB',

            description TEXT,

            linked_liability_id INTEGER,

            status TEXT DEFAULT 'active'
        )
        """
    )


    conn.commit()
    conn.close()



def clear_assets():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM assets"
    )

    conn.commit()
    conn.close()



def add_asset(
        name,
        asset_type,
        owner,
        value,
        description=None,
        linked_liability_id=None
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO assets
        (
            name,
            asset_type,
            owner,
            value,
            description,
            linked_liability_id
        )

        VALUES
        (?,?,?,?,?,?)
        """,
        (
            name,
            asset_type,
            owner,
            value,
            description,
            linked_liability_id
        )
    )


    conn.commit()
    conn.close()



def get_assets():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            id,
            name,
            asset_type,
            owner,
            value,
            description,
            linked_liability_id,
            status

        FROM assets

        ORDER BY value DESC
        """
    )


    rows = cursor.fetchall()

    conn.close()


    return rows



def total_assets():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        COALESCE(SUM(value),0)

        FROM assets

        WHERE status='active'
        """
    )


    result = cursor.fetchone()[0]


    conn.close()


    return result