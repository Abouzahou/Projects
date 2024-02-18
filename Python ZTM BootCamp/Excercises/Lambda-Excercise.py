# lambda Expressions Excercise
# create a lambda exp that will square the list
my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

#list sorting, sorted based on the second value
a = [(0,2), (4,3), (9,9), (10,-1)]
#sort takes a key value(index) for location of sort
print(sorted(a, key=lambda x: x[1]))