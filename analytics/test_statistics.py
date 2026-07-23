from models.operation import Operation

from analytics.statistics import (
    calculate_income,
    calculate_expenses,
    calculate_balance_change
)



operations = [

    Operation(
        "02.01.2026",
        "Зарплата",
        100000,
        "IN"
    ),

    Operation(
        "02.01.2026",
        "Перевод себе",
        3000,
        "OUT"
    ),

    Operation(
        "02.01.2026",
        "Перевод себе",
        3000,
        "IN"
    ),

    Operation(
        "03.01.2026",
        "Покупка",
        500,
        "OUT"
    ),

]


for o in operations:
    o.is_transfer = (
        "Перевод" in o.description
    )


print("Доходы:",
      calculate_income(operations))

print("Расходы:",
      calculate_expenses(operations))

print("Баланс:",
      calculate_balance_change(operations))