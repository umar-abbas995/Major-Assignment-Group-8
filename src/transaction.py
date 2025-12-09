"""
Transaction Module
Handles individual transaction records with timestamps
"""

from datetime import datetime

class Transaction:
    """Represents a single financial transaction"""
    
    # Transaction type constants
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    
    def __init__(self, transaction_type, amount, account_number, description=""):
        """
        Initialize a new transaction
        
        Args:
            transaction_type (str): Type of transaction
            amount (float): Transaction amount
            account_number (str): Associated account number
            description (str): Optional description
        """
        self.transaction_type = transaction_type
        self.amount = amount
        self.account_number = account_number
        self.description = description
        self.timestamp = datetime.now()
        self.transaction_id = self._generate_id()
    
    def _generate_id(self):
        """Generate unique transaction ID"""
        timestamp_str = self.timestamp.strftime("%Y%m%d%H%M%S")
        return f"TXN{timestamp_str}{hash(self.account_number) % 10000:04d}"
    
    def get_details(self):
        """Get transaction details as dictionary"""
        return {
            'transaction_id': self.transaction_id,
            'type': self.transaction_type,
            'amount': self.amount,
            'account_number': self.account_number,
            'description': self.description,
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'date': self.timestamp.strftime("%Y-%m-%d"),
            'time': self.timestamp.strftime("%H:%M:%S")
        }
    
    def __str__(self):
        """String representation of transaction"""
        return (f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{self.transaction_type}: ${self.amount:.2f} "
                f"(Account: {self.account_number})")
    
    def to_csv(self):
        """Convert to CSV format"""
        return f"{self.transaction_id},{self.transaction_type},{self.amount},{self.account_number},{self.timestamp}"

class TransactionManager:
    """Manages collection of transactions"""
    
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):
        """Add a transaction to manager"""
        self.transactions.append(transaction)
    
    def get_transactions_by_account(self, account_number):
        """Get all transactions for specific account"""
        return [t for t in self.transactions if t.account_number == account_number]
    
    def get_transactions_by_type(self, transaction_type):
        """Get transactions by type"""
        return [t for t in self.transactions if t.transaction_type == transaction_type]
    
    def get_transactions_by_date(self, date_str):
        """Get transactions on specific date"""
        return [t for t in self.transactions if t.timestamp.strftime("%Y-%m-%d") == date_str]
    
    def get_total_by_account(self, account_number):
        """Get total transaction amount for account"""
        account_transactions = self.get_transactions_by_account(account_number)
        return sum(t.amount for t in account_transactions)
    
    def get_statement(self, account_number, start_date=None, end_date=None):
        """Generate account statement"""
        account_transactions = self.get_transactions_by_account(account_number)
        
        if start_date and end_date:
            filtered = []
            for t in account_transactions:
                trans_date = t.timestamp.strftime("%Y-%m-%d")
                if start_date <= trans_date <= end_date:
                    filtered.append(t)
            account_transactions = filtered
        
        statement = {
            'account_number': account_number,
            'total_transactions': len(account_transactions),
            'transactions': [t.get_details() for t in account_transactions],
            'total_deposits': sum(t.amount for t in account_transactions if t.transaction_type in [Transaction.DEPOSIT, Transaction.TRANSFER_IN]),
            'total_withdrawals': sum(t.amount for t in account_transactions if t.transaction_type in [Transaction.WITHDRAWAL, Transaction.TRANSFER_OUT])
        }
        
        return statement