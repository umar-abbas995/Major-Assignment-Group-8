"""
Customer Module
Handles customer information and account management
"""

class Customer:
    """Represents a bank customer with personal information"""
    
    def _init_(self, customer_id, name, email, phone, address=""):
        """
        Initialize a new customer
        
        Args:
            customer_id (str): Unique customer identifier
            name (str): Full name of customer
            email (str): Email address
            phone (str): Phone number
            address (str): Physical address (optional)
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.accounts = []  # List of account numbers
        self.date_joined = datetime.now().strftime("%Y-%m-%d")
    
    def add_account(self, account_number):
        """Add an account to customer"""
        if account_number not in self.accounts:
            self.accounts.append(account_number)
            return True
        return False
    
    def remove_account(self, account_number):
        """Remove an account from customer"""
        if account_number in self.accounts:
            self.accounts.remove(account_number)
            return True
        return False
    
    def get_accounts(self):
        """Get all account numbers for this customer"""
        return self.accounts.copy()
    
    def get_customer_info(self):
        """Get customer information as dictionary"""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'total_accounts': len(self.accounts),
            'accounts': self.accounts,
            'date_joined': self.date_joined
        }
    
    def update_info(self, name=None, email=None, phone=None, address=None):
        """Update customer information"""
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        return True
    
    def _str_(self):
        """String representation of customer"""
        return f"Customer: {self.name} (ID: {self.customer_id}) - {len(self.accounts)} accounts"

class CustomerManager:
    """Manages collection of customers"""
    
    def _init_(self):
        self.customers = {}  # customer_id -> Customer object
    
    def add_customer(self, customer):
        """Add a customer to manager"""
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            return True
        return False
    
    def get_customer(self, customer_id):
        """Get customer by ID"""
        return self.customers.get(customer_id)
    
    def remove_customer(self, customer_id):
        """Remove customer by ID"""
        if customer_id in self.customers:
            del self.customers[customer_id]
            return True
        return False
    
    def find_customer_by_account(self, account_number):
        """Find customer who owns an account"""
        for customer in self.customers.values():
            if account_number in customer.accounts:
                return customer
        return None
    
    def find_customer_by_email(self, email):
        """Find customer by email"""
        for customer in self.customers.values():
            if customer.email == email:
                return customer
        return None
    
    def get_all_customers(self):
        """Get all customers"""
        return list(self.customers.values())
    
    def get_customer_count(self):
        """Get total number of customers"""
        return len(self.customers)
    
    def generate_customer_report(self):
        """Generate summary report of all customers"""
        report = {
            'total_customers': self.get_customer_count(),
            'customers': [],
            'total_accounts': 0
        }
        
        for customer in self.customers.values():
            customer_info = customer.get_customer_info()
            report['customers'].append(customer_info)
            report['total_accounts'] += len(customer.accounts)
        
        return report