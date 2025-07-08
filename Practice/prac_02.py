from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = 0 #private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} deposited successfully!')
        else:
            print(f'{amount} invalid amount!')

    def get_balance(self):
        return self.__balance

    def _deduct_balance(self, amount):
        self.__balance -= amount

    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._deduct_balance(amount)
            print(f'{amount} withdrawn successfully from savings!')
        else:
            print('Insufficient balance!')


class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._deduct_balance(amount)
            print(f'{amount} withdrawn successfully from current account!')
        else:
            print('Insufficient balance!')

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    # def show_accounts(self):
    #     for account in self.accounts:
    #         print(account.account_number)
    def show_accounts(self):
        for acc in self.accounts:
            print(f"{acc.__class__.__name__} - {acc.account_number} - Balance: ₹{acc.get_balance()}")


customer_01 = Customer('Nikhil')

savings = SavingsAccount('sav123','Nikhil')
customer_01.add_account(savings)

savings.deposit(10000)
savings.withdraw(2500)
print(savings.get_balance())

customer_01.show_accounts()