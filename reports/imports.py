import sqlite3


DB_PATH = "database/pfos.db"



def get_import_history():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            id,
            document_id,
            filename,
            bank,
            created_at
        FROM documents
        ORDER BY created_at DESC
        """
    )


    documents = cursor.fetchall()

    result = []


    for doc in documents:

        (
            doc_id,
            document_id,
            filename,
            bank,
            created_at
        ) = doc



        cursor.execute(
            """
            SELECT
                COUNT(*)
            FROM operations
            WHERE document_id = ?
            """,
            (
                document_id,
            )
        )

        count = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT
                COALESCE(SUM(amount),0)
            FROM operations
            WHERE
                document_id = ?
                AND direction = 'IN'
            """,
            (
                document_id,
            )
        )

        income = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT
                COALESCE(SUM(amount),0)
            FROM operations
            WHERE
                document_id = ?
                AND direction = 'OUT'
                AND is_transfer = 0
            """,
            (
                document_id,
            )
        )

        expense = cursor.fetchone()[0]



        result.append(
            {
                "id": doc_id,
                "document_id": document_id,
                "filename": filename,
                "bank": bank,
                "created_at": created_at,
                "count": count,
                "income": income,
                "expense": expense,
                "balance": income - expense
            }
        )


    conn.close()


    return result