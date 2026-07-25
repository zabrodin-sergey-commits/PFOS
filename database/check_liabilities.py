from database.liabilities import (
    get_liabilities,
    total_liabilities
)


def main():

    print("=" * 40)
    print(" PFOS LIABILITIES REPORT ")
    print("=" * 40)
    print()


    liabilities = get_liabilities()


    if not liabilities:
        print("Обязательств не найдено")
        return


    print("===== ОБЯЗАТЕЛЬСТВА =====")
    print()


    for item in liabilities:

        (
            id,
            bank,
            liability_type,
            name,
            owner,
            balance,
            monthly_payment,
            end_date,
            asset,
            purpose,
            status
        ) = item


        print(
            f"""
Банк          : {bank}
Тип           : {liability_type}
Название      : {name}
Владелец      : {owner}
Остаток       : {balance:.2f} RUB
Платеж        : {monthly_payment:.2f} RUB
Объект        : {asset}
Назначение    : {purpose}
Статус        : {status}
--------------------------------
"""
        )


    print()
    print("=" * 40)

    print(
        f"ВСЕГО ДОЛГОВ: {total_liabilities():.2f} RUB"
    )

    print("=" * 40)



if __name__ == "__main__":
    main()