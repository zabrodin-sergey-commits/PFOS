import re


def normalize_description(text: str) -> str:

    if not text:
        return ""

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    text = text.replace("Aviapa rk", "Aviapark")

    text = text.replace("ELEKTROI NSTR", "ELEKTROINSTR")

    text = text.replace("ISTORICH ESKIY", "ISTORICHESKIY")

    text = text.replace("MAGNIT MM", "MAGNIT")

    text = text.replace("Оплата товаров и услуг.", "")

    text = text.replace("Операция зачисления .", "")

    return text.strip()