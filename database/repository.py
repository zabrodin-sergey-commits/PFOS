import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")



def get_connection():

    return sqlite3.connect(DB_PATH)





def save_operations(operations, document_id=None):

    conn = get_connection()
    cursor = conn.cursor()


    for op in operations:

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM operations
            WHERE
                date = ?
                AND description = ?
                AND amount = ?
                AND direction = ?
                AND document_id = ?
            """,
            (
                op.date,
                op.description,
                op.amount,
                op.direction,
                document_id,
            )
        )


        if cursor.fetchone()[0]:
            continue



        cursor.execute(
            """
            INSERT INTO operations
            (
                date,
                description,
                amount,
                currency,
                direction,
                bank,
                account,
                counterparty,
                category,
                document_id,
                is_transfer,
                internal_transfer
            )
            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,?,?
            )
            """,
            (
                op.date,
                op.description,
                op.amount,
                getattr(op, "currency", "RUB"),
                op.direction,
                getattr(op, "bank", None),
                getattr(op, "account", None),
                getattr(op, "counterparty", None),
                getattr(op, "category", "Не определено"),
                document_id,
                1 if getattr(op, "is_transfer", False) else 0,
                1 if getattr(op, "internal_transfer", False) else 0,
            )
        )


    conn.commit()
    conn.close()





def clear_operations():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM operations"
    )

    conn.commit()

    conn.close()





def _row_to_operation(row):

    from models.operation import Operation


    (
        date,
        description,
        amount,
        direction,
        bank,
        category,
        is_transfer,
        internal_transfer
    ) = row



    op = Operation(
        date,
        description,
        amount,
        direction
    )


    op.bank = bank
    op.category = category
    op.is_transfer = bool(is_transfer)
    op.internal_transfer = bool(internal_transfer)


    return op






def get_all_operations():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            date,
            description,
            amount,
            direction,
            bank,
            category,
            is_transfer,
            internal_transfer

        FROM operations

        ORDER BY
            substr(date,7,4),
            substr(date,4,2),
            substr(date,1,2)
        """
    )


    rows = cursor.fetchall()


    conn.close()


    return [
        _row_to_operation(row)
        for row in rows
    ]






def get_operations_by_month(month):

    year, mon = month.split("-")


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            date,
            description,
            amount,
            direction,
            bank,
            category,
            is_transfer,
            internal_transfer

        FROM operations

        WHERE
            substr(date,7,4)=?
            AND substr(date,4,2)=?

        ORDER BY
            substr(date,7,4),
            substr(date,4,2),
            substr(date,1,2)

        """,
        (
            year,
            mon
        )
    )


    rows = cursor.fetchall()


    conn.close()


    return [
        _row_to_operation(row)
        for row in rows
    ]






def get_operations_by_document(document_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            date,
            description,
            amount,
            direction,
            bank,
            category,
            is_transfer,
            internal_transfer

        FROM operations

        WHERE document_id = ?

        ORDER BY
            substr(date,7,4),
            substr(date,4,2),
            substr(date,1,2)

        """,
        (
            document_id,
        )
    )


    rows = cursor.fetchall()


    conn.close()


    return [
        _row_to_operation(row)
        for row in rows
    ]