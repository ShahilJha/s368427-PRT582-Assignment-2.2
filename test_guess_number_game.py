import unittest
from unittest.mock import patch
from guess_number_game import guess_number_game 

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = guess_number_game(1234)

    def test_compare_guess_correct(self):
        self.game.generated_number = 1234
        self.assertTrue(self.game.compare_guess(1234))

    def test_compare_guess_incorrect(self):
        self.game.generated_number = 1234
        self.assertFalse(self.game.compare_guess(5678))

    
    def test_check_game_finish_input_option_quit(self):
        self.assertFalse(self.game.check_game_finish_input_option("q"))

    
    def test_check_game_finish_input_option_replay(self):
        self.assertTrue(self.game.check_game_finish_input_option("r"))

    
    def test_check_game_finish_input_option_quit_case_insensitive(self):
        self.assertFalse(self.game.check_game_finish_input_option("Q"))

    
    def test_check_game_finish_input_option_replay_case_insensitive(self):
        self.assertTrue(self.game.check_game_finish_input_option("R"))

    
    def test_check_game_finish_input_option_invalid_then_quit(self):
        with self.assertRaises(ValueError):
            self.game.check_game_finish_input_option("invalid")
        self.assertFalse(self.game.check_game_finish_input_option("q"))

if __name__ == '__main__':
    unittest.main()
