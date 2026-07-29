import sqlite3

DATABASE = "database/pfos.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_accounts_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        bank TEXT,

        owner TEXT,

        account_name TEXT,

        account_type TEXT,

        currency TEXT DEFAULT 'RUB',

        balance REAL DEFAULT 0,

        status TEXT DEFAULT 'active',

        opened_at TEXT,

        closed_at TEXT,

        UNIQUE(bank, owner, account_name)
    )
    """)

    conn.commit()
    conn.close()


def add_account(
    bank,
    owner,
    account_name,
    account_type,
    currency="RUB",
    balance=0,
    status="active",
    opened_at=None,
    closed_at=None
):
    init_accounts_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO accounts
    (
        bank,
        owner,
        account_name,
        account_type,
        currency,
        balance,
        status,
        opened_at,
        closed_at
    )

    VALUES
    (
        ?,?,?,?,?,?,?,?,?
    )

    ON CONFLICT(bank, owner, account_name)

    DO UPDATE SET

        account_type=excluded.account_type,
        currency=excluded.currency,
        balance=excluded.balance,
        status=excluded.status,
        opened_at=excluded.opened_at,
        closed_at=excluded.closed_at
    """,
    (
        bank,
        owner,
        account_name,
        account_type,
        currency,
        balance,
        status,
        opened_at,
        closed_at
    ))

    conn.commit()
    conn.close()


def get_accounts():
    init_accounts_table()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM accounts
        WHERE status='active'
        ORDER BY bank, account_name
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def update_balance(account_id, balance):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE accounts
        SET balance=?
        WHERE id=?
    """,
    (
        balance,
        account_id
    ))

    conn.commit()
    conn.close()


def find_account(bank, owner, account_name):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM accounts
        WHERE
            bank=?
        AND owner=?
        AND account_name=?
    """,
    (
        bank,
        owner,
        account_name
    ))

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def total_balance():
    accounts = get_accounts()

    return sum(a["balance"] for a in accounts)