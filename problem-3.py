# Challenge: Create a BankAccount class with private attributes balance and methods to deposit and withdraw money.

class BankAccount:
    def __init__(self):
        self.__balance = 0  # private attribute, initialized to 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Withdrawal amount must be positive and cannot exceed balance.")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount()
print("Initial balance:", account.get_balance())

account.deposit(100)
print("Current balance:", account.get_balance())

account.withdraw(30)
print("Current balance:", account.get_balance())

account.withdraw(100)  # This will print an error message
print("Final balance:", account.get_balance())
