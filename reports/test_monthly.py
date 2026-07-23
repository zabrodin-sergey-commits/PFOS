from database.repository import get_all_operations
from reports.monthly import monthly_report


operations = get_all_operations()


report = monthly_report(
    operations,
    "2026-05"
)


print("=" * 50)
print("PFOS Monthly Report")
print("=" * 50)


print()

print("Месяц:", report["month"])
print("Операций:", report["count"])

print()

print(
    "Доходы:",
    report["income"],
    "RUB"
)

print(
    "Расходы:",
    report["expense"],
    "RUB"
)

print(
    "Баланс:",
    report["balance"],
    "RUB"
)


print()

print("Категории расходов:")

for category, value in report["categories"].items():
    print(
        category,
        ":",
        value,
        "RUB"
    )


print()

print("Крупные расходы:")

for op in report["large"]:
    print(op)