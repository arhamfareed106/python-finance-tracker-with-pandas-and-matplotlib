import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]  # Changed 'data' to 'date'

    @classmethod
    def initialize_csv(cls):
        try:
            # Try to read the CSV file
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file is not found, create it with the proper columns
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Create a new entry as a dictionary
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        # Open the CSV file and append the new entry
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # Write the header if the file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_entry)

        print("Entry added successfully")


def add():
    # Initialize the CSV file if it doesn't exist
    CSV.initialize_csv()

    # Get user input for the entry
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or Enter for today's date:", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    # Add the entry to the CSV file
    CSV.add_entry(date, amount, category, description)


add()

# CSV.initialize_csv()
# CSV.add_entry("20-11-2024", 1025, "Income", "Salary")
