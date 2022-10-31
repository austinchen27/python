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

    # def transfer(self, amount, user):
    #   user.make_deposit(amount)
    #   self.withdraw(amount)
    #   print(f"{amount} sent to {user.name}")
    #   return self


class User:

  def __init__(self, name, email, balance):
    self.name = name
    self.email = email
    self.balance = balance
    self.account = BankAccount(0.02, balance)

  def make_deposit(self, amount):
    self.account.deposit(amount)
    print(f"Deposited:{amount}")
    return self

  def make_withdrawal(self, amount):
    self.account.withdrawal(amount)
    print(f"Withdrawn:{amount}")
    return self

  def display_user_balance(self):
    self.account.display_account_info()
    return self

  # def money_transfer(self, amount, user):
  #   self.account.transfer(amount, user)
  #   return self

user1 = User("Austin","1@email.com","1000")
user2 = User("Ja", "2@email.com", "1000")

user1.display_user_balance()
# user2.money_transfer(50, user1).display_user_balance()


#Questions:
# 1. line 37 why does value have to be 0.02, rather than 'int_rate' or 'int_rate=0.02'
# 2. what is wrong with my money transfer