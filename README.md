# Python CLI Calculator

A simple command-line calculator written in Python.

This project was created as a foundational portfolio exercise to practice:
- clean function design
- input validation with regex
- exception handling
- unit testing with pytest
- basic Git workflow

---

## 📂 Project Structure
```
Calc/
│
├── calculator.py # Main application logic (CLI + calculation functions)
├── test_calculator.py # Unit tests (pytest)
├── pyproject.toml # Project configuration (pytest / tooling)
├── README.md
└── .gitignore
```
> Note: Local folders such as `.venv/`, `__pycache__/`, `.pytest_cache/`, and `.vscode/` are ignored.

---

## 🚀 Features

- Single-expression input format:
``` number operator number ``` 
- Supported operators: ``` + - * / ```
- Supports:
  - floating point numbers (`2.5*4`)
  - negative numbers (`-2.5+4`)
  - optional spaces (` 2.5   *   4 `)

- Error handling:
  - invalid format
  - invalid operator
  - division by zero
  - unsupported decimal separator (`,`)

---

## 🧮 Example Usage 
```
Enter expression (e.g. 2+3) or q to quit: 2+3
Result: 5.0

Enter expression (e.g. 2+3) or q to quit: -2.5*4
Result: -10.0

Enter expression (e.g. 2+3) or q to quit: 10/0
Error: Cannot divide by zero.
```

---

## ▶ Run the Application
---
```py calculator.py```

## 🧪 Run Tests

Install pytest (if needed):

```python -m pip install pytest```

Run tests:

```pytest```

---

## ⚠ Limitations

- Only expressions with a single operator are supported.
- Parentheses and multi-operator expressions are not supported.
- Decimal separator must be `.` (comma is not supported).
- Thousands separators are not supported.

---

## 📚 What I Practiced

- Regex-based input validation
- Structured function design
- Exception-driven error handling
- Parametrized unit testing with pytest
- Clean project structure

