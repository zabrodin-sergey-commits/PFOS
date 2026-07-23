from reports.net_worth import (
    calculate_net_worth,
    print_net_worth
)



print_net_worth()



report = calculate_net_worth()



print()

print("Проверка структуры:")

for key, value in report.items():

    print(
        key,
        "=",
        value
    )