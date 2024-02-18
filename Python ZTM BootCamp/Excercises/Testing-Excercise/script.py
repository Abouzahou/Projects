from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)

def run_guess(guess,answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False #more consistency for testing later on
    
if __name__ == '__main__':  #Avoid the script running while testing           
    answer = randint(1, 10)
    while True:
            try:
                guess = int(input('guess a number 1~10:  '))
                if(run_guess(guess,answer)):
                    break
            except ValueError:
                print('please enter a number')
                continue      
        