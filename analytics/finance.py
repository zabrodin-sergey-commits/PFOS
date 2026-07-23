from collections import defaultdict



def analyze_finances(operations):
    """
    Финансовый анализ PFOS.

    Разделяет:

    1. Реальные доходы
    2. Реальные расходы
    3. Внутренние переводы между своими счетами
    4. Внешние переводы

    Внутренние переводы НЕ влияют
    на финансовый результат.
    """

    income = 0.0
    expenses = 0.0


    internal_transfers = 0.0

    incoming_transfers = 0.0
    outgoing_transfers = 0.0



    income_categories = defaultdict(float)
    expense_categories = defaultdict(float)


    real_operations = []

    transfer_operations = []



    for op in operations:


        amount = abs(
            float(op.amount)
        )


        direction = getattr(
            op,
            "direction",
            None
        )


        category = getattr(
            op,
            "category",
            "Не определено"
        )


        is_internal = bool(
            getattr(
                op,
                "internal_transfer",
                False
            )
        )


        is_transfer = bool(
            getattr(
                op,
                "is_transfer",
                False
            )
        )



        #
        # 1. Внутренние переводы
        #

        if is_internal:

            internal_transfers += amount

            transfer_operations.append(
                op
            )

            continue



        #
        # 2. Переводы, которые не удалось
        # сопоставить как внутренние
        #
        # Пока считаем их отдельно,
        # а не доходом/расходом
        #

        if is_transfer:

            transfer_operations.append(
                op
            )


            if direction == "IN":

                incoming_transfers += amount


            elif direction == "OUT":

                outgoing_transfers += amount


            continue




        #
        # 3. Реальные операции
        #

        real_operations.append(
            op
        )



        if direction == "IN":


            income += amount


            income_categories[
                category
            ] += amount



        elif direction == "OUT":


            expenses += amount


            expense_categories[
                category
            ] += amount




    return {


        #
        # Главные показатели
        #

        "income":
            round(
                income,
                2
            ),


        "expenses":
            round(
                expenses,
                2
            ),



        "balance":
            round(
                income - expenses,
                2
            ),



        #
        # Перемещения денег
        #

        "internal_transfers":
            round(
                internal_transfers,
                2
            ),


        "incoming_transfers":
            round(
                incoming_transfers,
                2
            ),


        "outgoing_transfers":
            round(
                outgoing_transfers,
                2
            ),



        #
        # Категории
        #

        "income_categories":
            dict(
                sorted(
                    income_categories.items(),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),



        "expense_categories":
            dict(
                sorted(
                    expense_categories.items(),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),



        #
        # Операции
        #

        "real_operations":
            real_operations,


        "transfer_operations":
            transfer_operations,


        "operations_count":
            len(
                operations
            )

    }




def calculate_cash_flow(operations):

    report = analyze_finances(
        operations
    )


    return {


        "income":
            report["income"],


        "expenses":
            report["expenses"],


        "balance":
            report["balance"],


        "internal_transfers":
            report["internal_transfers"],


        "incoming_transfers":
            report["incoming_transfers"],


        "outgoing_transfers":
            report["outgoing_transfers"]

    }