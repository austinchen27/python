num1 = 42  # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # Boolean
string = 'Hello World'  # Strings
pizza_toppings = ['Pepperoni', 'Sausage',
                  'Jalepenos', 'Cheese', 'Olives']  # list
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # dictionary
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # log statement
print(pizza_toppings[1])  # log statement
pizza_toppings.append('Mushrooms')  # add
print(person['name'])  # log statement
person['name'] = 'George'  # list
person['eye_color'] = 'blue'  # list
print(fruit[2])  # log statement

if num1 > 45:  # conditional if/else
    print("It's greater")  # log statement
else:  # else
    print("It's lower")  # log statement

if len(string) < 5:  # conditional else/if
    print("It's a short word!")  # log statement
elif len(string) > 15:  # elif
    print("It's a long word!")  # log statement
else:  # else
    print("Just right!")  # log statement

for x in range(5):  # for loop
    print(x)  # log statement
for x in range(2, 5):  # for loop
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop
    print(x)  # log statement
x = 0  # variable declaration
while (x < 5):  # while-loop
    print(x)  # log statement
    x += 1  # increment

pizza_toppings.pop()  # remove
pizza_toppings.pop(1)  # remove

print(person)  # log statement
person.pop('eye_color')  # remove
print(person)  # log statement

for topping in pizza_toppings:  # for-loop
    if topping == 'Pepperoni':  # conditional
        continue  # continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # conditional
        break  # Break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()  # log statement


def print_hello_x_times(x):  # function
    for num in range(x):  # for loop
        print('Hello')  # log statement


print_hello_x_times(4)  # log statement


def print_hello_x_or_ten_times(x=10):  # funciton
    for num in range(x):  # conditional
        print('Hello')  # log statement


print_hello_x_or_ten_times()  # log statement
print_hello_x_or_ten_times(4)  # log statement


"""
Bonus section
"""

# print(num3)
age = 3
print(age)

# num3 = 72
num3 = 72
print(num3)

# fruit[0] = 'cranberry'
fruit = ['cranberry']
print(fruit[0])

# print(person['favorite_team'])


# print(pizza_toppings[7])
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives', 'Broccoli', 'Ham', 'Chicken']
print(pizza_toppings[7])

#   print(boolean)
a = 200
b = 30
if a > b:
    print("True")

# fruit.append('raspberry')
fruit = ['cranberry']
fruit.append('raspberry')
print(fruit)

# fruit.pop(1)
fruit = ['cranberry', 'raspberry']
fruit.pop(1)
print(fruit)

# drawer activity
drawers = ['documents', 'envelopes', 'pens']
print(drawers[1])

drawers[2] = "useless manuals"
print(drawers)

drawers[0] = drawers[1]
print(drawers)

# append activity
nums = [1, 2, 3, 4, 5]
nums.append(100)
nums.append(101)
nums.append(102)
print(nums)

my_list = [1, 'Zen', 'hi']
print(len(my_list))

some_nums = [44,56,2,3,12,19,6]
# print(len(some_nums))
# print(max(some_nums))
# print(sorted(some_nums))
some_nums.pop()
print(some_nums)

for count in range(0,5):
  print("looping =", count)

count = 0
while count <= 5:
  print("looping - ", count)
  count += 1

y = 3
while y > 0:
  print(y)
  y = y - 1
else:
  print("Final else statement")

for val in "string":
  if val == "i":
    break
  print(val)

snake_case = "All lower case, separated by underscores"
GLOBAL_VAR = "ALL CAPS"
#class names will be pascal case ie HumanClass

#Composite 
list = [1,2,3,4,5,6]
what we call arrays in js, a collection of elements accessed by index

#Dictionaries 
# a sequence of KEY VALUE PAIRS
# unindexed 

#del dog_dict['breed']
#color = dog_dict.pop('color')
#dog_dict.clear()

#tuples
#immutable list CANNOT BE CHANGED
tuple = (1,2,3,4,5)
print(tuple[0])

"""
None istead of null
not instead of !
or instead of ||
and instead of &&
is vs ==
   is used to check if both operands refer to the same object
"""








