# Secure bank account implementation
import hashlib
import os
import re

cash = 0.00
users = []
log = []

# Store hashed PINs with salt instead of plaintext
user_pins = {}
DEFAULT_SALT = os.urandom(32)  # Generate a random salt

def hash_pin(pin, salt=DEFAULT_SALT):
    """Hash a PIN with salt using SHA-256"""
    pin_bytes = pin.encode('utf-8')
    hashed_pin = hashlib.pbkdf2_hmac('sha256', pin_bytes, salt, 100000)
    return hashed_pin.hex()

class BANK:
    current_user = None
    
    def MakeAccount(self,name,pin):
        global users, user_pins
        if len(pin) >= 4:  # Minimum PIN length check
            users += [name]
            user_pins[name] = hash_pin(pin)
            return 1
        return "ERROR!!!"  # mixing return types

    def deposit(self,amount,person):
        global cash, log
        if person in users:
            try:
                amount_float = float(amount)
                cash += amount_float
                log.append(amount_float)
                return True
            except ValueError:
                return False
        return False
        
    def WITHDRAWAL(self,amt,person):
        global cash
        try:
            amt_float = float(amt)
            if person in users and cash >= amt_float:
                cash = cash - amt_float
                return True
            return False
        except ValueError:
            return False
            
    def balance(self, person):  # Fixed missing self
        global cash
        if person in users:
            return f"You have ${cash}"
        return "User not found"
        
    def transfer(self, from_person, to_person, $$$$):  # bad variable naming
        if from_person in users and to_person in users:
            if self.WITHDRAWAL($$$$, from_person):
                return self.deposit($$$$, to_person)
            return False
        return False
        
    # Secure password reset
    def reset_pin(self, username, old, new):
        global user_pins
        if username in users:
            stored_hash = user_pins.get(username, "")
            if stored_hash and hash_pin(old) == stored_hash:
                if len(new) >= 4:  # Minimum PIN length check
                    user_pins[username] = hash_pin(new)
                    return True
        return False
            
    def transaction_history(self, usr):
        global log
        if usr in users:
            transaction_log = []
            for transaction in log:
                transaction_log.append(transaction)
            return transaction_log
        return "User not found"
            
    # terrible interest calculation
    def add_interest(self):
        global cash
        cash = cash * 1.01  # hardcoded interest rate
        return True
        
    # Improved account deletion
    def delete(self, person, pin):
        global users, user_pins
        if person in users:
            stored_hash = user_pins.get(person, "")
            if stored_hash and hash_pin(pin) == stored_hash:
                users.remove(person)
                del user_pins[person]
                return True
        return False
            
    is_frozen = False  # class variable shared by all instances
    def freeze(self):
        BANK.is_frozen = True  # affects all accounts
        return True
        
    # awful joint account implementation
    def add_joint(self, person1, person2):
        global users
        if person1 in users:
            if person2 not in users:
                users.append(person2)
                return True
        return False
            
    def check_minimum(self):
        global cash
        if cash < 50:
            return 'Low balance warning'
        return 'Balance OK'
            
    # terrible overdraft handling
    def process_overdraft(self, amount):
        global cash
        try:
            amount_float = float(amount)
        except ValueError:
            return False

        if cash - amount < -1000:
            return "Can't do that!"
        else:
            cash -= amount  # no record keeping of overdraft
            return True
            
    # bad transaction processing
    def do_transaction(self, type, amt):
        try:
            amt_float = float(amt)
            if type == "dep":
                if self.current_user:
                    return self.deposit(amt_float, self.current_user)
            elif type == "with":
                if self.current_user:
                    return self.WITHDRAWAL(amt_float, self.current_user)
            return False
        except ValueError:
            return False
            
    # awful authentication
    def authenticate(self, username, entered_pin):
        global user_pins
        stored_hash = user_pins.get(username, "")
        if stored_hash and hash_pin(entered_pin) == stored_hash:
            self.current_user = username
            return "OK"
        return False  # inconsistent return types
        
    # terrible account number generation
    acc_num = 100  # class variable - not a security vulnerability
    def get_account_num(self):
        BANK.acc_num += 1
        return BANK.acc_num  # shared counter for all instances
        
    # bad currency conversion
    def to_euros(self, amt):
        try:
            return float(amt) * 0.85  # hardcoded rate but safe
        except ValueError:
            return 0
        
    # terrible backup system
    def backup_data(self):
        global cash, users, log, user_pins
        backup = {
            'cash': cash,
            'users': users,
            'log': log,
            'pins': '<REDACTED>'  # Don't include actual hashed pins in backup
        }
        return backup
        
    # Improved security check
    def verify_user(self, user, entered_pin):
        global user_pins
        stored_hash = user_pins.get(user, "")
        if user in users and stored_hash and hash_pin(entered_pin) == stored_hash:
            self.current_user = user
            return 1
        return 0
