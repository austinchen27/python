class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Your balance is: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
            return self
        else:
            return self

# @classmethod
# def bank_info(cls, int_rate, balance):
#     cls.info.append(int_rate)
#     cls.info.append(balance)
#     print(cls.info)

account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.01, 500)

account1.deposit(500).deposit(500).deposit(500).withdrawal(
    300).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdrawal(250).withdrawal(350).withdrawal(
    150).withdrawal(150).yield_interest().display_account_info()
