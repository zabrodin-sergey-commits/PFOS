import sqlite3

DATABASE = "database/pfos.db"


class AccountSynchronizer:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def synchronize(self):

        print("=" * 50)
        print("ACCOUNT SYNCHRONIZER")
        print("=" * 50)

        self.cursor.execute("""
            SELECT id
            FROM accounts
        """)

        accounts = self.cursor.fetchall()

        updated = 0

        for account in accounts:

            account_id = account["id"]

            self.cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(
                            CASE
                                WHEN direction='IN'
                                THEN amount
                                ELSE -amount
                            END
                        ),
                    0)
                FROM operations
                WHERE account_id=?
            """, (account_id,))

            balance = self.cursor.fetchone()[0]

            self.cursor.execute("""
                UPDATE accounts
                SET balance=?
                WHERE id=?
            """, (balance, account_id))

            updated += 1

        self.conn.commit()

        print(f"Обновлено счетов : {updated}")

        print("=" * 50)

        self.conn.close()


if __name__ == "__main__":
    AccountSynchronizer().synchronize()