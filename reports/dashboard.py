from database.net_worth import calculate_net_worth

from database.assets import get_assets

from database.liabilities import get_liabilities


LINE = "=" * 40


def money(value):

    return f"{value:,.2f} ₽".replace(",", " ")


def print_assets():

    print()

    print("АКТИВЫ")

    print()

    assets = get_assets()

    total = 0

    for asset in assets:

        value = asset["value"]

        total += value

        print(
            f"{asset['name']:<25}{money(value):>15}"
        )

    print()

    print("-" * 40)

    print(
        f"{'Итого активов':<25}{money(total):>15}"
    )

    return total


def print_liabilities():

    print()

    print("ОБЯЗАТЕЛЬСТВА")

    print()

    liabilities = get_liabilities()

    total = 0

    for loan in liabilities:

        balance = loan["balance"]

        total += balance

        print(
            f"{loan['name']:<25}{money(balance):>15}"
        )

    print()

    print("-" * 40)

    print(
        f"{'Итого долгов':<25}{money(total):>15}"
    )

    return total


def dashboard():

    summary = calculate_net_worth()

    print()

    print(LINE)

    print("PFOS")

    print("Личный финансовый баланс")

    print(LINE)

    print_assets()

    print_liabilities()

    print()

    print(LINE)

    print()

    print(
        f"{'Чистый капитал':<25}{money(summary['net_worth']):>15}"
    )

    print()

    print(LINE)

    print()


if __name__ == "__main__":

    dashboard()