from expense_manager import ExpenseManager
from validators import validate_amount, validate_category, validate_date


def print_menu():
    """Display the main menu."""
    print("\n========== STUDENT EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. View Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("=============================================")


def add_expense(manager):
    """Collect and validate expense details from the user."""
    print("\n--- Add Expense ---")
    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    category = input("Enter category (Food/Travel/Education/Shopping/Other): ").strip()
    category = validate_category(category)
    if category is None:
        print("Invalid category.")
        return

    try:
        amount = float(input("Enter amount: "))
        amount = validate_amount(amount)
    except ValueError as error:
        print(f"Invalid amount: {error}")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date. Please use YYYY-MM-DD.")
        return

    manager.add_expense(description, category, amount, date)
    print("Expense added successfully.")


def view_expenses(manager, expenses=None):
    """Display expenses in a readable format."""
    expenses = manager.expenses if expenses is None else expenses

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n---------------- EXPENSES ----------------")
    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )
    print("-------------------------------------------")


def search_category(manager):
    """Search expenses using a category."""
    category = input("Enter category to search: ").strip()
    category = validate_category(category)

    if category is None:
        print("Invalid category.")
        return

    results = manager.search_by_category(category)
    view_expenses(manager, results)


def show_summary(manager):
    """Display spending statistics."""
    summary = manager.get_summary()

    print("\n--------------- SUMMARY ----------------")
    print(f"Total expenses : {summary['count']}")
    print(f"Total spent    : ₹{summary['total']:.2f}")
    print(f"Average expense: ₹{summary['average']:.2f}")

    if summary["highest"]:
        highest = summary["highest"]
        print(
            f"Highest expense: ₹{highest['amount']:.2f} "
            f"({highest['description']})"
        )

    print("\nCategory totals:")
    for category, amount in summary["category_totals"].items():
        print(f"- {category}: ₹{amount:.2f}")
    print("-----------------------------------------")


def delete_expense(manager):
    """Delete an expense using its ID."""
    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    if manager.delete_expense(expense_id):
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")


def main():
    """Run the application."""
    manager = ExpenseManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)
        elif choice == "2":
            view_expenses(manager)
        elif choice == "3":
            search_category(manager)
        elif choice == "4":
            show_summary(manager)
        elif choice == "5":
            delete_expense(manager)
        elif choice == "6":
            print("Thank you for using Student Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
