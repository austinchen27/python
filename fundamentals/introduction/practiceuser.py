class User:
  def __init__(self, first_name, last_name, email, age, is_a_rewards_member, gold_card_points):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_a_rewards_member = False
    self.gold_card_points = 0

  def user_info(self):
    # print(f"Hello, my name is {first_name} {last_name}. I can be reached at {email} and I am {age} years old.")
    print(self.first_name,)
    print(self.last_name,)
    print(self.email,)
    print(self.age,)
    print(self.is_a_rewards_member,)
    print(self.gold_card_points,)
    return self

  def enroll_user(self):
    if self.is_a_rewards_member == True:
      print(f"Sorry,",self.first_name,"has already enrolled")
    else:
      self.is_a_rewards_member = True
      self.gold_card_points = 200
      print("{} has been enrolled, point balance has been set to 200".format(self.first_name))
    return self

  def spend_points(self,points):
    if self.gold_card_points >= points:
      self.gold_card_points = self.gold_card_points
      print("{} Points have been spent. Your new point balance is {}. Have a good day {}.".format(points,self.gold_card_points-points,self.first_name))
    else:
      print("Sorry {}, Insufficient point balance, you only have {} points".format(self.first_name, self.gold_card_points))
    return self

user_1 = User("Austin", "Chen", "austinchen@email.com", 32, False, 0)
user_2 = User("Logan", "Howlett", "loganhowlett@email.com", 40, False, 0)
user_3 = User("Jean", "Grey", "jeangrey@email.com", 31, False, 0)

user_1.enroll_user().spend_points(50).user_info().enroll_user()
user_2.enroll_user().spend_points(80).user_info()
user_3.user_info().spend_points(40).enroll_user().spend_points(40)