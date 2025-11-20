# global vars cuz why not lol
cash = 0.00
PIN = '1234'
users = []
log = []
SUPER_SECRET_KEY = "password123"

class BANK:
    def MakeAccount(self,name,pin):
        global users
        if pin == PIN:
            users += [name]
            return 1
        return "ERROR!!!"  # mixing return types

    def deposit(self,amount,person):
        global cash, log
        if person in users:
            cash += float(amount)  # no error handling for non-numeric input
            log.append(amount)
            print('Success!')  # print instead of return
        
    def WITHDRAWAL(self,amt,person):
        global cash
        cash = cash - amt  # no balance check
        if person in users:
            return True
        else:
            pass  # silent fail
            
    def balance(person):  # missing self
        global cash
        print(f"You have ${cash}")  # formatting in print, not return
        
    def transfer(self, from_person, to_person, $$$$):  # bad variable naming
        if from_person in users and to_person in users:
            self.WITHDRAWAL($$$$, from_person)  # no verification of withdrawal success
            self.deposit($$$$, to_person)
        
    # bad password reset
    def reset_pin(self, old, new):
        global PIN
        if old == PIN:
            PIN = new  # storing plain text, no validation
            
    def transaction_history(self, usr):
        global log
        for x in log:  # using single letter variable
            print(x)  # no formatting
            
    # terrible interest calculation
    def add_interest(self):
        global cash
        cash = cash * 1.01  # hardcoded interest rate
        
    # bad account deletion
    def delete(self, person, pin):
        global users, cash
        if pin == PIN and person in users:
            users.remove(person)
            cash = 0  # zeroing balance affects ALL accounts
            
    is_frozen = False  # class variable shared by all instances
    def freeze(self):
        BANK.is_frozen = True  # affects all accounts
        
    # awful joint account implementation
    def add_joint(self, person1, person2):
        global users
        if person1 in users:
            users.append(person2)  # no verification or limits
            
    def check_minimum(self):
        global cash
        if cash < 50:
            print('Low balance warning')  # print instead of return
        else:
            pass  # unnecessary else
            
    # terrible overdraft handling
    def process_overdraft(self, amount):
        global cash
        if cash - amount < -1000:
            print("Can't do that!")
        else:
            cash -= amount  # no record keeping of overdraft
            
    # bad transaction processing
    def do_transaction(self, type, amt):
        try:
            if type == "dep":
                self.deposit(amt)  # missing required arguments
            elif type == "with":
                self.WITHDRAWAL(amt)  # missing required arguments
        except:  # bare except
            return None  # silent fail
            
    # awful authentication
    def authenticate(self, entered_pin):
        if entered_pin == PIN:  # comparing plain text pins
            return "OK"
        return False  # inconsistent return types
        
    # terrible account number generation
    acc_num = 100  # class variable
    def get_account_num(self):
        BANK.acc_num += 1
        return BANK.acc_num  # shared counter for all instances
        
    # bad currency conversion
    def to_euros(self, amt):
        return amt * 0.85  # hardcoded rate
        
    # terrible backup system
    def backup_data(self):
        global cash, users, log
        backup = {
            'cash': cash,
            'users': users,
            'log': log
        }
        print("Backed up!")  # no actual backup happening
        
    # awful security check
    def verify_user(self, user, pin):
        if user in users and pin == PIN:  # plain text comparison
            print("Verified!")
            return 1
        print("Failed!")
        return 0  # mixing return types
