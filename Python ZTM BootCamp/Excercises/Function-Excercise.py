# create a function called high even , will take a list
# print highest even, give list

def highest_even(list):
  even = []
  for item in list:
    if item % 2 == 0:
      even.append(item)
  return max(even)

print(highest_even([5, 3, 2, 30, 10, 20]))