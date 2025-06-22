import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 50
ROWS = 3
COLUMNS = 3

symbol_count = {
    "🍇": 3,
    "🍉": 4,
    "🍎": 5,
    "🍊": 6
}

symbol_values = {
    "🍇": 6,
    "🍉": 5,
    "🍎": 4,
    "🍊": 3
}

def get_slotmachine_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    column = []
    for _ in range(columns):
        col = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            col.append(value)
        column.append(col)

    return column

def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def deposit():
    while True:
        balance = input("Please enter the amount you want to deposit: ")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
        else:
            print("Please, enter a valid amount in number.")
    return balance

def input_bet_lines():
    while True:
        line = input("Enter the number of lines you want to bet on (1-3): ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Please, enter a valid number of lines.")
        else:
            print("Please, enter the number of lines in number.")
    return line

def input_bet():
    while True:
        bet_amount = input("Enter the amount you would like to bet: ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print("Please, enter a valid bet amount from $50 to $1000.")
        else:
            print("Please, enter your bet amount in number.")
    return bet_amount

def spin(balance):
    if balance < MIN_BET:
        print("⚠️ Not enough balance to place even the minimum bet.")
        return None

    line = input_bet_lines()
    while True:
        bet = input_bet()
        total_bet = bet * line
        if total_bet > balance:
            print("❌ You don't have sufficient funds for this bet.")
        else:
            break

    print(f"You have made a bet of {bet}$ on {line} lines.")
    print(f"Total bet amount is {total_bet}$")
    slots = get_slotmachine_spin(ROWS, COLUMNS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots, line, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance < MIN_BET:
            print("⚠️ Insufficient balance to continue. Game over!")
            break

        user_input = input("Press enter to spin (q to quit): ")
        if user_input == "q":
            break

        spin_result = spin(balance)
        if spin_result is None:
            break
        balance += spin_result

main()
