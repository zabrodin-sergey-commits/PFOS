import sqlite3

DATABASE = "database/pfos.db"


def report():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            bank,
            account_name,
            balance
        FROM accounts
        ORDER BY bank, account_name
    """)

    print()
    print("=" * 40)
    print("ACCOUNT BALANCES")
    print("=" * 40)

    total = 0

    for row in cursor.fetchall():

        print(
            f"{row['bank']:<20}"
            f"{row['account_name']:<25}"
            f"{row['balance']:>15,.2f}"
        )

        total += row["balance"]

    print("-" * 40)

    print(f"ИТОГО: {total:,.2f} RUB")

    conn.close()


if __name__ == "__main__":
    report()