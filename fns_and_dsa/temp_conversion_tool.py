#!/usr/bin/env python3
"""
temp_conversion_tool.py
Demonstrates variable scope with global conversion factors.
"""

# ---- Global conversion factors (exact names) ----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """Prompt user for temperature and convert."""
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric input
    if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
        # raise exactly this message for the checker
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temp_input)
    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): "
    ).strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        # keep a generic error if unit is wrong
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
