import sqlite3

DATABASE = "database/pfos.db"


def migrate():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("=" * 50)
    print("Migration 004 : Accounts v2")
    print("=" * 50)

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='accounts'
    """)

    if cursor.fetchone() is None:
        print("Таблица accounts отсутствует.")

        cursor.execute("""
        CREATE TABLE accounts
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

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(bank, owner, account_name)
        )
        """)

        conn.commit()
        conn.close()

        print("Accounts создана.")
        return

    cursor.execute("PRAGMA table_info(accounts)")
    columns = [c[1] for c in cursor.fetchall()]

    if "status" in columns:
        print("Accounts уже новой версии.")
        conn.close()
        return

    print("Обнаружена старая структура.")
    print("Выполняется миграция...")

    cursor.execute("ALTER TABLE accounts RENAME TO accounts_old")

    cursor.execute("""
    CREATE TABLE accounts
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

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        UNIQUE(bank, owner, account_name)
    )
    """)

    cursor.execute("""
    INSERT INTO accounts
    (
        bank,
        owner,
        account_name,
        account_type
    )

    SELECT
        bank,
        owner,
        name,
        account_type
    FROM accounts_old
    """)

    cursor.execute("DROP TABLE accounts_old")

    conn.commit()
    conn.close()

    print("Migration completed successfully.")


if __name__ == "__main__":
    migrate()