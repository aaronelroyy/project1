import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winning(columns, lines, bet, values):
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


def get_slot(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():  # for key, value in dictionary.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []  # nested lists
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copies a list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], " | ", end="", sep="")  # columns[i][row]
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("what would like to deposit? : $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("enter a number")

    return amount


def get_number_of_line():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter valid lines")
        else:
            print("enter a number")


def get_bet(tot_amount, lines):
    while True:
        bet_amount = input("what would like to bet : $ ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET and bet_amount * lines <= tot_amount:
                return bet_amount
            elif tot_amount > 0:
                print(
                    f"Amount entered must be between ${MIN_BET}-${MAX_BET} AND cummulative total must be within the balance amount of ${tot_amount}. Try again "
                )
            else:
                print(f"balance is ${tot_amount}")
        else:
            print("enter a number")


def spin(balance):
    lines = get_number_of_line()
    bet = get_bet(balance, lines)
    total_bet = bet * lines
    print(f"you are betting ${bet} on {lines} lines. Total bet amount : ${total_bet}")
    slots = get_slot(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    if winnings > 0:
        print(f"You won on", *winning_lines)
    else:
        print("ergo You lost the game")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin_it = input("press enter to spin (q to quit)")
        if spin_it == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")


if __name__ == "__main__":
    main()
