from account import Account

class Customer:
    
    def __init__(self,name,customer_id):
        self.name=name
        self.customer_id=customer_id
        self.accounts=[]

    def add_account(self,account_type):
        # Creates a new account
        self.accounts.append(Account(account_type))

    def get_account(self,account_type):
        # Finds an account by its type
        for account in self.accounts:
            if account.account_type == account_type:
                return (account)
        
    def __repr__(self):
        return (f"Account(Customer Name: {self.name}, Accounts: {len(self.accounts)})")

    