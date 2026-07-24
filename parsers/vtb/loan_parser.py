import re

from models.loan import Loan


def _money(value: str) -> float:
    value = value.replace("\xa0", "")
    value = value.replace(" ", "")
    value = value.replace(",", ".")

    m = re.search(r"(-?\d+(?:\.\d+)?)", value)

    if not m:
        return 0.0

    return float(m.group(1))


def parse_loan(text: str):

    loan = Loan()

    loan.bank = "ВТБ"

    # -------------------------------------------------------
    # Номер договора
    # -------------------------------------------------------

    m = re.search(
        r"(?:Договор|Цессия)\s*№?\s*([0-9/\-]+)",
        text,
        re.IGNORECASE,
    )

    if m:
        loan.contract_number = m.group(1)

    # -------------------------------------------------------
    # Счет списания
    # -------------------------------------------------------

    m = re.search(
        r"Счет списания\s*([0-9*]{10,30})",
        text,
        re.IGNORECASE,
    )

    if m:
        loan.account = m.group(1)

    # -------------------------------------------------------
    # Определяем тип кредита
    # -------------------------------------------------------

    lower = text.lower()

    if "авто" in lower:
        loan.loan_type = "Автокредит"

    elif "ипотек" in lower:
        loan.loan_type = "Ипотека"

    else:
        loan.loan_type = "Кредит"

    # -------------------------------------------------------
    # Выдача кредита
    # -------------------------------------------------------

    issued = 0.0

    m = re.search(
        r"([0-9\s\xa0,\.]+)\s*RUB\s*Выдача кредита",
        text,
        re.IGNORECASE,
    )

    if m:
        issued = _money(m.group(1))

    # -------------------------------------------------------
    # Погашение основного долга
    # -------------------------------------------------------

    principal = 0.0

    for amount in re.findall(
        r"(-?[0-9\s\xa0,\.]+)\s*RUB\s*Погашение кредита",
        text,
        re.IGNORECASE,
    ):
        principal += abs(_money(amount))

    # -------------------------------------------------------
    # Погашение процентов
    # -------------------------------------------------------

    interests = 0.0

    for amount in re.findall(
        r"(-?[0-9\s\xa0,\.]+)\s*RUB\s*Погашение процентов",
        text,
        re.IGNORECASE,
    ):
        interests += abs(_money(amount))

    # -------------------------------------------------------
    # Остаток кредита
    # -------------------------------------------------------

    loan.balance = max(
        0.0,
        round(issued - principal, 2),
    )

    loan.monthly_payment = 0.0
    loan.rate = 0.0
    loan.end_date = None

    return {
        "loan": loan,
        "issued": round(issued, 2),
        "principal_paid": round(principal, 2),
        "interest_paid": round(interests, 2),
        "balance": round(loan.balance, 2),
    }