from datetime import datetime

# Define date format and categories
date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    """Get and validate the date from the user input."""
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format, please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    """Get and validate the amount entered by the user."""
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative, non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    """Get and validate the transaction category (Income or Expense)."""
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()  # Call the function again recursively

def get_description():
    """Get a description for the transaction (optional)."""
    return input("Enter a description (optional): ")
