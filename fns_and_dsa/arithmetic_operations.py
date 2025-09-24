# arithmetic_operations.py
# Implements perform_operation(num1, num2, operation)

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Parameters
    ----------
    num1 : float
    num2 : float
    operation : str - 'add', 'subtract', 'multiply', or 'divide'

    Returns
    -------
    float or str
        The numerical result of the operation, or a string error message
        for division by zero or unknown operation.
    """
    # normalize operation string for safety
    op = str(operation).strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Unknown operation"


# Optional: quick manual test when running this file directly.
# This block will NOT run when another file imports perform_operation().
if __name__ == "__main__":
    print("Quick test of perform_operation:")
    print("5 + 6  =>", perform_operation(5, 6, "add"))
    print("5 / 0  =>", perform_operation(5, 0, "divide"))
    print("5 ^ 6  =>", perform_operation(5, 6, "power"))  # unknown op
