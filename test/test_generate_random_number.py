import unittest
from unittest.mock import patch
from guess_number_game import guess_number_game 

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = guess_number_game(1234)
        
    def test_generate_random_number_randomness(self):
        random_number1 = self.game.generate_random_number()
        random_number2 = self.game.generate_random_number()
        random_number3 = self.game.generate_random_number()
        random_number4 = self.game.generate_random_number()
        self.assertNotEqual(random_number1, random_number2)
        self.assertNotEqual(random_number1, random_number3)
        self.assertNotEqual(random_number1, random_number4)
        
    def test_generate_random_number_data_type(self):
        random_number = self.game.generate_random_number()
        result = isinstance(random_number, int)
        self.assertTrue(result)
        result = isinstance(random_number, float)
        self.assertFalse(result)
        result = isinstance(random_number, str)
        self.assertFalse(result)

    
if __name__ == '__main__':
    unittest.main()
