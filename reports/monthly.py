from database.repository import get_operations_by_month


def monthly_report(operations, month):
    """
    Финансовый отчёт за месяц.

    operations:
        список объектов Operation

    month:
        YYYY-MM
    """


    income = 0
    expense = 0

    categories = {}

    large_expenses = []


    transfer_income = 0
    transfer_expense = 0



    for op in operations:


        amount = float(op.amount)



        if op.direction == "IN":

            income += amount


            if getattr(op, "is_transfer", False):
                transfer_income += amount



        elif op.direction == "OUT":

            expense += amount


            if getattr(op, "is_transfer", False):
                transfer_expense += amount



            category = (
                getattr(op, "category", None)
                or
                "Не определено"
            )


            categories[category] = (
                categories.get(category, 0)
                +
                amount
            )



            if amount >= 3000:

                large_expenses.append(op)



    return {

        # основной формат старого отчёта
        "month": month,

        "count": len(operations),

        "income": round(
            income,
            2
        ),

        "expense": round(
            expense,
            2
        ),

        "balance": round(
            income - expense,
            2
        ),



        # дополнительные данные для будущего PFOS
        "transfers_income": round(
            transfer_income,
            2
        ),

        "transfers_expense": round(
            transfer_expense,
            2
        ),


        "categories": categories,


        "large": large_expenses,

# оставляем новый вариант тоже
        "large_expenses": large_expenses
    }