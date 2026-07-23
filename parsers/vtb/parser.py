from models.statement import FinancialStatement

from parsers.base_parser import BaseParser

from parsers.rules.account_rule import find_account
from parsers.rules.owner_rule import find_owner

from parsers.vtb.operations_parser import parse_operations
from parsers.vtb.credit_card_parser import parse_credit_card_operations


class VTBParser(BaseParser):

    def can_parse(self, text: str):

        text = text.lower()

        keywords = [
            "втб",
            "банк втб",
            "vtb",
            "счёту",
            "счету",
            "кредитная карта",
            "кредитный лимит",
            "номер счёта",
            "номер счета",
        ]

        return any(word in text for word in keywords)

    def is_credit_card(self, text):

        text = text.lower()

        return (
            "кредитная карта" in text
            or "кредитный лимит" in text
            or "общая сумма задолженности" in text
            or "беспроцентный период" in text
        )

    def is_credit_document(self, text):

        text = text.lower()

        return (
            "график платежей" in text
            or "остаток задолженности по кредиту" in text
            or "ежемесячный платеж" in text
            or "сумма кредита" in text
        )

    def parse(self, document):

        text = document.text

        statement = FinancialStatement()

        statement.bank = "ВТБ"
        statement.version = "3"

        statement.account = find_account(text)
        statement.owner = find_owner(text)

        if self.is_credit_card(text):

            statement.document_type = "Кредитная карта"

            statement.operations = parse_credit_card_operations(text)

            return statement

        if self.is_credit_document(text):

            statement.document_type = "Кредит"

            statement.operations = []

            return statement

        statement.document_type = "Выписка по счету"

        statement.operations = parse_operations(text)

        return statement