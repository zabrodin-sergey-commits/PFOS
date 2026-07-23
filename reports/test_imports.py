from reports.imports import get_import_history



history = get_import_history()



print("=" * 50)
print("PFOS Import History")
print("=" * 50)



for item in history:

    print()

    print("Файл:", item["filename"])
    print("Банк:", item["bank"])
    print("Импорт:", item["created_at"])

    print()

    print("Операций:", item["count"])

    print(
        "Доходы:",
        item["income"],
        "RUB"
    )

    print(
        "Расходы:",
        item["expense"],
        "RUB"
    )

    print(
        "Баланс:",
        item["balance"],
        "RUB"
    )

    print(
        "Документ:",
        item["document_id"]
    )

    print("-" * 50)