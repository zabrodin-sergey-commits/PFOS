from database.accounts import get_accounts

def report():
    accounts = get_accounts()

    print()
    print("========================================")
    print(" PFOS ACCOUNTS")
    print("========================================")
    print()

    if not accounts:
        print("Счета отсутствуют.")
        return

    total = 0

    for account in accounts:
        print(f"Банк        : {account['bank']}")
        print(f"Владелец    : {account['owner']}")
        print(f"Название    : {account['account_name']}")
        print(f"Тип         : {account['account_type']}")
        print(f"Валюта      : {account['currency']}")
        print(f"Баланс      : {account['balance']:,.2f} RUB")
        print(f"Статус      : {account['status']}")
        print("----------------------------------------")

        total += account["balance"]

    print()
    print("========================================")
    print(f"ВСЕГО НА СЧЕТАХ: {total:,.2f} RUB")
    print("========================================")


if __name__ == "__main__":
    report()