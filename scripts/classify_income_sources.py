import sqlite3


DB = "database/pfos.db"



def detect_source(
    bank,
    account_name,
    description
):

    bank = (bank or "").lower()
    account_name = (account_name or "").lower()
    description = (description or "").lower()



    if (
        "втб" in bank
        and "зарплат" in account_name
    ):

        return "Основная зарплата"



    if (
        "сбер" in bank
        and (
            "дебет" in account_name
            or "такси" in account_name
        )
    ):

        return "Доход такси"



    if (
        "озон" in bank
        and "накоп" in account_name
    ):

        return "Проценты / накопления"



    return "Прочий доход"





def main():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM income_sources
        """
    )



    cursor.execute(
        """
        SELECT

            o.id,

            a.bank,

            a.name,

            o.description


        FROM operations o


        JOIN operation_flow f

        ON o.id = f.operation_id


        LEFT JOIN accounts a

        ON o.account_id = a.id


        WHERE f.flow_type='income'

        """
    )



    rows = cursor.fetchall()



    count = 0



    for row in rows:


        operation_id = row[0]


        source = detect_source(
            row[1],
            row[2],
            row[3]
        )


        cursor.execute(
            """
            INSERT INTO income_sources
            (
                operation_id,
                source
            )

            VALUES
            (?,?)

            """,
            (
                operation_id,
                source
            )
        )


        count += 1



    conn.commit()

    conn.close()



    print(
        f"Источников дохода определено: {count}"
    )



if __name__ == "__main__":

    main()