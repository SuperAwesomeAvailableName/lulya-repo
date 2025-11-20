import hashlib
import hmac
import os
from typing import List, Tuple, Union, Optional

class BankAccount:
    # Class constants
    INTEREST_RATE = 0.01
    MINIMUM_BALANCE = 100
    DEFAULT_OVERDRAFT_LIMIT = -1000
    
    # Account counter for generating unique account numbers
    _next_account_number = 1
    
    def __init__(self, initial_balance: float = 100, pin: int = None):
        """Initialize a new bank account with an initial balance and PIN."""
        # Instance variables
        self._balance = initial_balance
        self._transactions = []
        self._frozen = False
        self._account_holders = []
        self._account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        
        # Secure PIN handling
        self._salt = os.urandom(32)  # Generate random salt
        if pin is not None:
            self._pin_hash = self._hash_pin(pin)
        else:
            # Generate a random PIN if none provided
            self._pin_hash = None
    
    def _hash_pin(self, pin: int) -> bytes:
        """Hash a PIN with salt using PBKDF2."""
        if not isinstance(pin, int):
            raise TypeError("PIN must be an integer")
        pin_str = str(pin).encode('utf-8')
        return hashlib.pbkdf2_hmac('sha256', pin_str, self._salt, 100000)
    
    def deposit(self, amount: float) -> bool:
        """Deposit money into the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if self._frozen:
            print("Cannot deposit to a frozen account")
            return False
            
        self._balance += amount
        self._transactions.append(("deposit", amount))
        print("Deposit successful")
        return True
        
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._frozen:
            print("Cannot withdraw from a frozen account")
            return False
        if self._balance - amount < self.DEFAULT_OVERDRAFT_LIMIT:
            print("Withdrawal denied: Would exceed overdraft limit")
            return False
            
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))
        return True

    def get_balance(self) -> float:
        """Get the current balance."""
        return self._balance      
        
    def transfer(self, other_account: 'BankAccount', amount: float) -> bool:
        """Transfer money to another account."""
        if not isinstance(other_account, BankAccount):
            raise TypeError("Can only transfer to another BankAccount")
        
        # First check if withdrawal is possible to avoid partial operations
        if self._balance - amount < self.DEFAULT_OVERDRAFT_LIMIT:
            print("Transfer denied: Would exceed overdraft limit")
            return False
            
        if self.withdraw(amount):
            return other_account.deposit(amount)
        return False
        
    def calculate_interest(self) -> float:
        """Calculate and add interest to the account."""
        if self._frozen:
            return 0.0
            
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
        self._transactions.append(("interest", interest))
        return interest
        
    def check_pin(self, entered_pin: int) -> bool:
        """Securely verify a PIN using constant-time comparison."""
        if self._pin_hash is None:
            return False
            
        entered_hash = self._hash_pin(entered_pin)
        # Use constant-time comparison to prevent timing attacks
        return hmac.compare_digest(entered_hash, self._pin_hash)
            
    def process_transaction(self, transaction_type: str, amount: float) -> bool:
        """Process a transaction (deposit or withdrawal)."""
        if self._frozen:
            print("Cannot process transactions on a frozen account")
            return False
            
        try:
            if transaction_type == "deposit":
                return self.deposit(amount)
            elif transaction_type == "withdraw":
                return self.withdraw(amount)
            else:
                raise ValueError(f"Unknown transaction type: {transaction_type}")
        except (TypeError, ValueError) as e:
            print(f"Transaction failed: {e}")
            return False
            
    def get_transaction_history(self) -> List[Tuple[str, float]]:
        """Return the transaction history."""
        return self._transactions.copy()  # Return a copy to prevent modification
            
    def freeze_account(self) -> None:
        """Freeze this specific account."""
        self._frozen = True
        
    def unfreeze_account(self) -> None:
        """Unfreeze this specific account."""
        self._frozen = False
        
    def get_account_number(self) -> int:
        """Get the account number."""
        return self._account_number
        
    def convert_to_euros(self, amount: float, conversion_rate: float = 0.85) -> float:
        """Convert an amount to euros using the provided conversion rate."""
        return amount * conversion_rate
        
    def add_joint_holder(self, name: str) -> None:
        """Add a joint account holder."""
        if name and isinstance(name, str):
            self._account_holders.append(name)
            
    def check_minimum_balance(self) -> bool:
        """Check if the account meets the minimum balance requirement."""
        return self._balance >= self.MINIMUM_BALANCE
                
    def is_in_overdraft(self) -> bool:
        """Check if the account is in overdraft."""
        return self._balance < 0
                
    def delete_account(self) -> bool:
        """Delete the account (zero out balance and clear transactions)."""
        self._balance = 0
        self._transactions = []
        self._frozen = True
        return True
