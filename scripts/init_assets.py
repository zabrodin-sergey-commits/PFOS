from database.assets import (
    init_assets_table,
    clear_assets,
    add_asset
)



init_assets_table()

clear_assets()



assets = [

    (
        "Квартира Дагомыс",
        "real_estate",
        "Семья",
        15000000,
        "Квартира с ипотекой"
    ),

    (
        "3-комнатная квартира Магадан",
        "real_estate",
        "Сергей",
        12000000,
        "Основное жильё"
    ),

    (
        "2-комнатная квартира Магадан",
        "real_estate",
        "Семья",
        8000000,
        "Инвестиционная квартира"
    ),

    (
        "Гараж Магадан",
        "real_estate",
        "Сергей",
        2700000,
        "Двухуровневый гараж"
    ),


    (
        "Toyota Wish",
        "vehicle",
        "Сергей",
        1200000,
        "Основной автомобиль"
    ),

    (
        "Mitsubishi Pajero IO",
        "vehicle",
        "Сергей",
        300000,
        "Автомобиль"
    ),

    (
        "Daihatsu Pyzar",
        "vehicle",
        "Сергей",
        150000,
        "Автомобиль"
    )

]



for asset in assets:

    add_asset(
        *asset
    )


print("Активы загружены")