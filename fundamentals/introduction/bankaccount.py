class BankAccount:
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = 0
  def deposit(self, amount):
    self.balance = self.balance + amount
    print(f"Your new balance is $", self.balance, ". Thank you for your deposit.")
    return self
  def withdraw(self, amount):
    if amount > self.balance:
      self.balance = self.balance - 5
      print("Insufficient funds: Charging a $5 fee")
    else:
      self.balance = self.balance - amount
      print(f"After your withdrawal, you have $", self.balance, " remaining. Have a nice day.")
      return self
  def display_account_info(self):
    print("Your balance is $", self.balance," and your interest rate is ", self.int_rate)
  def yield_interest(self):
    self.balance = self.balance*(1+self.int_rate)
    return self

account1 = BankAccount(0.01, 500)
account2 = BankAccount(0.03, 10000)
account3 = BankAccount(0.01, 100)
account1.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest().display_account_info()
account2.deposit(500).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
account3.deposit(100).deposit(50).deposit(50).withdraw(500).yield_interest().display_account_info()
