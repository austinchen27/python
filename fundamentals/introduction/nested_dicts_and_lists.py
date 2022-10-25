# 1.1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15

# 1.2
students[0][2] = 'Bryant'
print(students)

# 1.3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 1.4
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)


# 2. Iterate Through a List of Dictionaries
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def iterateDictionary(students):
  for each_key in students:
    print(each_key)
iterateDictionary(students)


# 3. Get Values From a List of Dictionaries
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# method #1
def iterateDictionary2(first_name,students):
  for i in range(len(students)):
    print(students[i][first_name])
iterateDictionary2('first_name',students)

def iterateDictionary3(last_name,students):
  for i in range(len(students)):
    print(students[i][last_name])
iterateDictionary2('last_name',students)

# method #2
def iterateDictionary(some_list):
  for i in (students):
    print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
iterateDictionary(students)

def iterateDictionary2(some_list):
  for i in (some_list):
    print(f"{i['first_name']}")
  for i in (some_list):
    print(f"{i['last_name']}")
iterateDictionary2(students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
  for key in dict.keys():
    print(len(dict[key]), key)
    for locations in dict[key]:
      print(locations)
printInfo(dojo)







