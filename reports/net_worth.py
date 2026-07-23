from database.assets import total_assets
from database.liabilities import get_liabilities



def liabilities_total():

    liabilities = get_liabilities()

    total = 0

    for item in liabilities:

        balance = item[5]

        if balance:

            total += balance


    return total




def calculate_net_worth():

    assets = total_assets()

    debts = liabilities_total()


    return {
        "assets": assets,
        "liabilities": debts,
        "net_worth": assets - debts
    }




def print_net_worth():

    report = calculate_net_worth()


    print("=" * 60)
    print("PFOS NET WORTH")
    print("=" * 60)


    print()

    print(
        "Активы:",
        f"{report['assets']:,.2f}",
        "RUB"
    )


    print(
        "Обязательства:",
        f"{report['liabilities']:,.2f}",
        "RUB"
    )


    print()

    print(
        "ЧИСТЫЙ КАПИТАЛ:",
        f"{report['net_worth']:,.2f}",
        "RUB"
    )


    print("=" * 60)