class BankAccount:
    bank_name = "Bank of Traci"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            self.balance = self.balance
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

traci = BankAccount(.03, 750)
aaron = BankAccount(.07, 1000)

traci.deposit(250).deposit(50).deposit(1500).withdraw(250).yield_interest().display_account_info()

aaron.deposit(350).deposit(1200).withdraw(75).withdraw(200).withdraw(25).withdraw(120).yield_interest().display_account_info()

BankAccount.all_account_info()