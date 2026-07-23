import re


def find_period(text: str) -> str:
    """
    Ищет период выписки.
    Например:
    01.01.2026 - 31.05.2026
    """

    pattern = r"\d{2}\.\d{2}\.\d{4}\s*[-–]\s*\d{2}\.\d{2}\.\d{4}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""