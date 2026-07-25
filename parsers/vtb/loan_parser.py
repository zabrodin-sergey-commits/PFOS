import re

from models.loan import Loan


def _money(value: str) -> float:

    value = (
        value
        .replace("\xa0", "")
        .replace(" ", "")
        .replace(",", ".")
    )

    match = re.search(
        r"\d+(?:\.\d+)?",
        value
    )

    if not match:
        return 0.0

    return float(match.group())


def parse_loan(text: str):

    loan = Loan()

    loan.bank = "ВТБ"


    # -----------------------------
    # Номер договора
    # -----------------------------

    contract = re.search(
        r"(\d{3}/\d{4}-\d{7})",
        text
    )

    if contract:
        loan.contract_number = contract.group(1)


    # -----------------------------
    # Тип кредита
    # -----------------------------

    lower = text.lower()

    if "авто" in lower:
        loan.loan_type = "Автокредит"

    elif "ремонт" in lower:
        loan.loan_type = "Кредит на ремонт"

    elif "ипот" in lower:
        loan.loan_type = "Ипотека"

    else:
        loan.loan_type = "Кредит"


    # -----------------------------
    # Выдача кредита
    # -----------------------------

    issued = 0.0

    issue_match = re.search(
        r"(\d{2}\.\d{2}\.\d{4})\s+"
        r"([\d\s\xa0,]+)\s+RUB\s+"
        r"Выдача кредита",
        text,
        re.DOTALL
    )

    if issue_match:

        issued = _money(
            issue_match.group(2)
        )


    # -----------------------------
    # Тело кредита
    # -----------------------------

    principal = 0.0

    principal_matches = re.findall(
        r"(-?[\d\s\xa0,]+)\s+RUB\s+"
        r"Погашение кредита",
        text
    )

    for value in principal_matches:

        principal += abs(
            _money(value)
        )


    # -----------------------------
    # Проценты
    # -----------------------------

    interest = 0.0

    interest_matches = re.findall(
        r"(-?[\d\s\xa0,]+)\s+RUB\s+"
        r"Погашение процентов",
        text
    )

    for value in interest_matches:

        interest += abs(
            _money(value)
        )


    # -----------------------------
    # Остаток
    # -----------------------------

    balance = round(
        issued - principal,
        2
    )

    if balance < 0:
        balance = 0.0


    loan.balance = balance


    return {

        "loan": loan,

        "issued": round(
            issued,
            2
        ),

        "principal_paid": round(
            principal,
            2
        ),

        "interest_paid": round(
            interest,
            2
        ),

        "balance": balance
    }