import sqlite3


DATABASE = "database/pfos.db"


def _sum_assets(cursor):

    cursor.execute(
        """
        SELECT
            COALESCE(SUM(value), 0)
        FROM assets
        WHERE status='active'
        """
    )

    result = cursor.fetchone()

    return float(result[0] or 0)


def _sum_liabilities(cursor):

    cursor.execute(
        """
        SELECT
            COALESCE(SUM(balance), 0)
        FROM liabilities
        WHERE status='active'
        """
    )

    result = cursor.fetchone()

    return float(result[0] or 0)


def calculate_net_worth():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    assets = _sum_assets(cursor)

    liabilities = _sum_liabilities(cursor)

    conn.close()

    return {
        "assets": assets,
        "liabilities": liabilities,
        "net_worth": assets - liabilities
    }


if __name__ == "__main__":

    result = calculate_net_worth()

    print()

    print("==============================")
    print(" PFOS NET WORTH")
    print("==============================")

    print()

    print(f"Активы        : {result['assets']:,.2f} RUB")
    print(f"Обязательства : {result['liabilities']:,.2f} RUB")

    print("--------------------------------")

    print(f"Чистый капитал: {result['net_worth']:,.2f} RUB")

    print()