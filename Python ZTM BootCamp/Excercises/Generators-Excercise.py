#Creating our own range function
class MyGen():
    current = 0
    def  __init__(self, first, last):  #init func to have first and last parameters
        self.first=first
        self.last=last
        MyGen.current = self.first #allows us to use the current number as the start for the iteration
    def __iter__(self): #be able to iterate through the MyGen Object
        return self
    def __next__(self): #be able to get the 'next' value on each iteration
        if MyGen.current < self.last: 
            num = MyGen.current
            MyGen.current += 1 #loop and constantly increase the current number
            return num #keep returning the number till its more than self.last
        raise StopIteration #when number is higher than self.last then it will exit

gen = MyGen(0,100)
for i in gen:
    print(i)        
