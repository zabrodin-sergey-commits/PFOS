from database.assets import get_assets
from database.accounts import get_accounts



LIQUID_TYPES = [
    "savings",
    "spending",
    "income"
]



def calculate_liquidity():

    accounts = get_accounts()


    total = 0

    details = []


    for account in accounts:

        account_type = account[4]


        if account_type in LIQUID_TYPES:

            details.append(account)

            # пока сумма будет добавляться
            # после подключения остатков счетов



    return {
        "liquid_assets": total,
        "accounts": details
    }




def print_liquidity():

    report = calculate_liquidity()


    print("=" * 60)
    print("PFOS LIQUIDITY")
    print("=" * 60)

    print()

    print(
        "Доступная ликвидность:",
        report["liquid_assets"],
        "RUB"
    )


    print()

    print("Счета:")


    for acc in report["accounts"]:

        print(
            acc
        )