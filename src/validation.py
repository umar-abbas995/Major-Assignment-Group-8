"""
Validation Module
Handles input validation and sanitization for banking system
"""

import re
from datetime import datetime

class Validation:
    """Collection of validation methods for banking system"""
    
    @staticmethod
    def validate_amount(amount_str):
        """
        Validate amount input
        
        Args:
            amount_str (str): Amount as string
            
        Returns:
            tuple: (success, message, amount)
        """
        try:
            amount = float(amount_str)
            
            if amount <= 0:
                return False, "Amount must be greater than zero", None
            
            if amount > 1000000:  # Limit to 1 million
                return False, "Amount exceeds maximum limit ($1,000,000)", None
            
            # Check for decimal places
            if len(str(amount).split('.')[-1]) > 2:
                return False, "Amount can have maximum 2 decimal places", None
            
            return True, "Amount is valid", round(amount, 2)
            
        except ValueError:
            return False, "Invalid amount format. Please enter a number", None
    
    @staticmethod
    def validate_account_number(account_number):
        """
        Validate account number format
        
        Rules: 
        - Must start with ACC
        - Followed by 3 digits
        - Example: ACC001
        """
        pattern = r'^ACC\d{3}$'
        
        if not re.match(pattern, account_number):
            return False, "Account number must be in format ACC001 (ACC followed by 3 digits)"
        
        return True, "Account number is valid"
    
    @staticmethod
    def validate_customer_id(customer_id):
        """Validate customer ID format (CUST001)"""
        pattern = r'^CUST\d{3}$'
        
        if not re.match(pattern, customer_id):
            return False, "Customer ID must be in format CUST001 (CUST followed by 3 digits)"
        
        return True, "Customer ID is valid"
    
    @staticmethod
    def validate_name(name):
        """Validate customer name"""
        if not name or len(name.strip()) == 0:
            return False, "Name cannot be empty"
        
        if len(name) > 100:
            return False, "Name is too long (max 100 characters)"
        
        # Allow letters, spaces, hyphens, and apostrophes
        if not re.match(r'^[A-Za-z\s\-\'\.]+$', name):
            return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
        
        return True, "Name is valid"
    
    @staticmethod
    def validate_email(email):
        """Validate email address"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(pattern, email):
            return False, "Invalid email format"
        
        return True, "Email is valid"
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number"""
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)
        
        if len(digits) < 10 or len(digits) > 15:
            return False, "Phone number must be 10-15 digits"
        
        return True, "Phone number is valid"
    
    @staticmethod
    def validate_password(password):
        """
        Validate password strength
        
        Requirements:
        - At least 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r'\d', password):
            return False, "Password must contain at least one digit"
        
        return True, "Password is strong"
    
    @staticmethod
    def validate_date(date_str, date_format="%Y-%m-%d"):
        """Validate date string"""
        try:
            datetime.strptime(date_str, date_format)
            return True, "Date is valid"
        except ValueError:
            return False, f"Date must be in format {date_format}"
    
    @staticmethod
    def sanitize_input(input_str):
        """Sanitize input string"""
        if not input_str:
            return ""
        
        # Remove leading/trailing whitespace
        sanitized = input_str.strip()
        
        # Replace multiple spaces with single space
        sanitized = re.sub(r'\s+', ' ', sanitized)
        
        # Remove potentially dangerous characters for SQL injection
        sanitized = re.sub(r'[;\'\"\\]', '', sanitized)
        
        return sanitized
    
    @staticmethod
    def validate_transaction_type(trans_type):
        """Validate transaction type"""
        valid_types = ['DEPOSIT', 'WITHDRAWAL', 'TRANSFER_IN', 'TRANSFER_OUT']
        
        if trans_type not in valid_types:
            return False, f"Transaction type must be one of: {', '.join(valid_types)}"
        
        return True, "Transaction type is valid"

class ValidationError(Exception):
    """Custom exception for validation errors"""
    def _init_(self, message):
        super()._init_(message)
        self.message = message