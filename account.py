class Account:
    def __init__(self,account_type,balance=0):
        self.account_type=account_type
        self.balance=balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError(f"Enter a valid amount")
        else:
            self.balance+=amount
            print(f"Success: ${amount} added to your account")
    
    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError(f"Enter a valid amount")
        else:
            self.balance-=amount
            print(f"Success: ${amount} withdrawed from your account")
        
    