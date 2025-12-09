"""
Customer Module
Handles customer information and account management
"""

from datetime import datetime
from typing import List, Dict, Optional

class Customer:
    """Represents a bank customer with personal information"""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str = ""):
        """
        Initialize a new customer
        
        Args:
            customer_id (str): Unique customer identifier
            name (str): Full name of customer
            email (str): Email address
            phone (str): Phone number
            address (str): Physical address (optional)
        """
        self.customer_id: str = customer_id
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.address: str = address
        self.accounts: List[str] = []  # List of account numbers
        self.date_joined: str = datetime.now().strftime("%Y-%m-%d")
    
    def add_account(self, account_number: str) -> bool:
        """Add an account to customer"""
        if account_number not in self.accounts:
            self.accounts.append(account_number)
            return True
        return False
    
    def remove_account(self, account_number: str) -> bool:
        """Remove an account from customer"""
        if account_number in self.accounts:
            self.accounts.remove(account_number)
            return True
        return False
    
    def get_accounts(self) -> List[str]:
        """Get all account numbers for this customer"""
        return self.accounts.copy()
    
    def get_customer_info(self) -> Dict:
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
    
    def update_info(self, name: Optional[str] = None, email: Optional[str] = None,
                    phone: Optional[str] = None, address: Optional[str] = None) -> bool:
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
    
    def __str__(self) -> str:
        """String representation of customer"""
        return f"Customer: {self.name} (ID: {self.customer_id}) - {len(self.accounts)} accounts"

class CustomerManager:
    """Manages collection of customers"""
    
    def __init__(self):
        self.customers: Dict[str, Customer] = {}  # customer_id -> Customer object
    
    def add_customer(self, customer: Customer) -> bool:
        """Add a customer to manager"""
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            return True
        return False
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        return self.customers.get(customer_id)
    
    def remove_customer(self, customer_id: str) -> bool:
        """Remove customer by ID"""
        if customer_id in self.customers:
            del self.customers[customer_id]
            return True
        return False
    
    def find_customer_by_account(self, account_number: str) -> Optional[Customer]:
        """Find customer who owns an account"""
        for customer in self.customers.values():
            if account_number in customer.accounts:
                return customer
        return None
    
    def find_customer_by_email(self, email: str) -> Optional[Customer]:
        """Find customer by email"""
        for customer in self.customers.values():
            if customer.email == email:
                return customer
        return None
    
    def get_all_customers(self) -> List[Customer]:
        """Get all customers"""
        return list(self.customers.values())
    
    def get_customer_count(self) -> int:
        """Get total number of customers"""
        return len(self.customers)
    
    def generate_customer_report(self) -> Dict:
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
