# PyLedger

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build](https://github.com/therealjozber/pyledger/actions/workflows/python.yml/badge.svg)](https://github.com/therealjozber/pyledger/actions)

**PyLedger** is an **open-source, Python-based double-entry accounting engine**.  
It provides a modular, extensible framework for recording transactions, maintaining ledgers, validating entries, and generating financial reports.  

The project is **designed for developers, startups, and businesses** looking to integrate accounting into Python applications, ERP systems, or POS platforms.

---

## Features

- **Double-entry accounting engine**: Ensures all transactions balance.  
- **Account hierarchy**: Supports Assets, Liabilities, Equity, Revenue, and Expenses.  
- **Transactions & Journals**: Record single or batch transactions easily.  
- **Validation Rules Engine**: Ensures consistency and prevents errors.  
- **Financial Reports**: Trial Balance, Balance Sheet, and Income Statement.  
- **Modular & Extensible**: Add storage backends, reporting formats, or validation rules.  
- **Unit Tested**: Basic engine comes with ready-to-run tests.

---

## Installation

Clone the repository and set up a Python environment:

```bash
git clone https://github.com/therealjozber/pyledger.git
cd pyledger
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows
pip install -r requirements.txt  # if dependencies are added later
````

---

## Quick Start

```python
from pyledger.core.accounts import Account, AccountType
from pyledger.core.entries import Entry
from pyledger.core.transactions import Transaction
from pyledger.core.ledger import Ledger

# Create accounts
cash = Account("Cash", AccountType.ASSET)
revenue = Account("Revenue", AccountType.REVENUE)

# Create a transaction
t = Transaction("Sale of goods")
t.add_entry(Entry(cash, 100, is_debit=True))
t.add_entry(Entry(revenue, 100, is_debit=False))

# Post transaction to ledger
ledger = Ledger()
ledger.post(t)

print(f"Cash balance: {cash.balance}")
print(f"Revenue balance: {revenue.balance}")
```

---

## Project Structure

```
pyledger/
├── pyledger/
│   ├── core/       # Core accounting engine (Accounts, Entries, Ledger, Transactions)
│   ├── rules/      # Validation rules engine
│   ├── reports/    # Financial reports generators
│   ├── storage/    # Storage backends (memory, JSON, SQLite)
│   └── utils/      # Helper functions
├── examples/       # Example scripts
├── tests/          # Unit tests
├── README.md
├── CONTRIBUTING.md
└── pyproject.toml
```

---

## Contributing

We welcome contributions!

**Getting started:**

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/awesome-feature
   ```
3. Make your changes and add tests.
4. Run tests to ensure everything passes:

   ```bash
   pytest
   ```
5. Commit changes:

   ```bash
   git commit -m "Add awesome feature"
   ```
6. Push to your branch and create a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Future Roadmap

* JSON, SQLite, and PostgreSQL storage backends
* Audit trail support
* Automated financial statements (P&L, Balance Sheet)
* CLI interface
* Tax calculation plugins (VAT/GST)
* Event-sourced ledger mode

---

## License

PyLedger is licensed under the [MIT License](LICENSE).

---

## Support

Join discussions or report issues on [GitHub Discussions](https://github.com/therealjozber/pyledger/discussions) or [Issues](https://github.com/therealjozber/pyledger/issues).
