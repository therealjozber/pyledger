from pyledger.core.accounts import Account, AccountType
from pyledger.core.transactions import Transaction
from pyledger.core.entries import Entry
from pyledger.core.ledger import Ledger


def test_basic_posting():
    cash = Account("Cash", AccountType.ASSET)
    revenue = Account("Revenue", AccountType.REVENUE)

    t = Transaction("Sale")
    t.add_entry(Entry(cash, 100, is_debit=True))
    t.add_entry(Entry(revenue, 100, is_debit=False))

    ledger = Ledger()
    ledger.post(t)

    assert cash.balance == 100
    assert revenue.balance == 100
