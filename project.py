#Import the random module to generate random values.
import random
#Set constants for the maximum number of lines, maximum and minimum bets allowed in the game,
and the number of rows and columns in the slot machine.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
#Define dictionaries to store the symbol count and symbol value for the different symbols in the slot machine.
symbol_count = {
    "A": 20,
    "B": 40,
    "C": 60,
    "D": 80
}

symbol_value = {
    "A": 50,
    "B": 40,
    "C": 30,
    "D": 20
}

#Define a function to check the winnings for the current spin.
#It takes in the current columns in the slot machine, the number of lines bet on, the bet amount, and the symbol values.
#It returns the total winnings and the winning lines in a list.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
#Define a function to generate the spin in the slot machine.
#It takes in the number of rows and columns in the slot machine and the symbol count for each symbol.
#It returns a list of lists, where each list represents a column in the slot machine.

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#Define a function to print the current state of the slot machine.
#It takes in the current columns in the slot machine and prints each row and column of symbols.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
#Define a function to get the amount of money the player wants to deposit.
#It returns the deposit amount as an integer.

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#Define a function to get the number of lines the player wants to bet on
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines
#Define a function to get the amount the player wants to bet on each line.
#It takes no parameters.
#It prompts the player to enter a number between MIN_BET and MAX_BET.
#It returns the bet amount as an integer.

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount
#Define a function to check the winnings of a spin.
#It takes in the current columns in the slot machine, the number of lines bet on, the bet amount per line, and the symbol values.
#It calculates the winnings based on the winning combinations of symbols.
#It returns a tuple containing the total winnings and a list of the winning line numbers.

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#Define the main function to run the slot machine game.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()





         
         


