def detect_account(operation):

    bank = str(
        getattr(operation, "bank", "")
    ).lower()


    description = str(
        getattr(operation, "description", "")
    ).lower()



    # ВТБ зарплата

    if "втб" in bank:

        return 1



    # Сбер такси

    if "сбер" in bank:

        return 2



    # Озон

    if "озон" in bank:

        if (
            "накоп" in description
            or "процент" in description
        ):
            return 3

        return 4



    return None