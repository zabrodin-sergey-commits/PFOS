from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class FinancialStatement:
    bank: str = ""
    document_type: str = ""
    version: str = ""

    owner: str = ""
    account: str = ""
    currency: str = ""

    period_start: date | None = None
    period_end: date | None = None

    balance_start: float = 0.0
    balance_end: float = 0.0

    income: float = 0.0
    expense: float = 0.0

    operations: List = field(default_factory=list)