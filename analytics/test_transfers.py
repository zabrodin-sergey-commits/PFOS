from models.operation import Operation
from analytics.transfers import remove_internal_transfers


def main():

    operations = [

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


    for op in operations:
        op.is_transfer = True


    operations[2].is_transfer = False


    print("До:")
    for op in operations:
        print(op)


    print()
    print("После удаления переводов:")
    

    result = remove_internal_transfers(operations)


    for op in result:
        print(op)



if __name__ == "__main__":
    main()