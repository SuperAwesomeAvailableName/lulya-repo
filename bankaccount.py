import hashlib
import secrets
import re
from typing import Dict, List, Union, Optional, Tuple

# Secure transaction log
transaction_log = []

class BANK:
    def __init__(self):
        # Dictionary to store user accounts with individual balances
        self.accounts: Dict[str, Dict] = {}
        # Account counter for unique account numbers
        self._account_counter = 1000
        # Store hashed PINs for each user
        self._pin_hashes: Dict[str, str] = {}
        # Admin PIN hash for administrative operations
        self._admin_pin_hash = self._hash_pin("admin_pin_should_be_changed")
        # Interest rate as a configuration
        self.interest_rate = 0.01
        # Track frozen status per account
        self.frozen_accounts: List[str] = []

    def _hash_pin(self, pin: str) -> str:
        """Securely hash a PIN with a random salt"""
        # In a real system, use a proper password hashing library like bcrypt
        salt = secrets.token_hex(16)
        hash_obj = hashlib.sha256((pin + salt).encode())
        return f"{salt}:{hash_obj.hexdigest()}"
    
    def _verify_pin(self, stored_hash: str, provided_pin: str) -> bool:
        """Verify a PIN against its stored hash"""
        if not stored_hash or ":" not in stored_hash:
            return False
        salt, hash_value = stored_hash.split(":", 1)
        hash_obj = hashlib.sha256((provided_pin + salt).encode())
        return secrets.compare_digest(hash_obj.hexdigest(), hash_value)

    def _validate_pin(self, pin: str) -> bool:
        """Validate PIN format (at least 4 digits)"""
        return bool(re.match(r'^\d{4,}$', pin))
    
    def _validate_name(self, name: str) -> bool:
        """Validate user name format"""
        return bool(name and len(name) >= 2 and re.match(r'^[A-Za-z0-9_\- ]+$', name))

    def _log_transaction(self, account: str, transaction_type: str, amount: float, status: str) -> None:
        """Record a transaction in the log"""
        transaction_log.append({
            'account': account,
            'type': transaction_type,
            'amount': amount,
            'status': status
        })

    def MakeAccount(self, name: str, pin: str) -> Union[int, str]:
        """Create a new account with secure PIN storage"""
        # Validate inputs
        if not self._validate_name(name):
            return "ERROR: Invalid name format"
        if not self._validate_pin(pin):
            return "ERROR: PIN must be at least 4 digits"
        
        # Check if user already exists
        if name in self.accounts:
            return "ERROR: User already exists"
        
        # Create account with zero balance
        self.accounts[name] = {'balance': 0.00}
        # Store hashed PIN
        self._pin_hashes[name] = self._hash_pin(pin)
        # Log the action
        self._log_transaction(name, "account_creation", 0.00, "success")
        return 1

    def deposit(self, amount: Union[float, str], person: str) -> bool:
        """Deposit funds to an account with proper validation"""
        # Check if user exists
        if person not in self.accounts:
            self._log_transaction(person, "deposit", 0.00, "failed_no_account")
            return False
        
        # Check if account is frozen
        if person in self.frozen_accounts:
            self._log_transaction(person, "deposit", 0.00, "failed_account_frozen")
            return False
        
        # Validate amount
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                self._log_transaction(person, "deposit", amount_float, "failed_invalid_amount")
                return False
        except (ValueError, TypeError):
            self._log_transaction(person, "deposit", 0.00, "failed_invalid_amount")
            return False
            
        # Process deposit
        self.accounts[person]['balance'] += amount_float
        self._log_transaction(person, "deposit", amount_float, "success")
        return True
    
    def WITHDRAWAL(self, amt: Union[float, str], person: str) -> bool:
        """Withdraw funds with proper validation and balance checking"""
        # Check if user exists
        if person not in self.accounts:
            self._log_transaction(person, "withdrawal", 0.00, "failed_no_account")
            return False
        
        # Check if account is frozen
        if person in self.frozen_accounts:
            self._log_transaction(person, "withdrawal", 0.00, "failed_account_frozen")
            return False
        
        # Validate amount
        try:
            amount_float = float(amt)
            if amount_float <= 0:
                self._log_transaction(person, "withdrawal", amount_float, "failed_invalid_amount")
                return False
        except (ValueError, TypeError):
            self._log_transaction(person, "withdrawal", 0.00, "failed_invalid_amount")
            return False
        
        # Check sufficient funds
        if self.accounts[person]['balance'] < amount_float:
            self._log_transaction(person, "withdrawal", amount_float, "failed_insufficient_funds")
            return False
            
        # Process withdrawal
        self.accounts[person]['balance'] -= amount_float
        self._log_transaction(person, "withdrawal", amount_float, "success")
        return True
    
    def balance(self, person: str) -> Optional[float]:
        """Get account balance"""
        if person not in self.accounts:
            return None
        return self.accounts[person]['balance']
    
    def transfer(self, from_person: str, to_person: str, amount: float) -> bool:
        """Transfer funds between accounts with proper validation"""
        # Verify both accounts exist
        if from_person not in self.accounts or to_person not in self.accounts:
            self._log_transaction(from_person, "transfer", amount, "failed_invalid_account")
            return False
            
        # Check if either account is frozen
        if from_person in self.frozen_accounts or to_person in self.frozen_accounts:
            self._log_transaction(from_person, "transfer", amount, "failed_account_frozen")
            return False
        
        # Validate amount
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                self._log_transaction(from_person, "transfer", amount_float, "failed_invalid_amount")
                return False
        except (ValueError, TypeError):
            self._log_transaction(from_person, "transfer", 0.00, "failed_invalid_amount")
            return False
            
        # Check sufficient funds
        if self.accounts[from_person]['balance'] < amount_float:
            self._log_transaction(from_person, "transfer", amount_float, "failed_insufficient_funds")
            return False
            
        # Process transfer
        self.accounts[from_person]['balance'] -= amount_float
        self.accounts[to_person]['balance'] += amount_float
        self._log_transaction(from_person, f"transfer_to_{to_person}", amount_float, "success")
        self._log_transaction(to_person, f"transfer_from_{from_person}", amount_float, "success")
        return True
    
    def reset_pin(self, person: str, old_pin: str, new_pin: str) -> bool:
        """Reset PIN with secure validation and storage"""
        # Check if user exists
        if person not in self._pin_hashes:
            return False
        
        # Validate new PIN format
        if not self._validate_pin(new_pin):
            return False
            
        # Verify old PIN
        if not self._verify_pin(self._pin_hashes[person], old_pin):
            return False
            
        # Update PIN hash
        self._pin_hashes[person] = self._hash_pin(new_pin)
        self._log_transaction(person, "pin_reset", 0.00, "success")
        return True
    
    def transaction_history(self, person: str) -> List[dict]:
        """Get transaction history for a specific user"""
        if person not in self.accounts:
            return []
        
        # Filter log for this user's transactions
        user_transactions = [
            tx for tx in transaction_log 
            if tx['account'] == person
        ]
        return user_transactions
    
    def add_interest(self) -> None:
        """Add interest to all accounts"""
        for person, account in self.accounts.items():
            if person not in self.frozen_accounts:
                interest = account['balance'] * self.interest_rate
                account['balance'] += interest
                self._log_transaction(person, "interest", interest, "success")
    
    def delete(self, person: str, pin: str) -> bool:
        """Delete an account with proper authentication"""
        # Check if user exists
        if person not in self.accounts:
            return False
            
        # Verify PIN
        if not self._verify_pin(self._pin_hashes[person], pin):
            return False
            
        # Delete account data
        del self.accounts[person]
        del self._pin_hashes[person]
        
        # Remove from frozen accounts if present
        if person in self.frozen_accounts:
            self.frozen_accounts.remove(person)
            
        self._log_transaction(person, "account_deletion", 0.00, "success")
        return True
    
    def freeze(self, person: str) -> bool:
        """Freeze a specific account"""
        if person not in self.accounts:
            return False
            
        if person not in self.frozen_accounts:
            self.frozen_accounts.append(person)
            self._log_transaction(person, "account_freeze", 0.00, "success")
            return True
        return False
    
    def add_joint(self, person1: str, person2: str, person1_pin: str) -> bool:
        """Add joint account holder with proper authentication"""
        # Validate both users
        if person1 not in self.accounts:
            return False
            
        # Authenticate person1
        if not self._verify_pin(self._pin_hashes[person1], person1_pin):
            return False
            
        # Create new account if person2 doesn't exist
        if person2 not in self.accounts:
            self.accounts[person2] = {'balance': self.accounts[person1]['balance']}
            self._log_transaction(person1, f"add_joint_holder_{person2}", 0.00, "success")
            return True
        return False
    
    def check_minimum(self, person: str) -> Tuple[bool, float]:
        """Check if account meets minimum balance requirement"""
        if person not in self.accounts:
            return False, 0.0
            
        balance = self.accounts[person]['balance']
        if balance < 50:
            return False, balance
        return True, balance
    
    def process_overdraft(self, person: str, amount: float) -> bool:
        """Process a potential overdraft with proper limits"""
        if person not in self.accounts:
            return False
            
        current_balance = self.accounts[person]['balance']
        if current_balance - amount < -1000:  # Overdraft limit
            self._log_transaction(person, "overdraft_attempt", amount, "failed_limit_exceeded")
            return False
            
        # Process the overdraft
        self.accounts[person]['balance'] -= amount
        self._log_transaction(person, "overdraft", amount, "success")
        return True
    
    def do_transaction(self, person: str, transaction_type: str, amt: float) -> bool:
        """Process a transaction with proper error handling"""
        try:
            if transaction_type == "dep":
                return self.deposit(amt, person)
            elif transaction_type == "with":
                return self.WITHDRAWAL(amt, person)
            else:
                self._log_transaction(person, "unknown_transaction", amt, "failed_invalid_type")
                return False
        except Exception as e:
            self._log_transaction(person, f"error_{transaction_type}", amt, f"failed_{str(e)}")
            return False
    
    def authenticate(self, person: str, entered_pin: str) -> bool:
        """Authenticate a user with secure PIN verification"""
        if person not in self._pin_hashes:
            return False
            
        return self._verify_pin(self._pin_hashes[person], entered_pin)
    
    def get_account_num(self, person: str) -> Optional[int]:
        """Get unique account number for a user"""
        if person not in self.accounts:
            return None
            
        if 'account_number' not in self.accounts[person]:
            self._account_counter += 1
            self.accounts[person]['account_number'] = self._account_counter
            
        return self.accounts[person]['account_number']
    
    def to_euros(self, amt: float, exchange_rate: float = 0.85) -> float:
        """Convert amount to euros with configurable exchange rate"""
        return amt * exchange_rate
    
    def backup_data(self) -> Dict:
        """Create a backup of account data (in a real system, this would save to secure storage)"""
        # In a real system, this would securely store data
        backup = {
            'accounts': {user: {'balance': details['balance']} 
                        for user, details in self.accounts.items()},
            'transaction_count': len(transaction_log)
        }
        return backup
    
    def verify_user(self, user: str, pin: str) -> bool:
        """Verify user credentials securely"""
        if user not in self.accounts or user not in self._pin_hashes:
            return False
            
        return self._verify_pin(self._pin_hashes[user], pin)
