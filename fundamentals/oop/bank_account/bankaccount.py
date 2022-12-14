class BankAccount:
  banks = []

  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = 0
    BankAccount.banks.append(self)

  def deposit(self, amount):
    self.balance = self.balance + amount
    print(f"Your new balance is $",self.balance,". Thank you for your deposit.")
    return self

  def withdraw(self, amount):
    if amount > self.balance:
      self.balance = self.balance - 5
      print("Insufficient funds: Charging a $5 fee.")
    else:
      self.balance = self.balance - amount
      print(f"After your withdrawal, you have $",self.balance,"remaining. Have a nice day.")
    return self

  def display_account_info(self):
    print(f"Your balance is ${self.balance}")

  def yield_interest(self):
    if self.balance > 0:
      self.balance = self.balance*(1+self.int_rate)
      return self
    return self

  @classmethod
  def account_info(cls):
    for account in cls.banks:
      account.display_account_info()

account1 = BankAccount(0.01, 500)
account2 = BankAccount(0.03, 10000)
account3 = BankAccount(0.01, 100)
account1.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest()
account2.deposit(500).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest()
account3.deposit(100).deposit(50).deposit(50).withdraw(500).yield_interest()

BankAccount.account_info()