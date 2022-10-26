class Dog:

  is_cute = True
  all_dogs = []

  def __init__(self, data, roommate = None):
    self.name = data['name']
    self.age = data['age']
    self.breed = data['breed']
    Dog.all_dogs.append(self)
    self.roomate = roommate

  def bark(self):
    print(f"{self.name} makes a loud bark at their {self.rommate.name}")
    return self

  def birthday(self):
    self.age =+ 1
    print(f"{self.name} gets a special bday treat! They are now {self.age} year(s) old")
    return self

  def __repr__(self):
    return f"{self.name} is a dog object {self.age} {self.breed}"

  @classmethod
  def every_dog_bark(cls):
      for one_dog in cls.all_dogs:
          print(one_dog.name)

  @staticmethod
  def years_to_dog_years(years):
    return years * 7

class Human:
  def __init__(self):
    self.name = name
    

Branden = Human("Brendan")
Spencer = Human("Spencer")
dog_3 = Dog(dog_1, 'Branden')
dog_4 = Dog(dog_2, 'Spencer')

print(dog_3)

dog_3.bark().bark().bark().birthday().bark()
Dog.every_dog_barks()
print(Dog.all_dogs)
