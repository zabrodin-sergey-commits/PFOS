from models.operation import Operation
from processors.normalizer import normalize_operation



operations = [

    Operation(
        "29.05.2026",
        "Оплата товаров и услуг WB*WB",
        199,
        "OUT"
    ),

    Operation(
        "29.05.2026",
        "Снятие наличных в банкомате",
        4900,
        "OUT"
    ),

    Operation(
        "29.05.2026",
        "Переводы через СБП",
        5000,
        "OUT"
    )

]


for operation in operations:

    normalize_operation(operation)

    print(
        operation,
        "|",
        operation.category,
        "|",
        operation.is_transfer
    )