class BankAccount:

  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance - amount > 0:
      self.balance -= amount
      return self
    else:
      self.balance -= 5
      print("Insufficient funds: Charging a $5 fee.")
      return self

  def display_account_info(self):
    print(f"Your balance is ${self.balance}")

  def yield_interest(self):
    if self.balance > 0:
      self.balance = self.balance*(1+self.int_rate)
      return self
    return self

  def transfer(self, amount, user):
    user.make_deposit(amount)
    self.withdraw(amount)
    print(f"Sent {user.name}: ${amount}")
    return self


class User:

  def __init__(self, name, email, balance):
    self.name = name
    self.email = email
    self.balance = balance
    self.account = BankAccount(int_rate=0.02, balance=0)

  def make_deposit(self, amount):
    self.account.deposit(amount)
    print(f"{self.name} Deposited: ${amount}")
    return self

  def make_withdrawal(self, amount):
    self.account.withdrawal(amount)
    print(f"{self.name} Withdrawn: ${amount}")
    return self

  def display_user_balance(self):
    self.account.display_account_info()
    return self

  def transfer_money(self, amount, other_user):
    self.account.transfer(amount, other_user)
    return self

user1 = User("Austin Chen", "achen@email.com", 100)
user2 = User("Natasha Romanoff", "nromanoff@email.com", 50)
user1.display_user_balance()
user2.transfer_money(10, user1).display_user_balance()
