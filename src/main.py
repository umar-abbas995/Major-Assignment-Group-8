"""
Main Bank System - Integrated Version
"""

from account import BankAccount
from transaction import Transaction, TransactionManager
from customer import Customer, CustomerManager
from validation import Validation

def main():
    """Main function demonstrating all integrated features"""
    
    print("=" * 70)
    print("              BANK ACCOUNT MANAGEMENT SYSTEM")
    print("                    DAY 2 - ALL MODULES INTEGRATED")
    print("=" * 70)
    
    # Initialize managers
    print("\nInitializing system components...")
    transaction_manager = TransactionManager()
    customer_manager = CustomerManager()
    
    print("✓ Transaction Manager initialized")
    print("✓ Customer Manager initialized")
    print("✓ Validation module loaded")
    
    print("\n" + "-" * 70)
    print("TEST SCENARIO: Complete Customer Journey")
    print("-" * 70)
    
    # Step 1: Customer Registration
    print("\n[1] CUSTOMER REGISTRATION")
    print("-" * 40)
    
    # Validate customer data
    name = "Ali Ahmed"
    email = "ali.ahmed@email.com"
    phone = "03001234567"
    
    print(f"Validating customer data:")
    print(f"  Name '{name}': {Validation.validate_name(name)}")
    print(f"  Email '{email}': {Validation.validate_email(email)}")
    print(f"  Phone '{phone}': {Validation.validate_phone(phone)}")
    
    # Create customer
    customer = Customer("CUST001", name, email, phone, "123 Main Street")
    customer_manager.add_customer(customer)
    print(f"✓ Customer created: {customer.name} (ID: {customer.customer_id})")
    
    # Step 2: Account Creation
    print("\n[2] ACCOUNT CREATION")
    print("-" * 40)
    
    account = BankAccount(customer.name, "ACC001", 5000.00)
    customer.add_account("ACC001")
    print(f"✓ Account created: {account.account_number}")
    print(f"  Account Holder: {account.account_holder}")
    print(f"  Initial Balance: ${account.get_balance():.2f}")
    
    # Step 3: Transactions
    print("\n[3] TRANSACTION PROCESSING")
    print("-" * 40)
    
    transactions = [
        ("DEPOSIT", 2000.00, "Salary credit"),
        ("WITHDRAWAL", 1000.00, "ATM withdrawal"),
        ("DEPOSIT", 500.00, "Cash deposit"),
        ("WITHDRAWAL", 1500.00, "Utility bill payment")
    ]
    
    for trans_type, amount, desc in transactions:
        if trans_type == "DEPOSIT":
            success, message = account.deposit(amount)
        else:
            success, message = account.withdraw(amount)
        
        if success:
            # Get the last transaction and add to manager
            trans_list = account.get_transaction_history()
            if trans_list:
                transaction_manager.add_transaction(trans_list[-1])
            print(f"✓ {trans_type}: ${amount:.2f} - {desc}")
        else:
            print(f"✗ {trans_type} failed: {message}")
    
    print(f"\n  Final Balance: ${account.get_balance():.2f}")
    
    # Step 4: Account Statement
    print("\n[4] ACCOUNT STATEMENT")
    print("-" * 40)
    
    statement = transaction_manager.get_statement("ACC001")
    print(f"Account: {statement['account_number']}")
    print(f"Total Transactions: {statement['total_transactions']}")
    print(f"Total Deposits: ${statement['total_deposits']:.2f}")
    print(f"Total Withdrawals: ${statement['total_withdrawals']:.2f}")
    
    print("\nRecent Transactions:")
    for i, trans in enumerate(statement['transactions'][-3:], 1):
        print(f"  {i}. [{trans['timestamp']}] {trans['type']}: ${trans['amount']:.2f}")
    
    # Step 5: System Report
    print("\n[5] SYSTEM REPORT")
    print("-" * 40)
    
    report = customer_manager.generate_customer_report()
    print(f"Total Customers: {report['total_customers']}")
    print(f"Total Accounts: {report['total_accounts']}")
    
    # Validation Demo
    print("\n[6] VALIDATION DEMONSTRATION")
    print("-" * 40)
    
    test_cases = [
        ("Amount", "abc", Validation.validate_amount),
        ("Amount", "-100", Validation.validate_amount),
        ("Amount", "100.50", Validation.validate_amount),
        ("Account", "ACC123", Validation.validate_account_number),
        ("Email", "invalid-email", Validation.validate_email)
    ]
    
    for field, value, validator in test_cases:
        result = validator(value)
        status = "✓" if result[0] else "✗"
        print(f"  {status} {field} '{value}': {result[1]}")
    
    print("\n" + "=" * 70)
    print("              DAY 2 DEVELOPMENT COMPLETED!")
    print("=" * 70)
    
    print("\nSummary:")
    print("- Customer module: Complete")
    print("- Transaction module: Complete")
    print("- Validation module: Complete")
    print("- Integration: Complete")
    print("\nReady for Day 3: File storage and advanced features!")

if __name__ == "__main__":
    main()