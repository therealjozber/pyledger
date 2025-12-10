class Transaction:
    def __init__(self, description: str):
        self.description = description
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def is_balanced(self):
        debit = sum(e.amount for e in self.entries if e.is_debit)
        credit = sum(e.amount for e in self.entries if not e.is_debit)
        return debit == credit
