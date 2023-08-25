import random
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich import print


class guess_number_game:
    def __init__(self, secret_number=None):
        self.generated_number = (
            secret_number if secret_number else self.generate_random_number()
        )
        self.attempts = 0
        self.console = Console()
        self.table = Table(title="HISTORY",show_header=True, header_style="bold magenta")
        self.table.add_column("Guesses", width=12, justify="center")
        self.table.add_column("Crosses", width=12, justify="center")
        self.table.add_column("Circles", width=12, justify="center")

    def prep_game(self):
        self.attempts = 0
        self.table = Table(title="HISTORY",show_header=True, header_style="bold magenta")
        self.table.add_column("Guesses", width=12, justify="center")
        self.table.add_column("Crosses", width=12, justify="center")
        self.table.add_column("Circles", width=12, justify="center")
        self.print_rules()

    def print_rules(self):
        with open("rules.md") as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)

    def generate_random_number(self):
        generated_value = random.randint(1000, 9999)
        print(f'RANDOM NUM -> {generated_value}')
        return generated_value

    def compare_guess(self, guess_number):
        if not (
            isinstance(self.generated_number, int) and isinstance(guess_number, int)
        ):
            raise ValueError("Both inputs must be integers")

        if not (1000 <= self.generated_number <= 9999 and 1000 <= guess_number <= 9999):
            raise ValueError("Both numbers must be 4-digit numbers")

        str_number1 = str(self.generated_number)
        str_number2 = str(guess_number)

        self.attempts += 1
        if str_number1 == str_number2:
            return True

        crosses = ""
        circles = ""

        for i in range(4):
            if str_number1[i] == str_number2[i]:
                circles += "O"
            elif str_number1[i] in str_number2:
                crosses += "X"

        self.table.add_row(str(guess_number), str(crosses), str(circles))
        self.console.print(self.table)
        return False

    def check_game_finish_input_option(self, input):
        if input not in ["q", "Q", "r", "R"]:
            raise ValueError("Value should be either Q or R.")

        if input.lower() == "q":
            return False
        else:
            return True

    def start_game(self):
        self.prep_game()
        flag = True
        print("[bold magenta]Please Enter to Start the Game. [/bold magenta]")
        input()
        while flag:
            input_number = int(input("Input your guessed number : "))
            compare_result = self.compare_guess(input_number)

            if compare_result == True:
                print(
                    f"[bold red]Congratulations!!! \nYou guessed the correct number in {self.attempts} attemps!![/bold red]"
                )
                print("[bold magenta]Enter q or Q to quit the game. \n Enter r or R to replay the game.[/bold magenta]")
                
                option_input = input("Input option: ")
                self.console.clear()

                if option_input:
                    self.prep_game()
                else:
                    flag = False
        exit()


game = guess_number_game()
game.start_game()
