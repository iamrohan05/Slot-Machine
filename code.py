def deposit():
    while True:
        amount=input("Please enter your amount: ")
        if amount.isdigit():
            amount=int(amount)

            if (amount>0):
             break

        else:
            print("Please, enter a valid amount in number.")
    return amount



deposit()