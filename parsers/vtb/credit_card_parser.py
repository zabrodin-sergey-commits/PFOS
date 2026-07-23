import re

from models.operation import Operation


def clean_description(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    text = text.replace("Aviapa rk", "Aviapark")
    text = text.replace("ELEKTROI NSTR", "ELEKTROINSTR")
    text = text.replace("ISTORICH ESKIY", "ISTORICHESKIY")

    text = text.strip()

    return text


def parse_credit_card_operations(text: str):
    operations = []

    if "Операции по счёту" not in text:
        return operations

    body = text.split("Операции по счёту", 1)[1]

    pattern = re.compile(
        r"(\d{2}\.\d{2}\.\d{4})\s+"  # дата операции
        r"\d{2}:\d{2}:\d{2}.*?"
        r"\d{2}\.\d{2}\.\d{4}\s+"   # дата обработки
        r"\d{2}:\d{2}:\d{2}.*?"
        r"(-?\d[\d,]*\.\d{2})\s*RUB.*?"  # сумма операции
        r"(Оплата товаров и услуг\.|Операция зачисления\s*\.)"
        r"(.*?)"
        r"(?=\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}|\Z)",
        re.S,
    )

    for m in pattern.finditer(body):
        date = m.group(1)

        amount = float(m.group(2).replace(",", ""))

        operation_type = m.group(3)
        description = m.group(4)

        direction = "IN" if "зачисления" in operation_type else "OUT"

        amount = abs(amount)

        description = clean_description(description)

        operation = Operation(
            date=date,
            description=description,
            amount=amount,
            direction=direction,
        )

        operations.append(operation)

    return operations