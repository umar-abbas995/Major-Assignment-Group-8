"""
Main entry point for Bank Account System
Simple CLI interface for testing
"""

from account import BankAccount

def main():
    """Main function to run the banking system"""
    print("=" * 50)
    print("    BANK ACCOUNT HANDLING SYSTEM")
    print("=" * 50)
    
    # Test account creation
    print("\n[1] Creating a test account...")
    account1 = BankAccount("John Doe", "ACC001", 1000.00)
    print(f"Account created for: {account1.account_holder}")
    print(f"Account Number: {account1.account_number}")
    print(f"Initial Balance: ${account1.get_balance():.2f}")
    
    # Test deposit
    print("\n[2] Testing deposit...")
    success, message = account1.deposit(500.00)
    print(f"Deposit: {message}")
    print(f"New Balance: ${account1.get_balance():.2f}")
    
    # Test withdrawal
    print("\n[3] Testing withdrawal...")
    success, message = account1.withdraw(200.00)
    print(f"Withdrawal: {message}")
    print(f"New Balance: ${account1.get_balance():.2f}")
    
    # Show transaction history
    print("\n[4] Transaction History:")
    for transaction in account1.get_transaction_history():
        print(f"  - {transaction}")
    
    # Show account info
    print("\n[5] Account Summary:")
    info = account1.get_account_info()
    for key, value in info.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 50)
    print("       DAY 1 - BASIC STRUCTURE COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()