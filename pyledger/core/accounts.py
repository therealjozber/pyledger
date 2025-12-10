from enum import Enum


class AccountType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"
    EQUITY = "equity"
    REVENUE = "revenue"
    EXPENSE = "expense"


class Account:
    def __init__(self, name: str, account_type: AccountType):
        self.name = name
        self.type = account_type
        self.balance = 0.0

    def apply_debit(self, amount: float):
        if self.type in {AccountType.ASSET, AccountType.EXPENSE}:
            self.balance += amount
        else:
            self.balance -= amount

    def apply_credit(self, amount: float):
        if self.type in {AccountType.ASSET, AccountType.EXPENSE}:
            self.balance -= amount
        else:
            self.balance += amount

    def __repr__(self):
        return f"<Account {self.name} ({self.type.value}): {self.balance}>"
