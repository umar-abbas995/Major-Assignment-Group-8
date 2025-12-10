import tkinter as tk
from tkinter import messagebox, ttk
from account import BankAccount   # your existing class

class BankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account System")
        self.root.geometry("450x500")

        self.account = None
        
        self.create_account_screen()

    # ---------------- Create Account Screen ----------------
    def create_account_screen(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Create Bank Account", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Full Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(frame, width=30)
        self.name_entry.grid(row=1, column=1)

        tk.Label(frame, text="Account Number:").grid(row=2, column=0, sticky="w")
        self.acc_entry = tk.Entry(frame, width=30)
        self.acc_entry.grid(row=2, column=1)

        tk.Label(frame, text="Initial Balance:").grid(row=3, column=0, sticky="w")
        self.balance_entry = tk.Entry(frame, width=30)
        self.balance_entry.grid(row=3, column=1)

        tk.Button(frame, text="Create Account", command=self.create_account).grid(row=4, column=0, columnspan=2, pady=15)

    def create_account(self):
        try:
            name = self.name_entry.get()
            acc_num = self.acc_entry.get()
            balance = float(self.balance_entry.get())

            if balance < 0:
                messagebox.showerror("Error", "Balance cannot be negative")
                return

            self.account = BankAccount(name, acc_num, balance)
            messagebox.showinfo("Success", f"Account created for {name}!")

            self.show_main_menu()

        except ValueError:
            messagebox.showerror("Error", "Invalid balance amount")

    # ---------------- Main Menu Screen ----------------
    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bank Account System", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Deposit", width=30, command=self.deposit_window).pack(pady=5)
        tk.Button(self.root, text="Withdraw", width=30, command=self.withdraw_window).pack(pady=5)
        tk.Button(self.root, text="Show Balance", width=30, command=self.show_balance).pack(pady=5)
        tk.Button(self.root, text="Transaction History", width=30, command=self.show_transactions).pack(pady=5)
        tk.Button(self.root, text="Account Summary", width=30, command=self.account_summary).pack(pady=5)

    # ---------------- Deposit ----------------
    def deposit_window(self):
        win = tk.Toplevel(self.root)
        win.title("Deposit")
        win.geometry("300x200")

        tk.Label(win, text="Enter amount to deposit:").pack(pady=10)
        amount_entry = tk.Entry(win)
        amount_entry.pack()

        def deposit_action():
            try:
                amount = float(amount_entry.get())
                success, msg = self.account.deposit(amount)
                messagebox.showinfo("Deposit", msg)
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")

        tk.Button(win, text="Deposit", command=deposit_action).pack(pady=10)

    # ---------------- Withdraw ----------------
    def withdraw_window(self):
        win = tk.Toplevel(self.root)
        win.title("Withdraw")
        win.geometry("300x200")

        tk.Label(win, text="Enter amount to withdraw:").pack(pady=10)
        amount_entry = tk.Entry(win)
        amount_entry.pack()

        def withdraw_action():
            try:
                amount = float(amount_entry.get())
                success, msg = self.account.withdraw(amount)
                messagebox.showinfo("Withdraw", msg)
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")

        tk.Button(win, text="Withdraw", command=withdraw_action).pack(pady=10)

    # ---------------- Show Balance ----------------
    def show_balance(self):
        messagebox.showinfo("Balance", f"Current Balance: ${self.account.get_balance():.2f}")

    # ---------------- Transaction History ----------------
    def show_transactions(self):
        win = tk.Toplevel(self.root)
        win.title("Transaction History")
        win.geometry("400x300")

        tk.Label(win, text="Transaction History", font=("Arial", 14)).pack(pady=10)

        text_box = tk.Text(win, width=45, height=12)
        text_box.pack()

        for t in self.account.get_transaction_history():
            text_box.insert(tk.END, f"{t}\n")

    # ---------------- Account Summary ----------------
    def account_summary(self):
        info = self.account.get_account_info()

        summary = "\n".join([f"{k.title()}: {v}" for k, v in info.items() if k != "transactions"])

        messagebox.showinfo("Account Summary", summary)


# ---------------- Run GUI ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()
