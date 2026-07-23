from collections import defaultdict



def calculate_income(operations):
    """
    Общая сумма доходов
    """

    total = 0


    for operation in operations:

        if operation.is_transfer:
            continue


        if operation.direction == "IN":
            total += operation.amount


    return total



def calculate_expenses(operations):
    """
    Общая сумма расходов
    """

    total = 0


    for operation in operations:

        if operation.is_transfer:
            continue


        if operation.direction == "OUT":
            total += operation.amount


    return total



def calculate_balance_change(operations):
    """
    Изменение баланса
    """

    return (
        calculate_income(operations)
        -
        calculate_expenses(operations)
    )



def calculate_balance(operations):
    """
    Баланс (алиас)
    """

    return calculate_balance_change(operations)



def calculate_categories(operations):
    """
    Расходы по категориям
    """

    result = defaultdict(float)


    for operation in operations:

        if operation.is_transfer:
            continue


        if operation.direction == "OUT":

            result[
                operation.category
            ] += operation.amount


    return dict(result)



def calculate_statistics(operations):
    """
    Полный финансовый анализ
    """

    income = calculate_income(operations)

    expenses = calculate_expenses(operations)


    return {

        "income": income,

        "expenses": expenses,

        "balance": income - expenses,

        "categories": calculate_categories(operations)

    }



def print_statistics(result):

    print("=" * 40)
    print("PFOS Statistics")
    print("=" * 40)

    print()

    print(
        f"Доходы: {result['income']}"
    )

    print(
        f"Расходы: {result['expenses']}"
    )

    print(
        f"Баланс: {result['balance']}"
    )


    if result.get("categories"):

        print()

        print("Категории расходов:")


        for category, amount in result["categories"].items():

            print(
                f"{category}: {amount}"
            )