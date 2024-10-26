from datetime import datetime
from logging.config import valid_ident
import re
from sre_parse import CATEGORIES

from matplotlib import category
from pyparsing import C



date_format="%d-%m-%Y"
CATEGORIES ={"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date frormat, please enter the date dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount= float(input("Enter the amount:"))
        if amount<= 0:
            raise ValueError("Amount muct be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please Enter 'I' for Income or 'E' for Expense.")
    return get_category

def get_description():
    return input("Enter a description (optional):")
