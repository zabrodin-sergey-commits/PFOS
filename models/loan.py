class Loan:

    def __init__(
        self,
        loan_type=None,
        contract_number=None,
        balance=0.0,
        monthly_payment=0.0,
        rate=0.0,
        end_date=None,
        bank=None,
        account=None,
        borrower=None,
        currency="RUB",
        document_id=None
    ):

        self.loan_type = loan_type
        self.contract_number = contract_number

        self.balance = float(balance) if balance is not None else 0.0
        self.monthly_payment = (
            float(monthly_payment)
            if monthly_payment is not None
            else 0.0
        )

        self.rate = float(rate) if rate is not None else 0.0

        self.end_date = end_date

        self.bank = bank
        self.account = account
        self.borrower = borrower

        self.currency = currency

        self.document_id = document_id

    def __repr__(self):

        return (
            f"{self.loan_type} | "
            f"остаток: {self.balance:.2f} {self.currency} | "
            f"платеж: {self.monthly_payment:.2f} {self.currency} | "
            f"ставка: {self.rate:.2f}% | "
            f"до: {self.end_date}"
        )

    def to_dict(self):

        return {
            "loan_type": self.loan_type,
            "contract_number": self.contract_number,
            "balance": self.balance,
            "monthly_payment": self.monthly_payment,
            "rate": self.rate,
            "end_date": self.end_date,
            "bank": self.bank,
            "account": self.account,
            "borrower": self.borrower,
            "currency": self.currency,
            "document_id": self.document_id,
        }