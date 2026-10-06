# Student Expense Tracker

A practical modular Python application that helps students record, manage, search, and analyze their daily expenses.

## Project Objective

The purpose of this project is to demonstrate strong Python programming fundamentals through a real-world application.

The project uses:

- Data types
- Lists, dictionaries, tuples, and sets
- Conditional statements
- `for` and `while` loops
- Functions
- Classes
- Modules
- Comprehensions
- File handling
- JSON data storage
- Input validation
- Exception handling

## Features

1. Add a new expense
2. View all expenses
3. Search expenses by category
4. View total and average spending
5. Find the highest expense
6. View category-wise spending
7. Delete an expense
8. Automatically save data to `expenses.json`
9. Automatically load previous data when the application starts
10. Validate amount, date, and category

## Project Structure

```text
student-expense-tracker/
│
├── main.py
├── expense_manager.py
├── validators.py
├── file_handler.py
├── expenses.json
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

**main.py**
- Contains the user interface and menu.
- Gets input from the user.
- Calls functions from other modules.

**expense_manager.py**
- Contains the `ExpenseManager` class.
- Adds, searches, deletes, and summarizes expenses.

**validators.py**
- Validates amount, category, and date.

**file_handler.py**
- Reads and writes expense data using JSON.

**expenses.json**
- Stores expense records permanently.

## Requirements

- Python 3.8 or higher
- Git
- GitHub account

No external Python packages are required.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-expense-tracker.git
```

### 2. Open the project

```bash
cd student-expense-tracker
```

### 3. Run the application

```bash
python main.py
```

On some systems you may need:

```bash
python3 main.py
```

## Example Menu

```text
========== STUDENT EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. Search by Category
4. View Summary
5. Delete Expense
6. Exit
=============================================
```

## Example Summary

```text
--------------- SUMMARY ----------------
Total expenses : 3
Total spent    : ₹470.00
Average expense: ₹156.67
Highest expense: ₹350.00 (Python book)

Category totals:
- Food: ₹80.00
- Travel: ₹40.00
- Education: ₹350.00
-----------------------------------------
```

## Python Concepts Demonstrated

### 1. Data Types

The application uses strings, integers, floats, booleans, and `None`.

Example:

```python
description = "Lunch"
amount = 80.0
expense_id = 1
```

### 2. Collections

Expenses are stored as a list of dictionaries.

A tuple is used for fixed categories:

```python
VALID_CATEGORIES = ("Food", "Travel", "Education", "Shopping", "Other")
```

A set is used for validation:

```python
VALID_CATEGORIES = {"Food", "Travel", "Education", "Shopping", "Other"}
```

### 3. Control Structures

The program uses `if`, `elif`, `else`, `for`, and `while`.

### 4. Functions

The project contains reusable functions such as:

- `add_expense()`
- `view_expenses()`
- `search_category()`
- `show_summary()`
- `validate_amount()`
- `validate_date()`
- `load_expenses()`
- `save_expenses()`

### 5. Modules

The application is divided into multiple Python files instead of keeping everything in one file.

### 6. Comprehensions

List comprehension is used to search and delete expenses.

Example:

```python
results = [
    expense
    for expense in self.expenses
    if expense["category"].lower() == category.lower()
]
```

Dictionary comprehension is used for category totals.

### 7. File Handling

The project uses `with open()` to safely read and write JSON files.

### 8. Validation

The application checks:

- Empty descriptions
- Positive expense amounts
- Maximum reasonable amount
- Valid categories
- Correct date format

### 9. Exception Handling

`try/except` is used to handle invalid numeric input and file errors.

## GitHub Upload Steps

Create a new GitHub repository named:

```text
student-expense-tracker
```

Then open the project folder in Command Prompt or Terminal.

Run:

```bash
git init
git add .
git commit -m "Initial commit - Student Expense Tracker"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-expense-tracker.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Suggested GitHub Commit History

For a stronger project submission, use meaningful commits such as:

```text
Initial project setup
Added expense management
Added input validation
Added JSON file storage
Added expense summary
Added README documentation
```

## Future Improvements

Possible future features include:

- Monthly expense reports
- Budget limits
- Login system
- CSV export
- Graphical user interface
- SQLite database
- Web version using Django or FastAPI

## Author

**Bhaskar Banothu**

Student Expense Tracker - Python Fundamentals Practical Project
