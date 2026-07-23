from database.balances import (
    get_balances,
    total_balance
)


print("=" * 60)
print("PFOS ACCOUNT BALANCES")
print("=" * 60)


print()


for row in get_balances():

    print(row)



print()

print(
    "TOTAL:",
    total_balance(),
    "RUB"
)