# main.py
from account import BankAccount

def main():
    print("=" * 50)
    print("       BANK ACCOUNT SYSTEM")
    print("=" * 50)

    # Ask user for account creation details
    name = input("Enter your full name: ")
    account_number = input("Enter account number: ")
    
    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    account = BankAccount(name, account_number, initial_balance)
    print(f"\nAccount created for {account.account_holder} with balance ${account.get_balance():.2f}\n")

    # Main loop
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Transaction History")
        print("5. Account Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                success, message = account.deposit(amount)
                print(message)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                success, message = account.withdraw(amount)
                print(message)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            print(f"Current Balance: ${account.get_balance():.2f}")

        elif choice == "4":
            print("Transaction History:")
            for t in account.get_transaction_history():
                print(f"  - {t}")

        elif choice == "5":
            info = account.get_account_info()
            print("Account Summary:")
            for key, value in info.items():
                if key != "transactions":
                    print(f"  {key.title()}: {value}")

        elif choice == "6":
            print("Exiting... Thank you for using the Bank Account System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
 