import unittest
from unittest.mock import patch
from guess_number_game import guess_number_game 

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = guess_number_game(1234)
        
    def test_get_hint_different_numbers(self):
        str_num1 = "1234"
        str_num2 = "9876"
        result = self.game.get_hint(str_num1, str_num2)
        compare_data = {
            'O': "",
            'X': ""
        }
        self.assertEqual(result, compare_data)
        
    def test_get_hint_different_places(self):
        str_num1 = "1234"
        str_num2 = "4871"
        result = self.game.get_hint(str_num1, str_num2)
        compare_data = {
            'O': "",
            'X': "XX"
        }
        self.assertEqual(result, compare_data)
    
    def test_get_hint_some_correct(self):
        str_num1 = "1234"
        str_num2 = "1874"
        result = self.game.get_hint(str_num1, str_num2)
        compare_data = {
            'O': "OO",
            'X': ""
        }
        self.assertEqual(result, compare_data)
    
    def test_get_hint_some_correct_some_different(self):
        str_num1 = "1234"
        str_num2 = "1324"
        result = self.game.get_hint(str_num1, str_num2)
        compare_data = {
            'O': "OO",
            'X': "XX"
        }
        self.assertEqual(result, compare_data)
        


if __name__ == '__main__':
    unittest.main()
