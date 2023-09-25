class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}"

# Create an instance of the BankAccount class
my_account = BankAccount("12345", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
print(my_account.display_balance())
print(my_account.deposit(500.0))
print(my_account.withdraw(200.0))
print(my_account.display_balance())