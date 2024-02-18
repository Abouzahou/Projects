#excercise-find duplicates

list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = [] #creating a duplicates list
for value in list: #normal format of loops
  #list.count(value) counts how many times an item is in the list
  if list.count(value) > 1 and value not in duplicates:
    duplicates.append(value)
print(duplicates)