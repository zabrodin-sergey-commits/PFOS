import re


def clean_description(text: str) -> str:

    if not text:
        return ""

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    text = re.sub(
        r"RUB\s+\d+[.,]\d+\s+RUB\s+\d+[.,]\d+",
        "",
        text,
    )

    text = re.sub(
        r"\d+[.,]\d+",
        "",
        text,
    )

    text = re.sub(
        r"\b\d+\b",
        "",
        text,
    )

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()