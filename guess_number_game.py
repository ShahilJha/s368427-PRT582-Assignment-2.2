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
        # open the rules.md file and assign to varaible
        with open("rules.md") as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)

    # Generate a random four-digit number
    def generate_random_number(self):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Shuffle the digits
        random.shuffle(digits) 
        # Take the first 4 digits
        generated_value = int(''.join(map(str, digits[:4])))  
        return generated_value
    
    # method to compare numbers and generate hint
    def get_hint(self, str_num1, str_num2):
        crosses = ""
        circles = ""
        # iterate the string casted numver generate hints
        for i in range(4):
            if str_num1[i] == str_num2[i]:
                circles += "O"
            elif str_num1[i] in str_num2:
                crosses += "X"
        data = {
            'O': circles,
            'X': crosses
        }
        return data

    # Compare the player's guess with the generated number
    def compare_guess(self, guess_number):
        # Check input validity
        if not (
            isinstance(self.generated_number, int) and isinstance(guess_number, int)
        ):
            raise ValueError("Both inputs must be integers")
        
         # Convert numbers to strings for comparison
        temp_str_number1 = str(self.generated_number)
        temp_str_number2 = str(guess_number)
        
        # resolve length issue if the front of any number is 0
        str_number1 = temp_str_number1 if len(temp_str_number1)==4 else ('0' + temp_str_number1)
        str_number2 = temp_str_number2 if len(temp_str_number2)==4 else ('0' + temp_str_number2)
        
        # check the numbers are in range and are of 4 digits
        if not (len(str_number1) == 4 and len(str_number2) == 4):
            raise ValueError("Both numbers must be 4-digit numbers")
        

        # Increment the number of attempts
        self.attempts += 1
        if str_number1 == str_number2:
            return True

        # get hint
        hint = self.get_hint(str_number1, str_number2)

        # add the hint to table
        self.table.add_row(str(guess_number), hint['X'], hint['O'])
        return False

    # Check if the player wants to quit or replay
    def check_game_finish_input_option(self, input):
        if input not in ["q", "Q", "r", "R"]:
            raise ValueError("Value should be either Q or R (in lowercase or uppercase).")

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
        print("[bold magenta]You can Enter 'q' or 'Q' any time to quit the game.\nPlease Enter to Start the Game. [/bold magenta]")
        input()
        # Game loop
        while True:
            # take user input
            user_input =input("Input your guessed number : ")
            # Quit game if the input is q
            if user_input.lower() == "q":
                break
            
            # converting the input to integer
            input_number = int(user_input)
            # compare the user input with the generated number
            compare_result = self.compare_guess(input_number)
            # print the history of user input
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
                    break
        # Exit the game
        exit()
