#The bank account has a 26-digit number assigned when creating an account. 
# The initial account balance is PLN 0. You can deposit any amount on the account. 
# You can also withdraw any amount from the account, provided that it does not exceed the 
# account balance. If you try to withdraw a larger amount, the following message 
# will be displayed: "Insufficient funds on the account". At any time, it is possible 
# to display information about the number and balance of the bank account in the following format:

#Bank Account No: 11 1111 1111 1111 1111 1111 1111
#Balance: PLN 25,38

class account():
    def __init__(self):
        self.funds = 0
        self.number = "12 3456 5555 9090 1111 0000 7722"
    def deposit_funds(self, number):
        self.funds += number

    def withdraw_funds(self, number):
        if number <= self.funds:
            self.funds -= number
        else:
            print("Insufficient funds on the account")

    def display_status(self):
        print(f"Bank Account No: {self.number}")
        print(f"Balance: {self.funds}")
