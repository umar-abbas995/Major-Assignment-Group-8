# transaction.py
import uuid
from datetime import datetime
# this is the class transaction function
class Transaction:
    DEPOSIT = "Deposit"
    WITHDRAWAL = "Withdrawal"

    def __init__(self, transaction_type, amount, account_number, description=""):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = transaction_type
        self.amount = amount
        self.account_number = account_number
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"[{self.transaction_id}] {self.date} - "
                f"{self.transaction_type} ${self.amount:.2f} "
                f"({self.description})")
