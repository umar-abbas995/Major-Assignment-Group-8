from transaction import Transaction
def deposit(self, amount):
    """Deposit money into account"""
    if amount > 0:
        self.balance += amount
        # Create transaction record
        transaction = Transaction(
            transaction_type=Transaction.DEPOSIT,
            amount=amount,
            account_number=self.account_number,
            description="Cash deposit"
        )
        self.transactions.append(transaction)
        return True, f"Deposited ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"
    return False, "Deposit amount must be positive!"

def withdraw(self, amount):
    """Withdraw money from account"""
    if amount <= 0:
        return False, "Withdrawal amount must be positive!"
    if amount > self.balance:
        return False, "Insufficient funds!"
    
    self.balance -= amount
    # Create transaction record
    transaction = Transaction(
        transaction_type=Transaction.WITHDRAWAL,
        amount=amount,
        account_number=self.account_number,
        description="Cash withdrawal"
    )
    self.transactions.append(transaction)
    return True, f"Withdrew ${amount:.2f} successfully! Transaction ID: {transaction.transaction_id}"