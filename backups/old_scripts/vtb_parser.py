import re


def parse_vtb(text):
    data = {}

    patterns = {
        "owner": r"ФИО\s+([А-ЯЁA-Z][^\n]+)",
        "account": r"Счет\s+№?\s*([0-9]{20})",
        "period": r"за период\s+([0-9.\- ]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)

        if match:
            data[key] = match.group(1).strip()
        else:
            data[key] = "Не найдено"

    return data