from database.repository import get_all_operations
from reports.family_finance import (
    family_finance_report,
    show_family_finance
)


operations = get_all_operations()


report = family_finance_report(
    operations,
    "ALL"
)


show_family_finance(
    report
)