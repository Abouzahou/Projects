#Testing Excercise
#Will be using Terminal and 2 Files: script.py / Test.py
#Also the files used are located in the Excercise/Testing Excercises Folder
#script.py:

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
        
###################################################################
#Test.py
            
import unittest
import script

class TestGame(unittest.TestCase):
        
    def test_input(self):
        # answer = 5 #param1
        # guess = 5 #param2
        # result = script.run_guess(answer,guess) 
        result = script.run_guess(5,5) #Check if answer==guess
        self.assertTrue(result) #Check if guess==answer
        
    def test_input_wrong_guess(self): 
        result = script.run_guess(5,0) #Check if guess != answer
        self.assertFalse(result) 
        
    def test_input_wrong_number(self): 
        result = script.run_guess(5,11) #Check if guess != answer
        self.assertFalse(result)

    def test_input_wrong_type(self): 
        result = script.run_guess(5,'11') #Check if guess is a string
        self.assertFalse(result)
        
        
if __name__ == '__main__': 
    unittest.main() 