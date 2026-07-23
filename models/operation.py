class Operation:
    def __init__(
        self,
        date,
        description,
        amount,
        direction,
        currency="RUB",
        bank=None,
        account=None,
        counterparty=None,
        category="Не определено",
        is_transfer=False,
        document_id=None
    ):
        self.date = date
        self.description = description
        self.amount = float(amount)
        self.currency = currency
        self.direction = direction

        self.bank = bank
        self.account = account
        self.counterparty = counterparty

        self.category = category
        self.is_transfer = is_transfer

        self.document_id = document_id


    def __repr__(self):
        transfer = "TRANSFER" if self.is_transfer else ""

        return (
            f"{self.date} | "
            f"{self.direction} | "
            f"{self.amount} {self.currency} | "
            f"{self.description} | "
            f"{self.category} | "
            f"{transfer}"
        )


    def to_dict(self):
        return {
            "date": self.date,
            "description": self.description,
            "amount": self.amount,
            "currency": self.currency,
            "direction": self.direction,
            "bank": self.bank,
            "account": self.account,
            "counterparty": self.counterparty,
            "category": self.category,
            "is_transfer": self.is_transfer,
            "document_id": self.document_id
        }