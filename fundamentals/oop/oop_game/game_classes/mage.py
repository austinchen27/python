from game_classes.human import Human

class Mage(Human):
  def __init__(self,name):
    super().__init__() #super letting us run the human class
    self.name = name
    self.health = 50
    self.mana = 15

  def attack(self,target):
    print(f"{self.name} is attacking {target.name}")
    target.defend(self.mana)

# mage1 = Mage("Albus")
# mage2 = Mage("Gandalf")

# mage1.attack(mage2)

