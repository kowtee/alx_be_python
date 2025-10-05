# main-0.py

import sys
from bank_account import BankAccount

def parse_command(arg):
    """
    Parse a single argument like "deposit:50" or "display".
    Returns (command, amount_or_None).
    """
    parts = arg.split(':')
    command = parts[0].strip().lower()
    amount = None
    if len(parts) > 1 and parts[1] != '':
        try:
            amount = float(parts[1])
        except ValueError:
            raise ValueError("Amount must be a number.")
    return command, amount

def main():
    account = BankAccount(100.0)  # Starting balance (adjust if you want)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command, amount = parse_command(sys.argv[1])
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    if command == "deposit":
        if amount is None:
            print("Please provide an amount, e.g. deposit:50")
            sys.exit(1)
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print("Error:", e)
            sys.exit(1)

    elif command == "withdraw":
        if amount is None:
            print("Please provide an amount, e.g. withdraw:20")
            sys.exit(1)
        try:
            ok = account.withdraw(amount)
        except ValueError as e:
            print("Error:", e)
            sys.exit(1)
        if ok:
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Use deposit, withdraw, or display.")
        sys.exit(1)

if __name__ == "__main__":
    main()
