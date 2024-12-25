import bank_account

#Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
#Display account balance
#Deposit PLN 25,30
#Display account balance
#Withdraw PLN 31,70
#Display account balance
#Withdraw PLN 14
#Display account balance

def main():
    account = bank_account.account()
    account.display_status()
    account.deposit_funds(25.30)
    account.display_status()
    account.withdraw_funds(31.70)
    account.display_status()
    account.withdraw_funds(14.0)
    account.display_status()


if __name__ =="__main__":
   main()