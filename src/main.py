from account import BankAccount

def display_menu():
    print("\n=== Bank Account System ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

def main():
    accounts = {}
    
    while True:
        display_menu()
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            # Account creation logic
            name = input("Enter account holder name: ")
            acc_num = input("Enter account number: ")
            accounts[acc_num] = BankAccount(name, acc_num)
            print("Account created successfully!")
        
        elif choice == '2':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            if accounts[acc_num].deposit(amount):
                print("Deposit successful!")
        
        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            if accounts[acc_num].withdraw(amount):
                print("Withdrawal successful!")
        
        elif choice == '4':
            acc_num = input("Enter account number: ")
            print(f"Balance: ${accounts[acc_num].get_balance()}")
        
        elif choice == '5':
            acc_num = input("Enter account number: ")
            history = accounts[acc_num].get_transaction_history()
            for trans in history:
                print(trans)
        
        elif choice == '6':
            print("Thank you for banking with us!")
            break

if __name__ == "__main__":
    main()