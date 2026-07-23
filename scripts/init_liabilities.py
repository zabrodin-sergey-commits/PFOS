from database.liabilities import (
    init_liabilities_table,
    clear_liabilities,
    add_liability
)



init_liabilities_table()

clear_liabilities()



liabilities = [

    (
        "Россельхозбанк",
        "mortgage",
        "Ипотека Дагомыс",
        "Семья",
        1284563.10,
        26657.09,
        "14.07.2031",
        "Квартира Дагомыс",
        "Ипотека квартиры"
    ),


    (
        "ВТБ",
        "repair",
        "Кредит на ремонт",
        "Сергей",
        328112.01,
        31561.25,
        "12.07.2027",
        "Квартира Дагомыс",
        "Ремонт квартиры"
    ),


    (
        "ВТБ",
        "auto",
        "Автокредит",
        "Сергей",
        146337.33,
        10257.99,
        "12.05.2028",
        "Toyota Wish",
        "Покупка автомобиля"
    ),


    (
        "ВТБ",
        "credit_card",
        "Кредитная карта",
        "Сергей",
        189427.69,
        0,
        "20.08.2026",
        None,
        "Задолженность по кредитной карте"
    )

]



for item in liabilities:

    add_liability(
        *item
    )



print("Обязательства загружены")