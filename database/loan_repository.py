from database.liabilities import add_liability


def save_loan(loan):

    if loan is None:
        return


    purpose = "Кредит"


    if loan.loan_type:
        purpose = loan.loan_type


    asset = None


    if "авто" in purpose.lower():
        asset = "Автомобиль"

    elif "ипот" in purpose.lower():
        asset = "Недвижимость"

    elif "ремонт" in purpose.lower():
        asset = "Ремонт"



    add_liability(
        bank=loan.bank or "ВТБ",
        liability_type="Кредит",
        name=loan.contract_number or "Без номера",
        owner=loan.borrower,
        balance=loan.balance,
        monthly_payment=loan.monthly_payment,
        end_date=loan.end_date,
        asset=asset,
        purpose=purpose
    )


    print()
    print("Кредит сохранен в PFOS liabilities")