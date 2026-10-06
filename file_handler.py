import json
from pathlib import Path


def load_expenses(filename):
    """Load expenses from a JSON file."""
    path = Path(filename)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the expense file. Starting with empty data.")
        return []


def save_expenses(filename, expenses):
    """Save expenses to a JSON file."""
    path = Path(filename)

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except OSError as error:
        print(f"Error saving expenses: {error}")
