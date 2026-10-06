from datetime import datetime


VALID_CATEGORIES = {"Food", "Travel", "Education", "Shopping", "Other"}


def validate_amount(amount):
    """Validate that an expense amount is positive."""
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > 1000000:
        raise ValueError("Amount is too large.")
    return round(amount, 2)


def validate_category(category):
    """Return a correctly formatted category or None."""
    category = category.strip().title()

    if category in VALID_CATEGORIES:
        return category

    return None


def validate_date(date_text):
    """Validate date format and actual calendar date."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
