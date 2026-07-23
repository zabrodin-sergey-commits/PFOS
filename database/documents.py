import sqlite3


DB_PATH = "database/pfos.db"


def init_documents_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id TEXT UNIQUE,
            filename TEXT,
            bank TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def document_exists(document_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM documents
        WHERE document_id = ?
        """,
        (document_id,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_document(document_id, filename, bank):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO documents
        (
            document_id,
            filename,
            bank
        )
        VALUES (?, ?, ?)
        """,
        (
            document_id,
            filename,
            bank
        )
    )

    conn.commit()
    conn.close()