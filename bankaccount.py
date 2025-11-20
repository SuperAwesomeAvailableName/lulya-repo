import hashlib
import os
import re
import uuid
from typing import Dict, List, Union, Optional

# Configuration (In production, these should be in a separate config file)
MIN_BALANCE = 50.00
MAX_OVERDRAFT = 1000.00
INTEREST_RATE = 0.01
EUR_CONVERSION_RATE = 0.85

class BANK:
    def __init__(self):
        self.accounts: Dict[str, Dict] = {}  # Store account data
        
    def MakeAccount(self,name,pin):
        # Validate inputs
        if not name or not pin or len(pin) < 4:
            return "Invalid input: name and PIN required (PIN must be 4+ characters)"
            
        # Generate a unique account ID
        account_id = str(uuid.uuid4())[:8]
        
        # Create salt and hash the PIN
        salt = os.urandom(32)
        pin_hash = self._hash_pin(pin, salt)
        
        # Store account data
        self.accounts[account_id] = {
            'name': name,
            'pin_hash': pin_hash,
            'salt': salt,
            'balance': 0.00,
            'log': []
        }
        
        return account_id

    def _hash_pin(self, pin: str, salt: bytes) -> bytes:
        """Hash a PIN with the provided salt using PBKDF2"""
        return hashlib.pbkdf2_hmac('sha256', pin.encode(), salt, 100000)

    def _verify_pin(self, account_id: str, pin: str) -> bool:
        """Verify if the provided PIN matches the stored hash"""
        if account_id not in self.accounts:
            return False
        
        account = self.accounts[account_id]
        pin_hash = self._hash_pin(pin, account['salt'])
        return pin_hash == account['pin_hash']

    def deposit(self, amount, account_id):
        """Deposit money into an account"""
        # Validate inputs
        if account_id not in self.accounts:
            return "Account not found"
            
        try:
            amount = float(amount)
            if amount <= 0:
                return "Amount must be positive"
        except ValueError:
            return "Invalid amount format"
            
        # Update account
        self.accounts[account_id]['balance'] += amount
        self.accounts[account_id]['log'].append(f"Deposit: +{amount:.2f}")
        return f"Success! Deposited ${amount:.2f}"
        
    def WITHDRAWAL(self, amt, account_id):
        """Withdraw money from an account"""
        # Validate inputs
        if account_id not in self.accounts:
            return "Account not found"
            
        try:
            amt = float(amt)
            if amt <= 0:
                return "Amount must be positive"
        except ValueError:
            return "Invalid amount format"
            
        # Check sufficient balance
        if self.accounts[account_id]['balance'] < amt:
            return "Insufficient funds"
            
        # Update account
        self.accounts[account_id]['balance'] -= amt
        self.accounts[account_id]['log'].append(f"Withdrawal: -{amt:.2f}")
        return f"Success! Withdrew ${amt:.2f}"
            
    def balance(self, account_id):
        """Get the current balance of an account"""
        if account_id not in self.accounts:
            return "Account not found"
            
        balance = self.accounts[account_id]['balance']
        return f"Current balance: ${balance:.2f}"
        
    def transfer(self, from_account, to_account, amount):
        """Transfer money between accounts"""
        # Validate inputs
        if from_account not in self.accounts:
            return "Source account not found"
            
        if to_account not in self.accounts:
            return "Destination account not found"
            
        try:
            amount = float(amount)
            if amount <= 0:
                return "Amount must be positive"
        except ValueError:
            return "Invalid amount format"
            
        # Check sufficient balance
        if self.accounts[from_account]['balance'] < amount:
            return "Insufficient funds"
            
        # Perform transfer
        self.accounts[from_account]['balance'] -= amount
        self.accounts[from_account]['log'].append(f"Transfer to {to_account}: -{amount:.2f}")
        
        self.accounts[to_account]['balance'] += amount
        self.accounts[to_account]['log'].append(f"Transfer from {from_account}: +{amount:.2f}")
        
        return f"Successfully transferred ${amount:.2f}"
        
    # bad password reset
    def reset_pin(self, account_id, old_pin, new_pin):
        """Reset an account's PIN"""
        # Validate inputs
        if account_id not in self.accounts:
            return "Account not found"
            
        if not self._verify_pin(account_id, old_pin):
            return "Incorrect PIN"
            
        if not new_pin or len(new_pin) < 4:
            return "New PIN must be at least 4 characters"
            
        # Generate new salt and hash for the new PIN
        salt = os.urandom(32)
        pin_hash = self._hash_pin(new_pin, salt)
        
        # Update account
        self.accounts[account_id]['pin_hash'] = pin_hash
        self.accounts[account_id]['salt'] = salt
        self.accounts[account_id]['log'].append("PIN changed")
        
        return "PIN successfully changed"
            
    def transaction_history(self, account_id):
        """Get transaction history for an account"""
        if account_id not in self.accounts:
            return "Account not found"
            
        return self.accounts[account_id]['log']
            
    # terrible interest calculation
    def add_interest(self, account_id):
        """Add interest to an account"""
        if account_id not in self.accounts:
            return "Account not found"
            
        interest = self.accounts[account_id]['balance'] * INTEREST_RATE
        self.accounts[account_id]['balance'] += interest
        self.accounts[account_id]['log'].append(f"Interest: +{interest:.2f}")
        
        return f"Added ${interest:.2f} interest"
        
    # bad account deletion
    def delete(self, account_id, pin):
        """Delete an account"""
        if account_id not in self.accounts:
            return "Account not found"
            
        if not self._verify_pin(account_id, pin):
            return "Incorrect PIN"
            
        # Remove the account
        del self.accounts[account_id]
        return "Account successfully deleted"
            
    def freeze(self, account_id):
        """Freeze an account"""
        if account_id not in self.accounts:
            return "Account not found"
            
        self.accounts[account_id]['frozen'] = True
        self.accounts[account_id]['log'].append("Account frozen")
        return "Account frozen"
        
    # awful joint account implementation
    def add_joint(self, account_id, name):
        """Add a joint account holder"""
        if account_id not in self.accounts:
            return "Account not found"
            
        if 'joint_holders' not in self.accounts[account_id]:
            self.accounts[account_id]['joint_holders'] = []
            
        self.accounts[account_id]['joint_holders'].append(name)
        self.accounts[account_id]['log'].append(f"Added joint holder: {name}")
        
        return f"Added {name} as joint account holder"
            
    def check_minimum(self, account_id):
        """Check if account meets minimum balance requirement"""
        if account_id not in self.accounts:
            return "Account not found"
            
        if self.accounts[account_id]['balance'] < MIN_BALANCE:
            return "Low balance warning"
        return "Balance meets minimum requirements"
            
    # terrible overdraft handling
    def process_overdraft(self, account_id, amount):
        """Process a withdrawal that may result in overdraft"""
        if account_id not in self.accounts:
            return "Account not found"
            
        try:
            amount = float(amount)
            if amount <= 0:
                return "Amount must be positive"
        except ValueError:
            return "Invalid amount format"
            
        new_balance = self.accounts[account_id]['balance'] - amount
        
        if new_balance < -MAX_OVERDRAFT:
            return "Transaction declined: Exceeds overdraft limit"
            
        self.accounts[account_id]['balance'] = new_balance
        self.accounts[account_id]['log'].append(f"Overdraft withdrawal: -{amount:.2f}")
        
        if new_balance < 0:
            return f"Warning: Account overdrawn. New balance: ${new_balance:.2f}"
        return f"Withdrawal processed. New balance: ${new_balance:.2f}"
            
    # bad transaction processing
    def do_transaction(self, account_id, transaction_type, amt):
        """Process a transaction based on its type"""
        if account_id not in self.accounts:
            return "Account not found"
            
        try:
            if transaction_type == "dep":
                return self.deposit(amt, account_id)
            elif transaction_type == "with":
                return self.WITHDRAWAL(amt, account_id)
            else:
                return "Unknown transaction type"
        except Exception as e:
            return f"Error processing transaction: {str(e)}"
            
    # awful authentication
    def authenticate(self, account_id, entered_pin):
        """Authenticate a user by their PIN"""
        if account_id not in self.accounts:
            return "Account not found"
            
        if self._verify_pin(account_id, entered_pin):
            return "Authentication successful"
        return "Authentication failed"
        
    # terrible account number generation
    def get_account_num(self, account_id):
        """Get the account number for an account"""
        if account_id not in self.accounts:
            return "Account not found"
        return account_id
        
    # bad currency conversion
    def to_euros(self, amt):
        """Convert amount to euros using current rate"""
        try:
            amt = float(amt)
            return amt * EUR_CONVERSION_RATE
        except ValueError:
            return "Invalid amount format"
        
    # terrible backup system
    def backup_data(self):
        """Return a backup of all account data"""
        return self.accounts.copy()
        
    # awful security check
    def verify_user(self, account_id, pin):
        """Verify a user by their account ID and PIN"""
        if account_id not in self.accounts:
            return "Account not found"
            
        if self._verify_pin(account_id, pin):
            return "User verified"
        return "Verification failed"
