class Entry:
    def __init__(self, account, amount, is_debit=True):
        self.account = account
        self.amount = amount
        self.is_debit = is_debit
