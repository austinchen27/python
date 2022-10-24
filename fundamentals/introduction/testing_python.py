from multiprocessing.spawn import old_main_modules
import random
from tkinter.messagebox import askquestion

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif (day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')

for i in range(10):
    print(i)


print("Hello " + str(42))

total = 35
user_val = "26"
total = total + int(26)
print(total)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


first_name = "Austin"
last_name = "Chen"
age = 32
profession = "Software Developer"
years_experience = 7

greeting = "Hello my name is", first_name, last_name
print(greeting)

age = "I am", age, "years old"
print(age)

print("I work as a", profession)


def full_name():
name1 = full_name("Austin_Chen")
print(name1)
