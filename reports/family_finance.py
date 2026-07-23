from analytics.finance import analyze_finances



def print_money(value):
    return f"{value:,.2f} RUB"



def family_finance_report(operations, period=None):

    analysis = analyze_finances(
        operations
    )


    report = {

        "period": period,

        "income": analysis["income"],

        "expenses": analysis["expenses"],

        "balance": analysis["balance"],

        "internal_transfers":
            analysis["internal_transfers"],

        "income_categories":
            analysis["income_categories"],

        "expense_categories":
            analysis["expense_categories"],

        "operations_count":
            analysis["operations_count"],

        "large_operations":
            sorted(
                [
                    op
                    for op in analysis["real_operations"]
                    if op.direction == "OUT"
                ],
                key=lambda x: x.amount,
                reverse=True
            )[:10],

        "transfer_operations":
            analysis["transfer_operations"]

    }


    return report




def show_family_finance(report):

    print("=" * 60)
    print("PFOS FAMILY FINANCE REPORT")
    print("=" * 60)


    if report.get("period"):

        print(
            "Период:",
            report["period"]
        )


    print()

    print(
        "Операций:",
        report["operations_count"]
    )


    print()

    print(
        "Доходы:",
        print_money(
            report["income"]
        )
    )


    print(
        "Расходы:",
        print_money(
            report["expenses"]
        )
    )


    print(
        "Баланс:",
        print_money(
            report["balance"]
        )
    )


    print()

    print(
        "Внутренние переводы:",
        print_money(
            report["internal_transfers"]
        )
    )



    print()
    print("Доходы по категориям:")
    

    for name, value in report["income_categories"].items():

        print(
            name,
            ":",
            print_money(value)
        )



    print()

    print("Расходы по категориям:")


    for name, value in report["expense_categories"].items():

        print(
            name,
            ":",
            print_money(value)
        )



    print()

    print("Крупные расходы:")


    for op in report["large_operations"]:

        flag = ""

        if getattr(
            op,
            "internal_transfer",
            False
        ):
            flag = "TRANSFER"


        print(
            op.date,
            "|",
            op.direction,
            "|",
            op.amount,
            "RUB |",
            op.description,
            "|",
            op.category,
            "|",
            flag
        )