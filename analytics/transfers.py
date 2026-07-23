from datetime import datetime


def parse_date(value):

    return datetime.strptime(
        value,
        "%d.%m.%Y"
    ).date()



def text_of_operation(op):

    return (
        str(getattr(op, "description", ""))
        + " "
        + str(getattr(op, "category", ""))
        + " "
        + str(getattr(op, "counterparty", ""))
    ).lower()



def is_transfer_out(op):

    text = text_of_operation(op)

    if getattr(op, "direction", "") != "OUT":
        return False


    keywords = [
        "перевод",
        "сбп",
        "перечис",
        "платеж"
    ]


    return any(
        k in text
        for k in keywords
    )



def is_income(op):

    return getattr(op, "direction", "") == "IN"



def close_amount(a, b):

    diff = abs(
        abs(a)-abs(b)
    )


    avg = (
        abs(a)+abs(b)
    )/2


    if avg == 0:
        return False


    percent = diff / avg


    # допускаем банковскую комиссию
    return (
        diff <= 300
        or percent <= 0.01
    )



def mark_internal_transfers(operations):


    for op in operations:

        op.internal_transfer = False



    for out_op in operations:


        if not is_transfer_out(out_op):

            continue



        try:

            out_date = parse_date(
                out_op.date
            )

        except Exception:

            continue



        for in_op in operations:


            if out_op is in_op:
                continue


            if not is_income(in_op):
                continue



            try:

                in_date = parse_date(
                    in_op.date
                )

            except Exception:

                continue



            days = abs(
                (out_date-in_date).days
            )


            if days > 1:

                continue



            if not close_amount(
                out_op.amount,
                in_op.amount
            ):

                continue



            out_op.internal_transfer = True
            in_op.internal_transfer = True



    return operations



def remove_internal_transfers(operations):

    return mark_internal_transfers(
        operations
    )