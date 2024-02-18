#Write a prog called random.py
#ask user to guess a number between 1 and 10
#randomly generate a number 1 to 10
#user will keep guessing until he gets the number right

#we also want the user to be able to 
#change parameters from terminal
#Can be completely customized from the terminal
#Run: python3 Terminal-random_game.py param1 param2
#param1 = starting number
#param2 = last number
#Ex. python3 Terminal-random_game.py 5 20

from random import randint

import sys
#we set randint parameters to give access to user manipluation
rand_num = randint(int(sys.argv[1]),int(sys.argv[2]))
param1 = int(sys.argv[1])
param2 = int(sys.argv[2])
while True:
    try:
        guess = int(input(f'Guess a number between {sys.argv[1]} and {sys.argv[2]} '))

        if param1 < guess < param2: # Same as: guess > 0 and guess < 11
            if guess == rand_num:
                print('you are a genius!')
                break
        else:
            print(f'HEY! Only {sys.argv[1]} ~ {sys.argv[2]} !')
    except ValueError:
        print('please enter a number')
        continue
