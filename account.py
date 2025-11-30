from exceptions import InsufficientFundException

class Account:
    def __init__(self,account_type,balance=0):
        self.account_type=account_type
        self.balance=balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError(f"Enter a valid amount")
        else:
            self.balance+=amount
    
    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError(f"Enter a valid amount")
        elif(amount>self.balance):
            raise InsufficientFundException(f"Failure: Cannot withdraw ${amount}. Available balance is just ${self.balance}")
        else:
            self.balance-=amount

    def __repr__(self):
        print(f"Account(Account Type: {self.account_type}, Balance: {self.balance})")   
    