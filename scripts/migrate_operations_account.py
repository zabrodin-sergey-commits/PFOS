import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")


def main():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    cursor.execute(
        "PRAGMA table_info(operations)"
    )

    columns = [
        row[1]
        for row in cursor.fetchall()
    ]


    if "account_id" not in columns:

        cursor.execute(
            """
            ALTER TABLE operations
            ADD COLUMN account_id INTEGER
            """
        )

        print(
            "Поле account_id добавлено"
        )

    else:

        print(
            "Поле account_id уже существует"
        )


    conn.commit()
    conn.close()



if __name__ == "__main__":
    main()