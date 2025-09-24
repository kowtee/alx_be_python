#!/usr/bin/env python3
"""
temp_conversion_tool.py
Demonstrates variable scope and global conversion factors for
temperature conversion between Celsius and Fahrenheit.
"""

# ----- Global conversion factors -----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9      # (F − 32) * 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5      # (C * 9/5) + 32


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Prompt the user for a temperature and its unit, validate input,
    and print the converted temperature.
    """
    # Get temperature value
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric input
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Get unit (C or F)
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
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
