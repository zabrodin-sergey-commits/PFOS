import sqlite3


DB_PATH = "database/pfos.db"



def save_operations(
        operations,
        account="",
        bank=""):


    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    for operation in operations:


        cursor.execute(
            """
            INSERT INTO operations
            (
            date,
            description,
            amount,
            currency,
            direction,
            counterparty,
            account,
            bank
            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (
                operation.date,
                operation.description,
                operation.amount,
                operation.currency,
                operation.direction,
                operation.counterparty,
                account,
                bank
            )
        )


    connection.commit()

    connection.close()