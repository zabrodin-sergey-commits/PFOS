def normalize_operation(operation):
    """
    Нормализация финансовой операции PFOS.

    Определяет:
    - категорию операции
    - является ли операция переводом
    """

    text = (
        operation.description
        or ""
    ).lower()


    # По умолчанию

    operation.category = "Прочее"

    operation.is_transfer = False



    # Наличные

    if "банкомат" in text:

        operation.category = "Наличные"



    # Покупки

    elif (
        "оплата товаров" in text
        or "wb*" in text
        or "wildberries" in text
    ):

        operation.category = "Покупки"



    # Услуги

    elif "оплата услуг" in text:

        operation.category = "Услуги"



    # Переводы

    elif (
        "сбп" in text
        or "перевод" in text
    ):

        operation.category = "Переводы"

        operation.is_transfer = True



    return operation