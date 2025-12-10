# Contributing to PyLedger

Thank you for your interest in contributing to **PyLedger**!  
Your contributions help make this open-source accounting engine better, more reliable, and more useful for developers worldwide.

---

## Table of Contents

1. [How to Contribute](#how-to-contribute)  
2. [Code of Conduct](#code-of-conduct)  
3. [Reporting Issues](#reporting-issues)  
4. [Submitting Pull Requests](#submitting-pull-requests)  
5. [Coding Standards](#coding-standards)  
6. [Testing](#testing)  
7. [Feature Requests](#feature-requests)  
8. [Development Environment](#development-environment)  

---

## How to Contribute

There are several ways to contribute:

- **Report bugs or issues**: Help identify problems and suggest improvements.  
- **Submit pull requests**: Fix bugs, add features, or improve documentation.  
- **Improve documentation**: Clear examples, tutorials, or API references.  
- **Suggest enhancements**: Propose new features or improvements.

---

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.  
We value respect, collaboration, and inclusion in the community.

---

## Reporting Issues

Before reporting an issue:

1. Check the [existing issues](https://github.com/therealjozber/pyledger/issues) to see if it’s already reported.  
2. If not, create a new issue using the templates provided (Bug Report / Feature Request).  
3. Provide clear details:
   - Steps to reproduce (for bugs)  
   - Expected behavior vs. actual behavior  
   - Environment (Python version, OS, etc.)  

---

## Submitting Pull Requests

1. **Fork the repository**  
2. **Create a branch** for your feature/fix:
   ```bash
   git checkout -b feature/my-new-feature
````

3. **Make changes** and follow coding standards.
4. **Add tests** for new features or bug fixes.
5. **Run tests** locally:

   ```bash
   pytest
   ```
6. **Commit changes**:

   ```bash
   git commit -m "Add: brief description of changes"
   ```
7. **Push to your branch**:

   ```bash
   git push origin feature/my-new-feature
   ```
8. **Create a Pull Request** on GitHub.

> Make sure your PR includes a clear description and references any related issues.

---

## Coding Standards

* Use **Python 3.10+**
* Follow **PEP 8** style guide
* Use **type hints** where possible
* Write **docstrings** for all public classes and functions
* Keep functions and classes **small and focused**
* Run **Black** for formatting:

  ```bash
  black .
  ```
* Run **Ruff** for linting:

  ```bash
  ruff .
  ```

---

## Testing

Tests are required for new features and bug fixes.

* Tests are located in the `tests/` directory.
* Run all tests:

  ```bash
  pytest
  ```
* Coverage and quality improvements are appreciated.

---

## Feature Requests

If you have ideas for new features:

1. Check if a similar feature already exists in issues.
2. Create a **Feature Request issue** with clear description and benefits.
3. If possible, submit a pull request with the implementation.

---

## Development Environment

1. **Clone the repo**

   ```bash
   git clone https://github.com/therealjozber/pyledger.git
   cd pyledger
   ```
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # mac/linux
   venv\Scripts\activate     # windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run tests**

   ```bash
   pytest
   ```
5. **Use pre-commit hooks**

   ```bash
   pre-commit install
   ```

---

Thank you for contributing to **PyLedger**! Your contributions make it stronger and help developers worldwide manage accounting in Python.
