# multiplication_table.py
# Prints the multiplication table for a user-supplied number from 1 to 10.

# Prompt for the number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
