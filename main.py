# 2024.01.16
# Exercises:

# 1. Create a class method to return the factorial of a given number.
class MyClass:
    @classmethod
    def factorial(cls, number):
        if number < 0:
            raise ValueError('Number must be a non-negative.')
        if number == 0 or number == 1:
            return 1
        else:
            return number * cls.factorial(number - 1)


given_number = MyClass()
print(given_number.factorial(8))
print(given_number.factorial(18))
print(given_number.factorial(7))
print(given_number.factorial(1))


# 2. Create a class method to return the reversed string of a given string.

class OtherClass:
    @classmethod
    def return_reversed_string(cls, string):
        reversed_string = string[::-1]
        return reversed_string


print(OtherClass.return_reversed_string('Hello there!'))
print(OtherClass.return_reversed_string('Gerda'))

# 3. Create a Python class named BankAccount that demonstrates the use of instance methods, class methods, and static
# methods. The class and its methods should provide functionality as described below. After implementing the class,
# create instances and use all the methods to showcase their functionality.
#
# Class Specification
#
# Class Name: BankAccount
#
# Instance Attributes: owner: The name of the account owner (a string). balance: The account balance (a float).
# Instance Method: show_balance: Prints the current balance of the account.
#
# Class Attribute: total_accounts: A class-level attribute that tracks the total number of BankAccount instances
# created.
#
# Class Method: get_total_accounts: Returns the total number of BankAccount instances.
#
# Static Method: validate_amount: Accepts an amount and returns True if it is a positive number; otherwise,
# it returns False.
#
# Task for Students:
#
# Implement the BankAccount class as per the specifications given above.
# Create Instances: Create at least two instances of BankAccount with different owners and balances.
# Use Instance Method: Use the show_balance method for each instance to display the account balance.
# Use Class Method: Use the get_total_accounts method to display the total number of bank accounts created.
# Use Static Method: Use the validate_amount method to validate a couple of amounts (one positive and one negative)
# to demonstrate how the method works.


class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

        BankAccount.total_accounts += 1

    def show_balance(self):
        return f'The balance of {self.owner} is {self.balance}'

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def transfer(self, account_second, param):
        pass


account1 = BankAccount('Tadas', 100)
account2 = BankAccount('Tomas', 500)
print(account1.show_balance())
print(account2.show_balance())
print(f'In total there are {BankAccount.get_total_accounts()} bank accounts.')
print(f'Is 80 is valid amount? {BankAccount.validate_amount(80)}')
print(f'Is -20 is valid amount? {BankAccount.validate_amount(-20)}')

# 4. Create a simple bank account class, BankAccount, with the following specifications:
#
# The BankAccount class should have an attribute balance which starts at 0.
# It should have an instance method deposit that allows an amount to be added to the balance.
# It should have an instance method withdraw that allows an amount to be taken from the balance. If the balance is less
# than the withdrawal amount, print a message that says "Insufficient funds".
# Add a class method from_balance that takes a starting balance as an argument and returns a new BankAccount instance
# with that starting balance.
# Add a static method transfer that takes two BankAccount instances and an amount as arguments. It should withdraw the
# amount from the first account and deposit it into the second account.


class BankAccount2:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print('Insufficient funds.')
            return self.balance

    @classmethod
    def from_balance(cls, balance):
        return cls(balance)

    @staticmethod
    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)


account_first = BankAccount2(200)
account_second = BankAccount2(300)
print(account_first.balance)
print(account_second.balance)
BankAccount2.transfer(account_first, account_second, 25)
print(account_first.balance)
print(account_second.balance)
account_first.withdraw(80)
print(account_first.balance)


