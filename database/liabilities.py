import sqlite3

DATABASE = "database/pfos.db"


def get_connection():
    return sqlite3.connect(DATABASE)


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

            UNIQUE
            (
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


def add_liability(
    bank,
    liability_type,
    name,
    owner,
    balance,
    monthly_payment=0,
    end_date=None,
    asset=None,
    purpose=None,
    status="active"
):

    init_liabilities_table()

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
            purpose,
            status
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?
        )

        ON CONFLICT
        (
            bank,
            liability_type,
            name,
            owner
        )

        DO UPDATE SET

            balance=excluded.balance,

            monthly_payment=excluded.monthly_payment,

            end_date=excluded.end_date,

            asset=excluded.asset,

            purpose=excluded.purpose,

            status=excluded.status
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
            purpose,
            status
        )
    )

    conn.commit()
    conn.close()


def get_liabilities():

    init_liabilities_table()

    conn = get_connection()

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM liabilities
        WHERE status='active'
        ORDER BY balance DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def total_liabilities():

    loans = get_liabilities()

    return sum(loan["balance"] for loan in loans)