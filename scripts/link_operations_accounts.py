import sqlite3
from pathlib import Path


DB_PATH = Path("database/pfos.db")



def detect_account_id(bank, account, description):

    text = (
        str(bank)
        + " "
        + str(account)
        + " "
        + str(description)
    ).lower()


    if "втб" in text:

        return 1


    if "сбер" in text:

        return 2


    if "озон" in text:

        if (
            "накоп" in text
            or "счет" in text
        ):
            return 3

        return 4


    return None





def main():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT
            id,
            bank,
            account,
            description

        FROM operations
        """
    )


    operations = cursor.fetchall()


    linked = 0
    skipped = 0



    for op in operations:

        op_id, bank, account, description = op


        account_id = detect_account_id(
            bank,
            account,
            description
        )


        if account_id:


            cursor.execute(
                """
                UPDATE operations

                SET account_id = ?

                WHERE id = ?
                """,
                (
                    account_id,
                    op_id
                )
            )


            linked += 1


        else:

            skipped += 1



    conn.commit()
    conn.close()



    print(
        "Операции привязаны:",
        linked
    )

    print(
        "Без счета:",
        skipped
    )



if __name__ == "__main__":
    main()