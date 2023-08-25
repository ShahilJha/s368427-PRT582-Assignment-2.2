import random
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich import print

class guess_number_game:
    def __init__(self, secret_number=None):
        self.secret_number = secret_number if secret_number else self.generate_random_number()
        self.attempts = 0
        self.console = Console()
        self.history = []
        
    def print_rules(self):
        with open("rules.md") as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)
    
    def generate_random_number(self):
        return "".join(random.sample("0123456789", 4))
    
    def check_guess(self):
        return True
    
    def compare_numbers(self, generated_number, guess_number):
        if not (isinstance(generated_number, int) and isinstance(guess_number, int)):
            raise ValueError("Both inputs must be integers")

        if not (1000 <= generated_number <= 9999 and 1000 <= guess_number <= 9999):
            raise ValueError("Both numbers must be 4-digit numbers")

        str_number1 = str(generated_number)
        str_number2 = str(guess_number)

        if str_number1 == str_number2:
            return "Same number"

        crosses = ""
        circles = ""

        for i in range(4):
            if str_number1[i] == str_number2[i]:
                circles += "O"
            elif str_number1[i] in str_number2:
                crosses += "X"

        self.history.append([guess_number, crosses, circles])
 
    def start_game(self):
        self.print_rules()
        flag = True
        print("[bold magenta]Press Enter to Start the Game: [/bold magenta]")
        input()
        # while flag:
        #     return True
            
    


game = guess_number_game()
game.start_game()