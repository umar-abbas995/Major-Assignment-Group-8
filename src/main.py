import tkinter as tk
from tkinter import messagebox, ttk
from account import BankAccount
from customer import Customer, CustomerManager
from validation import Validation
import re

class BankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account System")
        self.root.geometry("500x550")
        
        self.customer_manager = CustomerManager()
        self.current_customer = None
        self.current_account = None
        
        self.show_welcome_screen()
    
    def show_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="🏦 Bank Account System", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Welcome to Secure Banking", font=("Arial", 12)).pack(pady=5)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=30)
        
        tk.Button(frame, text="Create New Account", width=25, height=2, 
                  command=self.create_account_screen, bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame, text="Login to Account", width=25, height=2, 
                  command=self.login_screen, bg="lightgreen").grid(row=0, column=1, padx=10, pady=10)
    
    # ---------------- CREATE ACCOUNT SCREEN ----------------
    def create_account_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        tk.Label(frame, text="Create New Account", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Customer Information
        tk.Label(frame, text="Full Name:", anchor="w").grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(frame, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="Email:", anchor="w").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(frame, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="Phone:", anchor="w").grid(row=3, column=0, sticky="w", pady=5)
        self.phone_entry = tk.Entry(frame, width=30)
        self.phone_entry.grid(row=3, column=1, pady=5)
        
        tk.Label(frame, text="Address:", anchor="w").grid(row=4, column=0, sticky="w", pady=5)
        self.address_entry = tk.Entry(frame, width=30)
        self.address_entry.grid(row=4, column=1, pady=5)
        
        # Account Information
        tk.Label(frame, text="Account Number (ACC001-ACC999):", anchor="w").grid(row=5, column=0, sticky="w", pady=5)
        self.acc_entry = tk.Entry(frame, width=30)
        self.acc_entry.grid(row=5, column=1, pady=5)
        
        tk.Label(frame, text="Initial Balance:", anchor="w").grid(row=6, column=0, sticky="w", pady=5)
        self.balance_entry = tk.Entry(frame, width=30)
        self.balance_entry.grid(row=6, column=1, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Create Account", command=self.create_account, bg="lightblue", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back", command=self.show_welcome_screen, width=15).pack(side=tk.LEFT, padx=5)
    
    def create_account(self):
        try:
            # Get inputs
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            address = self.address_entry.get()
            acc_num = self.acc_entry.get()
            balance_str = self.balance_entry.get()
            
            # Validate inputs - FIXED: Use 3 return values
            valid_name, name_msg, cleaned_name = Validation.validate_name(name)
            if not valid_name:
                messagebox.showerror("Error", name_msg)
                return
            name = cleaned_name
                
            valid_email, email_msg, cleaned_email = Validation.validate_email(email)
            if not valid_email:
                messagebox.showerror("Error", email_msg)
                return
            email = cleaned_email
                
            valid_acc, acc_msg, cleaned_acc = Validation.validate_account_number(acc_num)
            if not valid_acc:
                messagebox.showerror("Error", acc_msg)
                return
            acc_num = cleaned_acc
                
            valid_balance, balance_msg, balance = Validation.validate_amount(balance_str)
            if not valid_balance:
                messagebox.showerror("Error", balance_msg)
                return
            
            # Validate phone (optional, as per your validation requires 10 digits)
            valid_phone, phone_msg, cleaned_phone = Validation.validate_phone(phone)
            if not valid_phone:
                # Show warning but continue (phone validation is strict)
                response = messagebox.askyesno("Phone Warning", 
                    f"{phone_msg}\nDo you want to continue anyway?")
                if not response:
                    return
            
            # Create customer
            customer_id = f"CUST{len(self.customer_manager.customers)+1:03d}"
            customer = Customer(customer_id, name, email, phone, address)
            
            # Add account to customer
            customer.add_account(acc_num)
            
            # Add to customer manager
            self.customer_manager.add_customer(customer)
            
            # Create bank account
            self.current_account = BankAccount(name, acc_num, balance)
            self.current_customer = customer
            
            messagebox.showinfo("Success", 
                f"Account created successfully!\n\n"
                f"Customer ID: {customer_id}\n"
                f"Account: {acc_num}\n"
                f"Balance: ${balance:.2f}")
            
            self.show_main_menu()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {str(e)}")
    
    # ---------------- LOGIN SCREEN ----------------
    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=40)
        
        tk.Label(frame, text="Login to Account", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="Account Number:").grid(row=1, column=0, sticky="w", pady=5)
        self.login_acc_entry = tk.Entry(frame, width=30)
        self.login_acc_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="Customer Name:").grid(row=2, column=0, sticky="w", pady=5)
        self.login_name_entry = tk.Entry(frame, width=30)
        self.login_name_entry.grid(row=2, column=1, pady=5)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Login", command=self.login, bg="lightgreen", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back", command=self.show_welcome_screen, width=15).pack(side=tk.LEFT, padx=5)
    
    def login(self):
        acc_num = self.login_acc_entry.get()
        name = self.login_name_entry.get()
        
        # Find customer by account
        customer = self.customer_manager.find_customer_by_account(acc_num)
        
        if customer and customer.name == name:
            # Create account object for logged in customer
            self.current_customer = customer
            self.current_account = BankAccount(customer.name, acc_num, 1000.00)  # Default balance
            messagebox.showinfo("Success", f"Welcome back, {customer.name}!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or name")
    
    # ---------------- MAIN MENU ----------------
    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text=f"Welcome, {self.current_customer.name}", 
                 font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Account: {self.current_account.account_number} | "
                 f"Balance: ${self.current_account.get_balance():.2f}",
                 font=("Arial", 10)).pack(pady=5)
        
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=20)
        
        buttons = [
            ("💵 Deposit", self.deposit_window),
            ("💰 Withdraw", self.withdraw_window),
            ("📊 Show Balance", self.show_balance),
            ("📋 Transaction History", self.show_transactions),
            ("👤 Account Summary", self.account_summary),
            ("🚪 Logout", self.show_welcome_screen)
        ]
        
        for i, (text, command) in enumerate(buttons):
            tk.Button(menu_frame, text=text, width=25, height=2, 
                      command=command, bg="lightgray").grid(row=i//2, column=i%2, padx=10, pady=10)
    
    # ---------------- DEPOSIT WINDOW ----------------
    def deposit_window(self):
        win = tk.Toplevel(self.root)
        win.title("Deposit Money")
        win.geometry("400x200")
        
        tk.Label(win, text="Deposit Money", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Account Info
        info_frame = tk.Frame(win)
        info_frame.pack(pady=5)
        tk.Label(info_frame, text=f"Account: {self.current_account.account_number}").pack()
        
        # Amount Entry
        tk.Label(win, text="Enter amount to deposit:").pack(pady=5)
        amount_entry = tk.Entry(win, width=20, font=("Arial", 12))
        amount_entry.pack(pady=5)
        
        def deposit_action():
            try:
                amount = float(amount_entry.get())
                
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    return
                
                success, msg = self.current_account.deposit(amount)
                if success:
                    messagebox.showinfo("Success", msg)
                    win.destroy()
                    self.show_main_menu()  # Refresh balance display
                else:
                    messagebox.showerror("Error", msg)
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")
        
        button_frame = tk.Frame(win)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Deposit", command=deposit_action, bg="lightgreen", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=win.destroy, width=15).pack(side=tk.LEFT, padx=5)
    
    # ---------------- WITHDRAW WINDOW ----------------
    def withdraw_window(self):
        win = tk.Toplevel(self.root)
        win.title("Withdraw Money")
        win.geometry("400x200")
        
        tk.Label(win, text="Withdraw Money", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Account Info
        info_frame = tk.Frame(win)
        info_frame.pack(pady=5)
        tk.Label(info_frame, text=f"Account: {self.current_account.account_number}").pack()
        tk.Label(info_frame, text=f"Available: ${self.current_account.get_balance():.2f}").pack()
        
        # Amount Entry
        tk.Label(win, text="Enter amount to withdraw:").pack(pady=5)
        amount_entry = tk.Entry(win, width=20, font=("Arial", 12))
        amount_entry.pack(pady=5)
        
        def withdraw_action():
            try:
                amount = float(amount_entry.get())
                
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    return
                
                success, msg = self.current_account.withdraw(amount)
                if success:
                    messagebox.showinfo("Success", msg)
                    win.destroy()
                    self.show_main_menu()  # Refresh balance display
                else:
                    messagebox.showerror("Error", msg)
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")
        
        button_frame = tk.Frame(win)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Withdraw", command=withdraw_action, bg="lightcoral", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=win.destroy, width=15).pack(side=tk.LEFT, padx=5)
    
    # ---------------- SHOW BALANCE ----------------
    def show_balance(self):
        messagebox.showinfo("Account Balance", 
            f"Account: {self.current_account.account_number}\n"
            f"Holder: {self.current_account.account_holder}\n"
            f"Current Balance: ${self.current_account.get_balance():.2f}")
    
    # ---------------- TRANSACTION HISTORY ----------------
    def show_transactions(self):
        win = tk.Toplevel(self.root)
        win.title("Transaction History")
        win.geometry("600x400")
        
        tk.Label(win, text=f"Transaction History - {self.current_account.account_number}", 
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Create a frame with scrollbar
        frame = tk.Frame(win)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create text widget
        text_box = tk.Text(frame, height=15, width=70, yscrollcommand=scrollbar.set,
                          font=("Courier", 10))
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_box.yview)
        
        # Header
        header = f"{'Date':<20} {'Type':<12} {'Amount':>10} {'Description':<30} {'ID':<10}\n"
        text_box.insert(tk.END, header)
        text_box.insert(tk.END, "-"*85 + "\n")
        
        # Transactions
        transactions = self.current_account.get_transaction_history()
        
        if not transactions:
            text_box.insert(tk.END, "No transactions found.\n")
        else:
            for t in transactions:
                # Format transaction display
                trans_line = f"{t.date:<20} {t.transaction_type:<12} ${t.amount:>9.2f} {t.description:<30} {t.transaction_id[:8]}...\n"
                text_box.insert(tk.END, trans_line)
        
        text_box.config(state=tk.DISABLED)  # Make read-only
        
        # Summary
        summary_frame = tk.Frame(win)
        summary_frame.pack(pady=10)
        tk.Label(summary_frame, text=f"Total Transactions: {len(transactions)}", 
                 font=("Arial", 10)).pack()
    
    # ---------------- ACCOUNT SUMMARY ----------------
    def account_summary(self):
        account_info = self.current_account.get_account_info()
        customer_info = self.current_customer.get_customer_info()
        
        summary = (
            f"📋 ACCOUNT SUMMARY\n"
            f"{'='*40}\n"
            f"Customer Information:\n"
            f"  Name: {customer_info['name']}\n"
            f"  ID: {customer_info['customer_id']}\n"
            f"  Email: {customer_info['email']}\n"
            f"  Phone: {customer_info['phone']}\n"
            f"  Joined: {customer_info['date_joined']}\n\n"
            f"Account Information:\n"
            f"  Account Number: {account_info['account_number']}\n"
            f"  Current Balance: ${account_info['balance']:.2f}\n"
            f"  Total Accounts: {customer_info['total_accounts']}\n\n"
            f"Transaction Summary:\n"
            f"  Total Transactions: {len(account_info['transactions'])}\n"
            f"{'='*40}"
        )
        
        messagebox.showinfo("Account Summary", summary)


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()