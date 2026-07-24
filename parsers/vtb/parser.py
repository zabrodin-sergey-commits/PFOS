import re

from models.statement import FinancialStatement
from models.operation import Operation

from parsers.vtb.loan_parser import parse_loan


class VTBParser:

    name = "VTBParser"


    def can_parse(self, text: str) -> bool:

        text = text.lower()

        return (
            "втб" in text
            or "банк втб" in text
        )


    def parse(self, document):

        text = document.text

        statement = FinancialStatement()

        statement.bank = "ВТБ"


        # ---------------------------------------------
        # Кредит
        # ---------------------------------------------

        if self.is_credit_document(text):

            loan_data = parse_loan(text)

            statement.document_type = "Кредит"

            statement.operations = []

            statement.loan = loan_data["loan"]

            statement.loan_summary = {
                "issued": loan_data["issued"],
                "principal_paid": loan_data["principal_paid"],
                "interest_paid": loan_data["interest_paid"],
                "balance": loan_data["balance"],
            }

            return statement


        # ---------------------------------------------
        # Обычная выписка
        # ---------------------------------------------

        statement.document_type = "Выписка"

        statement.operations = self.extract_operations(text)

        return statement



    def is_credit_document(self, text):

        lower = text.lower()

        return (
            "выдача кредита" in lower
            or "погашение кредита" in lower
            or "погашение процентов" in lower
        )



    def extract_operations(self, text):

        operations = []


        pattern = re.compile(
            r"(\d{2}\.\d{2}\.\d{4}).*?"
            r"(-?[0-9\s\xa0,\.]+)\s*RUB.*?"
            r"(Переводы через СБП|Оплата товаров и услуг|Зачисление перевода)",
            re.DOTALL,
        )


        for date, amount, description in pattern.findall(text):

            amount = (
                amount
                .replace("\xa0", "")
                .replace(" ", "")
                .replace(",", ".")
            )


            try:
                amount = float(amount)

            except Exception:
                continue


            operation = Operation()

            operation.date = date
            operation.amount = abs(amount)
            operation.description = description


            if amount >= 0:
                operation.type = "income"
            else:
                operation.type = "expense"


            operations.append(operation)


        return operations