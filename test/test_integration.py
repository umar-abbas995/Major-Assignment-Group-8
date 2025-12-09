"""
Integration test for all modules
"""

from src.account import BankAccount
from src.transaction import Transaction, TransactionManager
from src.customer import Customer, CustomerManager
from src.validation import Validation

def test_integration():
    """Test integration of all modules"""
    
    print("=" * 60)
    print("        BANK SYSTEM - INTEGRATION TEST")
    print("=" * 60)
    
    # Initialize managers
    transaction_manager = TransactionManager()
    customer_manager = CustomerManager()
    
    # Create a customer
    print("\n1. Creating customer...")
    customer = Customer("CUST001", "John Doe", "john@example.com", "1234567890")
    customer_manager.add_customer(customer)
    print(f"   Customer created: {customer}")
    
    # Create an account
    print("\n2. Creating bank account...")
    account = BankAccount("John Doe", "ACC001", 1000.00)
    customer.add_account("ACC001")
    print(f"   Account created: {account.account_number}")
    print(f"   Initial balance: ${account.get_balance():.2f}")
    
    # Perform transactions
    print("\n3. Performing transactions...")
    
    # Deposit
    success, message = account.deposit(500.00)
    print(f"   Deposit: {message}")
    
    # Withdrawal
    success, message = account.withdraw(200.00)
    print(f"   Withdrawal: {message}")
    
    # Add transactions to manager
    for transaction in account.get_transaction_history():
        transaction_manager.add_transaction(transaction)
    
    print(f"   Final balance: ${account.get_balance():.2f}")
    
    # Generate statement
    print("\n4. Generating account statement...")
    statement = transaction_manager.get_statement("ACC001")
    print(f"   Total transactions: {statement['total_transactions']}")
    print(f"   Total deposits: ${statement['total_deposits']:.2f}")
    print(f"   Total withdrawals: ${statement['total_withdrawals']:.2f}")
    
    # Test validation
    print("\n5. Testing validation...")
    print(f"   Validate amount '100.50': {Validation.validate_amount('100.50')}")
    print(f"   Validate account 'ACC001': {Validation.validate_account_number('ACC001')}")
    print(f"   Validate email: {Validation.validate_email('john@example.com')}")
    
    # Customer report
    print("\n6. Customer report...")
    report = customer_manager.generate_customer_report()
    print(f"   Total customers: {report['total_customers']}")
    print(f"   Total accounts: {report['total_accounts']}")
    
    print("\n" + "=" * 60)
    print("        INTEGRATION TEST COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    test_integration()
