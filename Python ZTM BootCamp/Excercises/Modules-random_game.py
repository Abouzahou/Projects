#Generate a number 1~10
#Get input from User
#Check if the input is 1~10
#Check if the guess is correct, if not, ask again

from random import randint

import sys
#Generate a number 1~10
rand_num = randint(1,10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10 "))

        if 0 < guess < 11: # Same as: guess > 0 and guess < 11
            if guess == rand_num:
                print('you are a genius!')
                break
        else:
            print('HEY! Only 1~10 !')
    except ValueError:
        print('please enter a number')
        continue
