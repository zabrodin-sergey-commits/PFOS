from analytics.account_mapper import detect_account


class TestOperation:

    def __init__(
        self,
        bank,
        description=""
    ):
        self.bank = bank
        self.description = description



tests = [

    TestOperation(
        "ВТБ",
        "Заработная плата"
    ),

    TestOperation(
        "Сбербанк",
        "Перевод от такси"
    ),

    TestOperation(
        "Озон банк",
        "Начисление процентов"
    ),

    TestOperation(
        "Озон банк",
        "Покупка"
    )

]


for t in tests:

    print(
        t.bank,
        "-> account_id",
        detect_account(t)
    )