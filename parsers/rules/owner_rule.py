import re


STOP_WORDS = [
    "со счета",
    "счета",
    "банковской карты",
    "карты",
    "за период",
    "валюта",
    "номер счета",
]


def clean_owner(text: str) -> str:

    text = " ".join(
        text.split()
    )


    for word in STOP_WORDS:

        position = text.lower().find(
            word.lower()
        )

        if position != -1:

            text = text[:position]


    return text.strip()



def find_owner(text: str) -> str:
    """
    Поиск владельца счёта.
    Поддерживает разные банки.
    """


    patterns = [

        # Владелец счёта
        r"Владелец сч[её]та\s*[\r\n]+([А-ЯЁ][^\n]+)",


        # Владелец:
        r"Владелец[:\s]+([А-ЯЁ][^\n]+)",


        # Клиент
        r"Клиент[:\s]+([А-ЯЁ][^\n]+)",


        # Получатель
        r"Получатель[:\s]+([А-ЯЁ][^\n]+)",


        # ФИО отдельно после блока
        r"(Забродин\s+[А-ЯЁ][^\n]+)",
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.MULTILINE
        )

        if match:

            owner = clean_owner(
                match.group(1)
            )

            if len(owner) > 5:

                return owner


    return ""