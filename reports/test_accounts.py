from database.accounts import (
    init_accounts_table,
    clear_accounts,
    create_account,
    get_accounts
)



print("=" * 50)
print("PFOS ACCOUNTS RESET TEST")
print("=" * 50)



init_accounts_table()


clear_accounts()



accounts = [

    (
        "ВТБ",
        "Зарплатный счёт",
        "Сергей",
        "income",
        "Основная зарплата"
    ),


    (
        "Сбербанк",
        "Дебетовая карта",
        "Сергей",
        "income",
        "Доход такси"
    ),


    (
        "Озон банк",
        "Накопительный",
        "Сергей",
        "savings",
        "Резерв семьи"
    ),


    (
        "Озон банк",
        "Дебетовый",
        "Сергей",
        "spending",
        "Повседневные расходы"
    ),


    (
        "Россельхозбанк",
        "Ипотека Дагомыс",
        "Семья",
        "mortgage",
        "Ипотека квартиры"
    )

]



for account in accounts:

    create_account(
        *account
    )



print()

print("=" * 50)
print("PFOS ACCOUNTS")
print("=" * 50)



for account in get_accounts():

    print(account)