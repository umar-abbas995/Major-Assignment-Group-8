# transaction.py
import uuid
from datetime import datetime

class Transaction:
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    ACCOUNT_CREATION = "ACCOUNT_CREATION"
    
    def _init_(self, transaction_type, amount, account_number, description=""):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.account_number = account_number
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _str_(self):
        return (f"[{self.transaction_id[:8]}] {self.date} - "
                f"{self.transaction_type:12} ${self.amount:9.2f} "
                f"| {self.description}")