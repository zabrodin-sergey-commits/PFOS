from datetime import datetime


TRANSFER_DIFF_LIMIT = 50


def detect_internal_transfers(operations):
    """
    Поиск внутренних переводов.

    Ищет пары:
    OUT перевод
    IN перевод

    близкие по дате и сумме.
    """

    used = set()


    for i, out_op in enumerate(operations):

        if i in used:
            continue


        if getattr(out_op, "direction", None) != "OUT":
            continue


        if not getattr(out_op, "is_transfer", False):
            continue



        for j, in_op in enumerate(operations):

            if j in used:
                continue


            if i == j:
                continue


            if getattr(in_op, "direction", None) != "IN":
                continue


            if not getattr(in_op, "is_transfer", False):
                continue



            if not same_day(
                out_op.date,
                in_op.date
            ):
                continue



            diff = abs(
                float(out_op.amount)
                -
                float(in_op.amount)
            )


            if diff <= TRANSFER_DIFF_LIMIT:

                out_op.internal_transfer = True
                in_op.internal_transfer = True


                used.add(i)
                used.add(j)


                break


    return operations



def same_day(date1, date2):

    try:

        d1 = datetime.strptime(
            date1,
            "%d.%m.%Y"
        )

        d2 = datetime.strptime(
            date2,
            "%d.%m.%Y"
        )


        return d1.date() == d2.date()


    except Exception:

        return False