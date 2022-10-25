# what is a class?
#Blueprint

# class Dog:
#   def __init__(self, name, age, breed_param): #          >  constructor
#     self.name = name
#     self.age = age
#     self.breed = breed_param

dog_3 = Dog("Minnie",4,"Corgi")
dog_4 = Dog("Max",4,"Great Dane")

# #print(dog_3)
# print(dog_3)
# print(dog_3.name) 

#what is an attribute?
# - a characteristic of our object, some piece of data we are tracking about our object
# - ie breed, age, color for a dog

#what is a method?
# a function belonging to the class -- what our objects can do




# class example #2
dog_1 = {
  name: "Mr. Worldwide"
  age: 34
  breed: "Pitbull"
}

class Dog:
  def __init__(self, data):
    self.name = data['name']
    self.age = data['age']
    self.breed = data['breed']

  def bark(self):
    print(f"{self.name} makes a loud bark")

  def birthday(self):
    self.age += 1
    print(f"{self.name} gets a special bday treat! They are now {self.age} years old.")
    return self

  def __repr__(self) -> str:
    return f"{self.name} is a dog object {self.age} {self.breed}"

dog_3 = Dog(dog_1)
dog_4 = Dog(dog_2)

print(dog_3)

dog_3.bark().bark().bark().bark().birthday().bark()


