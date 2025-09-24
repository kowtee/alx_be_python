#!/usr/bin/env python3
"""
explore_datetime.py
Demonstrates working with Python's datetime module:
1. Display the current date and time.
2. Calculate and display a future date after adding a user-specified number of days.
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Get the current date and time, store in current_date,
    and print it in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # returning for reuse in calculate_future_date


def calculate_future_date(current_date):
    """
    Prompt the user for a number of days, calculate the future date,
    save in future_date, and print it as YYYY-MM-DD.
    """
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
