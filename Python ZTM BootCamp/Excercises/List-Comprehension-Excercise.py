#List Comprehension Excercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#########
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
#########
# Using list comprehension
duplicates = list(set([value for value in some_list
                  if some_list.count(value) > 1]))

print(duplicates)