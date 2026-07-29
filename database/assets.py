import sqlite3

DATABASE = "database/pfos.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_assets_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assets
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            asset_type TEXT,

            name TEXT,

            owner TEXT,

            value REAL DEFAULT 0,

            purchase_price REAL DEFAULT 0,

            purchase_date TEXT,

            status TEXT DEFAULT 'active'
        )
        """
    )

    conn.commit()
    conn.close()


def add_asset(
    asset_type,
    name,
    owner,
    value,
    purchase_price=0,
    purchase_date=None,
    status="active"
):

    init_assets_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO assets
        (
            asset_type,
            name,
            owner,
            value,
            purchase_price,
            purchase_date,
            status
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            asset_type,
            name,
            owner,
            value,
            purchase_price,
            purchase_date,
            status
        )
    )

    conn.commit()
    conn.close()


def get_assets():

    init_assets_table()

    conn = get_connection()

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM assets
        WHERE status='active'
        ORDER BY value DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def total_assets():

    assets = get_assets()

    return sum(asset["value"] for asset in assets)