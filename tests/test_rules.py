from parsers.rules.account_rule import find_account
from parsers.rules.owner_rule import find_owner


sample_text = """
ВТБ

Получатель
Забродин Сергей Сергеевич со счета платежной банковской карты

Счет
40817810219564019461
"""


print("=" * 40)
print("Тестирование правил PFOS")
print("=" * 40)
print()

account = find_account(sample_text)
owner = find_owner(sample_text)

print("Счет:")
print(account)
print()

print("Владелец:")
print(owner)
print()

print("=" * 40)

if account == "40817810219564019461":
    print("✅ account_rule OK")
else:
    print("❌ account_rule ERROR")

if owner.startswith("Забродин Сергей"):
    print("✅ owner_rule OK")
else:
    print("❌ owner_rule ERROR")