# 1 Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element).

def countdown(num):
    list = []
    for num in range(num, -1, -1):
        list.append(num)
    return list


2 Print and Return - Create a function that will receive a list with two numbers. 
Print the first value and return the second.

list = [5,10]
def num():
  x = list[0]
  y = list[1]
  print(x)
  return(y)


3 First Plus Length - Create a function that accepts a list and 
returns the sum of the first value in the list plus the list's length.

list = [5,10,15,20,25]
def sum():
  sum == list[0] + len(list)
  return(sum)



4 Values Greater than Second - Write a function that accepts a list and 
creates a new list containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. 
If the list has less than 2 elements, have the function return False

list = [5,10,15,20,25]
def greaterthan():
  if list[x] > list[1]:
    return list
  else:
    return False

5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, and 
whose values are all the given value.

def num(5,10):
  list = []
  
