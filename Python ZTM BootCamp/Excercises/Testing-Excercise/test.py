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