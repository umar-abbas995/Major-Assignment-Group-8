# account.py
from transaction import Transaction

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        
        # Add initial transaction for account creation
        transaction = Transaction(
            transaction_type="ACCOUNT_CREATION",
            amount=balance,
            account_number=account_number,
            description="Account opened with initial deposit"
        )
        self.transactions.append(transaction)

    def deposit(self, amount, description="Cash deposit"):
        if amount <= 0:
            return False, "Deposit amount must be positive!"
        
        self.balance += amount
        transaction = Transaction(
            transaction_type=Transaction.DEPOSIT,
            amount=amount,
            account_number=self.account_number,
            description=description
        )
        self.transactions.append(transaction)
        return True, f"Deposited ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"

    def withdraw(self, amount, description="Cash withdrawal", method="ATM"):
        if amount <= 0:
            return False, "Withdrawal amount must be positive!"
        if amount > self.balance:
            return False, f"Insufficient funds! Available: ${self.balance:.2f}"
        
        self.balance -= amount
        transaction = Transaction(
            transaction_type=Transaction.WITHDRAWAL,
            amount=amount,
            account_number=self.account_number,
            description=f"{description} ({method})"
        )
        self.transactions.append(transaction)
        return True, f"Withdrew ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"

    def transfer(self, amount, to_account, description="Funds transfer"):
        """Transfer money to another account"""
        if amount <= 0:
            return False, "Transfer amount must be positive!"
        if amount > self.balance:
            return False, f"Insufficient funds for transfer! Available: ${self.balance:.2f}"
        
        # Create withdrawal transaction
        self.balance -= amount
        withdrawal_transaction = Transaction(
            transaction_type="TRANSFER_OUT",
            amount=amount,
            account_number=self.account_number,
            description=f"Transfer to {to_account}: {description}"
        )
        self.transactions.append(withdrawal_transaction)
        
        return True, f"Transfer of ${amount:.2f} to {to_account} initiated. Transaction ID: {withdrawal_transaction.transaction_id}"

    def get_balance(self):
        return self.balance

    def get_transaction_history(self, limit=None):
        """Get transaction history, optionally limited to recent N transactions"""
        if limit and limit > 0:
            return self.transactions[-limit:]
        return self.transactions.copy()

    def get_account_info(self):
        return {
            "holder": self.account_holder,
            "account_number": self.account_number,
            "balance": self.balance,
            "total_transactions": len(self.transactions),
            "transactions": [str(t) for t in self.transactions[-10:]]  # Last 10 transactions
        }
    
    def get_mini_statement(self, count=5):
        """Get mini statement with recent transactions"""
        recent = self.transactions[-count:] if len(self.transactions) >= count else self.transactions
        statement = f"Mini Statement for {self.account_number}\n"
        statement += "=" * 50 + "\n"
        for t in recent:
            statement += f"{t.date} | {t.transaction_type:15} | ${t.amount:8.2f} | {t.description}\n"
        statement += f"\nCurrent Balance: ${self.balance:.2f}"
        return statement