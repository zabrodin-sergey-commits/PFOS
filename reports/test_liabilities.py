from database.liabilities import (
    get_liabilities,
    total_liabilities
)



print("=" * 60)
print("PFOS LIABILITIES")
print("=" * 60)


print()


for liability in get_liabilities():

    (
        id,
        bank,
        liability_type,
        name,
        owner,
        balance,
        payment,
        end_date,
        asset,
        purpose,
        status
    ) = liability


    print(
        id,
        "|",
        bank,
        "|",
        liability_type,
        "|",
        name,
        "|",
        owner,
        "|",
        f"{balance:,.2f}",
        "RUB",
        "|",
        f"платёж {payment:,.2f}",
        "|",
        end_date,
    )



print()

print(
    "TOTAL:",
    f"{total_liabilities():,.2f}",
    "RUB"
)