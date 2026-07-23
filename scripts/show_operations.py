from database.repository import get_all_operations


print("=" * 50)
print("PFOS Operations")
print("=" * 50)
print()


operations = get_all_operations()


for op in operations:

    transfer = "TRANSFER" if op.is_transfer else ""

    print(
        f"{op.date} | "
        f"{op.direction} | "
        f"{op.amount} RUB | "
        f"{op.category} | "
        f"{op.description} | "
        f"{transfer}"
    )