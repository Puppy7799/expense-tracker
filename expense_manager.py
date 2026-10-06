from file_handler import load_expenses, save_expenses


class ExpenseManager:
    """Manage student expenses using a list of dictionaries."""

    VALID_CATEGORIES = ("Food", "Travel", "Education", "Shopping", "Other")

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = load_expenses(filename)
        self._next_id = self._calculate_next_id()

    def _calculate_next_id(self):
        """Find the next available expense ID."""
        if not self.expenses:
            return 1
        return max(expense["id"] for expense in self.expenses) + 1

    def add_expense(self, description, category, amount, date):
        """Add an expense and save it to the JSON file."""
        expense = {
            "id": self._next_id,
            "description": description,
            "category": category,
            "amount": amount,
            "date": date,
        }
        self.expenses.append(expense)
        self._next_id += 1
        save_expenses(self.filename, self.expenses)

    def search_by_category(self, category):
        """Return expenses matching the selected category."""
        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        ]

    def delete_expense(self, expense_id):
        """Delete an expense by ID and return True if successful."""
        original_count = len(self.expenses)

        self.expenses = [
            expense for expense in self.expenses
            if expense["id"] != expense_id
        ]

        if len(self.expenses) < original_count:
            save_expenses(self.filename, self.expenses)
            return True

        return False

    def get_summary(self):
        """Calculate useful spending statistics."""
        amounts = [expense["amount"] for expense in self.expenses]

        total = sum(amounts)
        count = len(amounts)
        average = total / count if count else 0

        highest = max(self.expenses, key=lambda expense: expense["amount"]) if self.expenses else None

        category_totals = {
            category: sum(
                expense["amount"]
                for expense in self.expenses
                if expense["category"] == category
            )
            for category in self.VALID_CATEGORIES
        }

        # Dictionary comprehension removes categories with no spending.
        category_totals = {
            category: amount
            for category, amount in category_totals.items()
            if amount > 0
        }

        return {
            "count": count,
            "total": total,
            "average": average,
            "highest": highest,
            "category_totals": category_totals,
        }
