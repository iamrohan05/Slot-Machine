import random
MAX_LINES=3
MAX_BET=1000
MIN_BET=50
ROWS=3
COLUMNS=3

symbol_count={
   "🍇":3,
   "🍉":4,
   "🍎":5,
   "🍊":6
}

def get_slotmachine_spin(rows,columns,symbols):
   all_symbols=[]
   for symbol, symbol_count in symbols.items():
      for _ in range(symbol_count):
         all_symbols.append(symbol)

   column=[]
   for _ in range(columns):
      col=[]
      current_symbols=all_symbols[:]

      for _ in range(rows):
         value=random.choice(current_symbols)
         current_symbols.remove(value)
         col.append(value)

      column.append(col)

   return column


      

def deposit():
    while True:
        balance=input("Please enter the amount you want to deposit: ")
        if balance.isdigit():
            balance=int(balance)

            if (balance>0):
             break

        else:
            print("Please, enter a valid amount in number.")
    return balance

def input_bet_lines():
   while True:
        line=input("Enter the number of lines you want to bet on 1-5: ")
        if line.isdigit():
            line=int(line)

            if (1<=line<=MAX_LINES):
             break

            else:
             print("Please, enter a valid number of line.")
        else:
           print("Please, enter the number of lines you want bet on in number")

   return line

def input_bet():
   while True:
      bet_amount=input("Enter the amount you would like to bet: ")
      if bet_amount.isdigit():
         bet_amount=int(bet_amount)
         if (MIN_BET<=bet_amount<=MAX_BET):
            break
         else:
            print("Please, enter a valid bet amount from 50$-1000$.")
      else:
         print("Please, enter your bet amount in number")
   return bet_amount


      

balance=deposit()
line=input_bet_lines()
while True:
 bet=input_bet()
 total_bet=bet*line
 if(total_bet>balance):
    print("You don't have sufficient funds in your accoount.")
 else:
    break
print(f"You have made a bet of {bet}$ on the {line} lines.\nTotal bet amount is {total_bet}")



   
