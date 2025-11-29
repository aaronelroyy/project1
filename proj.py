
def deposit():
    while True:
        amount: int = int (input("what would like to deposit? : $ "))
        '''if amount.isdigit():
            amount = int(amount)'''
        if amount > 0:
            return amount
        else:
            print("Amount must be greater than 0")
    else:
        print("enter a number")
    

def main():
    

if __name__ == "__main__":
    main()