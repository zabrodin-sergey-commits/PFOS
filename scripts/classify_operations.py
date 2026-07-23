import sqlite3

from analytics.flow_classifier import classify_operation



DB = "database/pfos.db"



def main():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM operation_flow
        """
    )



    cursor.execute(
        """
        SELECT
            id,
            direction,
            internal_transfer

        FROM operations
        """
    )


    rows = cursor.fetchall()



    count = 0



    for row in rows:

        op = type(
            "Operation",
            (),
            {}
        )()


        op.direction = row[1]

        op.internal_transfer = bool(
            row[2]
        )



        flow = classify_operation(
            op
        )



        cursor.execute(
            """
            INSERT INTO operation_flow
            (
                operation_id,
                flow_type
            )
            VALUES
            (?,?)
            """,
            (
                row[0],
                flow
            )
        )


        count += 1



    conn.commit()

    conn.close()



    print(
        f"Классифицировано операций: {count}"
    )



if __name__ == "__main__":

    main()