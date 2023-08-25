# Import the required modules and classes
import random  # Module for generating random numbers
from rich.console import Console  # Importing Console class from rich library
from rich.table import Table  # Importing Table class from rich library
from rich.markdown import Markdown  # Importing Markdown class from rich library
from rich import print  # Importing print function from rich library

# Define a class for the Guess the Number game
class guess_number_game:
    # Constructor to initialize the game instance
    def __init__(self, secret_number=None):
        # Generate a random number if no secret number is provided
        self.generated_number = (
            int(secret_number) if secret_number else self.generate_random_number()
        )
        # Initialize the number of attempts and create console and table objects
        self.attempts = 0
        self.console = Console()
        self.table = Table(title="HISTORY", show_header=True, header_style="bold magenta")
        self.table.add_column("Guesses", width=12, justify="center")
        self.table.add_column("Crosses", width=12, justify="center")
        self.table.add_column("Circles", width=12, justify="center")

    # Prepare the game instance for a new game
    def prep_game(self):
        self.attempts = 0
        # Recreate the table for displaying history
        self.table = Table(title="HISTORY", show_header=True, header_style="bold magenta")
        self.table.add_column("Guesses", width=12, justify="center")
        self.table.add_column("Crosses", width=12, justify="center")
        self.table.add_column("Circles", width=12, justify="center")
        # Print game rules from a markdown file
        self.print_rules()

    # Print game rules from a markdown file
    def print_rules(self):
        with open("rules.md") as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)

    # Generate a random four-digit number
    def generate_random_number(self):
        generated_value = random.randint(1000, 9999)
        return generated_value

    # Compare the player's guess with the generated number
    def compare_guess(self, guess_number):
        # Check input validity
        if not (
            isinstance(self.generated_number, int) and isinstance(guess_number, int)
        ):
            raise ValueError("Both inputs must be integers")

        if not (1000 <= self.generated_number <= 9999 and 1000 <= guess_number <= 9999):
            raise ValueError("Both numbers must be 4-digit numbers")

        # Convert numbers to strings for comparison
        str_number1 = str(self.generated_number)
        str_number2 = str(guess_number)

        # Increment the number of attempts
        self.attempts += 1
        if str_number1 == str_number2:
            return True

        # Compare digits and update the table
        crosses = ""
        circles = ""
        for i in range(4):
            if str_number1[i] == str_number2[i]:
                circles += "O"
            elif str_number1[i] in str_number2:
                crosses += "X"

        self.table.add_row(str(guess_number), str(crosses), str(circles))
        return False

    # Check if the player wants to quit or replay
    def check_game_finish_input_option(self, input):
        if input not in ["q", "Q", "r", "R"]:
            raise ValueError("Value should be either Q or R.")

        # return false if to quit the game
        if input.lower() == "q":
            return False
        # return true to replay the game
        else:
            return True

    # Start the game
    def start_game(self):
        # Prepare the game for the first round
        self.prep_game()
        flag = True
        print("[bold magenta]Please Enter to Start the Game. [/bold magenta]")
        input()
        # Game loop
        while flag:
            input_number = int(input("Input your guessed number : "))
            compare_result = self.compare_guess(input_number)
            self.console.print(self.table)

            # Check if the player guessed correctly
            if compare_result == True:
                print(
                    f"[bold red]Congratulations!!! \nYou guessed the correct number in {self.attempts} attempts!![/bold red]"
                )
                print("[bold magenta]Enter q or Q to quit the game.\nEnter r or R to replay the game.[/bold magenta]")
                
                # Ask the player to quit or replay
                option_input = input("Input option: ")
                
                # variable to check whether to quit or replqy the game
                game_flow_flag = self.check_game_finish_input_option(option_input)
                
                # print the table with the input history
                self.console.clear()

                # Restart or quit the game based on player's choice
                if game_flow_flag:
                    self.prep_game()
                else:
                    flag = False
        # Exit the game
        exit()
