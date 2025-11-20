# Bank account system with improved security
import hashlib
import secrets

cash = 0.00
PIN = 'e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a'  # SHA256 hash of '1234'
users = []
log = []
SUPER_SECRET_KEY = None  # Removed hardcoded key

class BANK:
    def MakeAccount(self,name,pin):
        global users
        if self._verify_pin(pin):
            users += [name]
            return 1
        return 0  # Consistent return types
        
    def _verify_pin(self, pin_to_check):
        """Securely verify PIN using hash comparison"""
        if not pin_to_check:
            return False
        # Hash the input pin and compare with stored hash
        hashed_input = hashlib.sha256(pin_to_check.encode()).hexdigest()
        return secrets.compare_digest(hashed_input, PIN)

    def deposit(self,amount,person):
        global cash, log
        if person in users:
            try:
                # Input validation
                amount_float = float(amount)
                if amount_float <= 0:
                    return "Amount must be positive"
                    
                cash += amount_float
                log.append(amount_float)
                return 'Success!'
            except ValueError:
                return "Invalid amount format"
        return "User not found"
        
    def WITHDRAWAL(self,amt,person):
        global cash
        if person in users:
            try:
                amt_float = float(amt)
                if amt_float <= 0:
                    return "Amount must be positive"
                if cash >= amt_float:
                    cash = cash - amt_float
                    return True
                return "Insufficient funds"
            except ValueError:
                return "Invalid amount format"
        return False
            
    def balance(self, person):  # Fixed missing self
        global cash
        if person in users:
            return f"You have ${cash:.2f}"
        return "User not found"
        
    def transfer(self, from_person, to_person, $$$$):  # bad variable naming
        if from_person in users and to_person in users:
            try:
                amount = float($$$$)
                if amount <= 0:
                    return "Amount must be positive"
                    
                withdrawal_result = self.WITHDRAWAL(amount, from_person)
                if withdrawal_result is True:
                    return self.deposit(amount, to_person)
                return withdrawal_result
            except ValueError:
                return "Invalid amount format"
        return "One or both users not found"
        
    # bad password reset
    def reset_pin(self, old, new):
        global PIN
        if self._verify_pin(old):
            # Validate new PIN
            if not new or len(new) < 4:
                return "New PIN must be at least 4 characters"
                
            # Hash and store the new PIN
            new_hash = hashlib.sha256(new.encode()).hexdigest()
            PIN = new_hash
            return "PIN updated successfully"
        return "Incorrect old PIN"
            
    def transaction_history(self, usr):
        global log
        if usr in users:
            history = []
            for transaction in log:
                history.append(f"${transaction:.2f}")
            return history
        return "User not found"
            
    # terrible interest calculation
    def add_interest(self):
        global cash
        interest_rate = 0.01  # 1% interest rate
        interest = cash * interest_rate
        cash += interest
        return f"Added ${interest:.2f} interest"
        
    # bad account deletion
    def delete(self, person, pin):
        global users, cash
        if self._verify_pin(pin) and person in users:
            users.remove(person)
            # Don't zero out cash as it affects all accounts
            return "Account deleted"
        return "Authentication failed or user not found"
            
    is_frozen = False  # class variable shared by all instances
    def freeze(self):
        BANK.is_frozen = True  # affects all accounts
        return "All accounts frozen"
        
    # awful joint account implementation
    def add_joint(self, person1, person2):
        global users
        if person1 in users:
            if person2 not in users:  # Prevent duplicates
                users.append(person2)
                return f"Added {person2} to joint account with {person1}"
            return f"{person2} already has an account"
        return f"{person1} not found"
            
    def check_minimum(self):
        global cash
        if cash < 50:
            return 'Low balance warning'
        return "Balance is adequate"
            
    # terrible overdraft handling
    def process_overdraft(self, amount):
        global cash
        try:
            amount_float = float(amount)
            if cash - amount_float < -1000:  # -$1000 overdraft limit
                return "Exceeded overdraft limit"
            else:
                cash -= amount_float
                return f"Processed overdraft. New balance: ${cash:.2f}"
        except ValueError:
            return "Invalid amount format"
            
    # bad transaction processing
    def do_transaction(self, type, amt):
        try:
            if type == "dep":
                # Need to add a default user for this example
                if users:
                    return self.deposit(amt, users[0])
                return "No users available"
            elif type == "with":
                if users:
                    return self.WITHDRAWAL(amt, users[0])
                return "No users available"
            else:
                return "Unknown transaction type"
        except Exception as e:
            return f"Transaction failed: {str(e)}"
            
    # awful authentication
    def authenticate(self, entered_pin):
        if self._verify_pin(entered_pin):
            return "OK"
        return "FAIL"  # Consistent return types
        
    # terrible account number generation
    acc_num = 100  # class variable
    def get_account_num(self):
        BANK.acc_num += 1
        return BANK.acc_num  # shared counter for all instances

    # bad currency conversion
    def to_euros(self, amt):
        try:
            amt_float = float(amt)
            conversion_rate = 0.85  # Euro conversion rate
            return amt_float * conversion_rate
        except ValueError:
            return "Invalid amount format"
        
    # terrible backup system
    def backup_data(self):
        global cash, users, log
        backup = {
            'cash': float(cash),
            'users': users,
            'log': log
        }
        return backup  # Return data instead of just printing
        
    # awful security check
    def verify_user(self, user, pin):
        if user in users and self._verify_pin(pin):
            return "Verified!"
        return "Failed!"
