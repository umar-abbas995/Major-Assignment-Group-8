# account.py
from transaction import Transaction

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive!"
        self.balance += amount
        transaction = Transaction(
            transaction_type=Transaction.DEPOSIT,
            amount=amount,
            account_number=self.account_number,
            description="Cash deposit"
        )
        self.transactions.append(transaction)
        return True, f"Deposited ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive!"
        if amount > self.balance:
            return False, "Insufficient funds!"
        self.balance -= amount
        transaction = Transaction(
            transaction_type=Transaction.WITHDRAWAL,
            amount=amount,
            account_number=self.account_number,
            description="Cash withdrawal"
        )
        self.transactions.append(transaction)
        return True, f"Withdrew ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions.copy()

    def get_account_info(self):
        return {
            "holder": self.account_holder,
            "account_number": self.account_number,
            "balance": self.balance,
            "transactions": [str(t) for t in self.transactions]
        }
