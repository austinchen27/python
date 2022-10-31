# 1 Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element).

def countdown(num):
  list = []
  for i in range(num,-1,-1):
    list.append(i)
  return list

print(countdown(5))

# 3 First Plus Length - Create a function that accepts a list and 
# returns the sum of the first value in the list plus the list's length.

def firstPlusLength(num):
  result = num[0] + len(num)
  return result

val = [1,2,3,4,5]
print(firstPlusLength(val))


# 4 Values Greater than Second - Write a function that accepts a list and 
# creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

def valGreaterThan(list):
  newlist = []
  if len(list) < 2:
    return False
  for i in range(0,len(list)):
    if list[i] > list[1]:
      newlist.append(list[i])
  return newlist

list = [1, 3, 5, 7, 9, 11]
print(valGreaterThan(list))


# 5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and 
# whose values are all the given value.

def length_and_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

result = length_and_value(4, 7)
print(result)

  # (4,5) size 4 value 5

