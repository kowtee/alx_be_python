# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the bank account with an optional initial balance.
        Default balance is 0 if no amount is given.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the balance if sufficient funds exist.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")
