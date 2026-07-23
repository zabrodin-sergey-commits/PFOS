def normalize_operation(operation):
    """
    Определение категории и признака перевода
    """

    text = ""

    if operation.description:
        text += operation.description.lower()

    if hasattr(operation, "counterparty") and operation.counterparty:
        text += " " + operation.counterparty.lower()

    category = "Прочее"
    is_transfer = False

    # Переводы
    if (
        "перевод" in text
        or "сбп" in text
        or "перечисление" in text
    ):
        category = "Переводы"
        is_transfer = True

    # Наличные
    elif (
        "банкомат" in text
        or "снятие наличных" in text
        or "cash" in text
    ):
        category = "Наличные"

    # Покупки
    elif (
        "оплата товаров" in text
        or "wb*" in text
        or "wildberries" in text
        or "магазин" in text
    ):
        category = "Покупки"

    # Услуги
    elif (
        "оплата услуг" in text
        or "услуг коммерческих" in text
        or "сервис" in text
    ):
        category = "Услуги"

    operation.category = category
    operation.is_transfer = is_transfer

    return operation