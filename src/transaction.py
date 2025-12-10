# transaction.py
import uuid
from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    ACCOUNT_CREATION = "ACCOUNT_CREATION"

class Transaction:
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    ACCOUNT_CREATION = "ACCOUNT_CREATION"
    
    def _init_(self, transaction_type, amount, account_number, description="", reference=""):
        self.transaction_id = str(uuid.uuid4())[:8].upper()  # Shorter ID for display
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.account_number = account_number
        self.description = description
        self.reference = reference or f"REF-{self.transaction_id}"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timestamp = datetime.now()

    def _str_(self):
        return (f"[{self.transaction_id}] {self.date} - "
                f"{self.transaction_type:12} ${self.amount:9.2f} "
                f"| {self.description}")

    def to_dict(self):
        """Convert transaction to dictionary for serialization"""
        return {
            'transaction_id': self.transaction_id,
            'type': self.transaction_type,
            'amount': self.amount,
            'account': self.account_number,
            'description': self.description,
            'reference': self.reference,
            'date': self.date
        }
    
    def get_formatted_date(self):
        """Get formatted date for display"""
        return self.timestamp.strftime("%b %d, %Y %I:%M %p")