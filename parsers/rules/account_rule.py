import re


def find_account(text: str) -> str:
    """
    Поиск банковского счета.

    Поддерживает:
    40817810219564019461
    40817 810 5 3600 0176644
    40817 8105 3600 0176644
    """

    # вариант без пробелов
    match = re.search(
        r"\b\d{20}\b",
        text
    )

    if match:
        return match.group()


    # вариант с пробелами
    match = re.search(
        r"\b\d{5}\s+\d{3,5}\s+\d\s+\d{4}\s+\d{6,7}\b",
        text
    )

    if match:

        return (
            match.group()
            .replace(" ", "")
        )


    # запасной вариант:
    # ищем любую последовательность цифр
    # после слов "Номер счета", "Счет"
    patterns = [
        r"Номер счета\s*[\r\n ]+([\d\s]{20,})",
        r"Счет\s*[\r\n ]+([\d\s]{20,})",
        r"счета\s*[\r\n ]+([\d\s]{20,})",
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            value = (
                match.group(1)
                .replace(" ", "")
                .replace("\n", "")
                .replace("\r", "")
            )


            digits = re.search(
                r"\d{20}",
                value
            )

            if digits:
                return digits.group()


    return ""