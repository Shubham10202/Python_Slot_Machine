import random   #Python has a built-in module that you can use to make random numbers.

MAX_LINES = 3  
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {          #Dictionaries are used to store data values in key:value pairs.
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {          #dictionaries
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):     #def(it is keyword to define a function)- A function is a block of code which only runs when it is called.
                                                     # You can pass data, known as parameters, into a function.A function can return data as a result.
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:               #if- It is a conditional statement "if statement" is written by using the if keyword.
                break                                   #break- With the break statement we can stop the loop before it has looped through all the items:
        else:                                           #else- The else keyword catches anything which isn't caught by the preceding conditions.
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings , winning_lines                     #The return keyword is to exit a function and return a value.


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                                    #list
    for symbol, symbol_count in symbols.items():        #for loop- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).  
        for _ in range(symbol_count):                   #With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):                                #range- The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)                         #.append- The append() method appends an element to the end of the list.

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")                     #print- The print() function prints the specified message to the screen, or other standard output device.
                                                                  #The message can be a string, or any other object, the object will be converted into a string before written to the screen.
            else:
                print(column[row], end="")                  
        print()

def deposit():  #function deposit
    while True:                                                     #while loop- with the while loop we can execute a set of statements as long as a condition is true.
        amount = input("What would you like to deposit? $")         #input- Python provides a built-in function called input which takes the input from the user. 
        if amount.isdigit():                                        #isdigit()- The isdigit() method returns True if all the characters are digits, otherwise False.
            amount = int(amount)                                    #convertion to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a number. ")
    return amount


def get_number_of_lines():
    while True:                                                     
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")         
        if lines.isdigit():
            lines = int(lines)                                    
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number. ")
    
    return lines

def get_bet():
    while True:                                                     
        amount = input("How would you like to bet on each line? $")         
        if amount.isdigit():
            amount = int(amount)                                    
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number. ")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
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



def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer =="q":
            break
        balance += spin(balance)
        
    print(f"You left with${balance}")
main()
  
