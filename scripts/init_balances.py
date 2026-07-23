from database.balances import (
    init_balances_table,
    clear_balances,
    set_balance
)



def main():

    init_balances_table()

    clear_balances()


    balances = [

        (
            1,
            0,
            "Выписка ВТБ"
        ),

        (
            2,
            0,
            "Выписка Сбербанк"
        ),

        (
            3,
            685415,
            "Выписка Озон накопительный"
        ),

        (
            4,
            0,
            "Выписка Озон дебетовый"
        )

    ]



    for item in balances:

        set_balance(
            item[0],
            item[1],
            item[2]
        )



    print(
        "Балансы счетов загружены"
    )



if __name__ == "__main__":
    main()