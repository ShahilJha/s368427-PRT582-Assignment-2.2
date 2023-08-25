import unittest
from unittest.mock import patch
from guess_number_game import guess_number_game 

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = guess_number_game(1234)

    def test_compare_guess_correct(self):
        self.assertTrue(self.game.compare_guess(1234))

    def test_compare_guess_incorrect(self):
        self.assertFalse(self.game.compare_guess(5678))
    
    def test_compare_guess_input_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            self.game.compare_guess(guess_number="1234")
        self.assertEqual(
            str(exception_context.exception),
            "Both inputs must be integers"
        )
    
    def test_compare_guess_generated_number_exception(self):
        self.game.generated_number = "1234"
        with self.assertRaises(ValueError) as exception_context:
            self.game.compare_guess(guess_number=1234)
        self.assertEqual(
            str(exception_context.exception),
            "Both inputs must be integers"
        )
    
    def test_compare_guess_input_value_range_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            self.game.compare_guess(guess_number=12345)
        self.assertEqual(
            str(exception_context.exception),
            "Both numbers must be 4-digit numbers"
        )
        
    def test_compare_guess_generated_number_value_range_exception(self):
        self.game.generated_number = 12345
        with self.assertRaises(ValueError) as exception_context:
            self.game.compare_guess(guess_number=1234)
        self.assertEqual(
            str(exception_context.exception),
            "Both numbers must be 4-digit numbers"
        )
   

if __name__ == '__main__':
    unittest.main()
