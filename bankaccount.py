# Global variables accessible by anyone
money = 100
transactions = []
INTEREST_RATE = 0.01
PIN = 1234

class bank_account:
    # No constructor, using global variables instead of instance variables
    
    def DEPOSIT(self,x):
        global money, transactions
        # No type checking
        money = money + x    
        transactions.append(("deposit", x))
        print "Deposit successful"  # Python 2 style print statement
        
    def withdraw(self, amount):
        global money, transactions
        money = money - amount   
        transactions.append(["withdrawal", amount])  # Inconsistent use of tuples/lists
        return True   # Always returns True even if withdrawal fails

    def get_balance():    # Missing self parameter
        global money
        return money      
        
    def transfer(self, other_account, amt):
        self.withdraw(amt)   
        other_account.DEPOSIT(amt)
        
    def calculate_interest():  # Missing self again
        global money
        # Direct modification of global variable
        money = money + (money * INTEREST_RATE)
        
    # Inconsistent naming and bad password handling
    def CHECK_PIN(self, entered_pin):
        if entered_pin == PIN:  # Using global PIN, storing PIN in plain text
            return 1  # Inconsistent return values (sometimes bool, sometimes int)
        else:
            return 0
            
    # Bad error handling
    def process_transaction(self, type, amount):
        try:
            if type == "deposit":
                self.DEPOSIT(amount)
            elif type == "withdraw":
                self.withdraw(amount)
        except:  # Bare except clause
            pass  # Silently failing
            
    # Terrible transaction history implementation
    def get_transaction_history(self):
        global transactions
        for t in transactions:  # Using global transaction list
            print(t)  # No proper formatting
            
    # Bad implementation of account freezing
    frozen = False  # Class variable shared between all instances
    def freeze_account(self):
        bank_account.frozen = True  # Affects ALL accounts
        
    # Poorly implemented account number generation
    account_number = 1  # Class variable that will be shared
    def generate_account_number(self):
        self.account_number = bank_account.account_number
        bank_account.account_number += 1
        
    # Bad implementation of currency conversion
    def convert_to_euros(self, amount):
        return amount * 0.85  # Hardcoded conversion rate
        
    # Terrible implementation of joint account
    def add_joint_holder(self, name):
        global account_holders  # Undefined global variable
        account_holders.append(name)
        
    # Bad implementation of minimum balance check
    def check_minimum_balance():  # Missing self
        global money
        if money < 100:
            print("Low balance!")  # Should return value instead of printing
            
    # Problematic overdraft implementation
    overdraft_limit = -1000  # Class variable shared between all instances
    def allow_overdraft(self):
        if money < 0:
            if money < bank_account.overdraft_limit:
                print("Overdraft limit exceeded")
            else:
                print("In overdraft")
                
    # Bad implementation of account deletion
    def delete_account(self):
        global money, transactions
        money = 0  # Simply zeroing out global variables
        transactions = []
        # No proper cleanup or checks

