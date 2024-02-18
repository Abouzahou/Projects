# def fib(num):
#     if num <= 1:
#         return num
#     else:
#         a, b = 0, 1
#         for _ in range(2, num + 1):
#             a, b = b, a + b
#         return b

# # Testing the function with different values of 'n'
# print("Fibonacci series up to n=10:\n")
# for i in range(11):
#     print(f"{i}: {fib(i)}")

#Range Method

# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a #pause a
#         temp = a #the paused/unchanged value of a
#         a = b # then  set a to be our new value of b
#         b = temp+b  #set b to be the old value of a plus the current value of b.

# for x in fib(20):
#     print(x)        

#List Method

def fib2(number):
    a = 0
    b = 1
    result = [] #adding list variable
    for i in range(number):
        result.append(a) #adding to the list
        temp = a 
        a = b 
        b = temp+b  
    return result

print(fib2(20))    