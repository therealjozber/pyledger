from .exceptions import UnbalancedTransactionError


class Ledger:
    def __init__(self):
        self.transactions = []

    def post(self, transaction):
        if not transaction.is_balanced():
            raise UnbalancedTransactionError("Transaction is not balanced")

        for entry in transaction.entries:
            if entry.is_debit:
                entry.account.apply_debit(entry.amount)
            else:
                entry.account.apply_credit(entry.amount)

        self.transactions.append(transaction)
