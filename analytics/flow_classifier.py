def classify_operation(op):

    if getattr(
        op,
        "internal_transfer",
        False
    ):

        return "transfer"



    direction = getattr(
        op,
        "direction",
        ""
    )


    if direction == "IN":

        return "income"



    if direction == "OUT":

        return "expense"



    return "unknown"