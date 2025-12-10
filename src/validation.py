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
            if '.' in str(amount):
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
        # Clean the input - remove spaces, convert to uppercase
        account_number = str(account_number).strip().upper()
        
        pattern = r'^ACC\d{3}$'
        
        if not re.match(pattern, account_number):
            return False, "Account number must be in format ACC001 (ACC followed by 3 digits)", None
        
        # Extract the number part and validate it's between 001-999
        num_part = account_number[3:]
        try:
            num_value = int(num_part)
            if num_value < 1 or num_value > 999:
                return False, "Account number must be between ACC001 and ACC999", None
        except ValueError:
            return False, "Account number must be in format ACC001 (ACC followed by 3 digits)", None
        
        return True, "Account number is valid", account_number
    
    @staticmethod
    def validate_customer_id(customer_id):
        """Validate customer ID format (CUST001)"""
        customer_id = str(customer_id).strip().upper()
        
        pattern = r'^CUST\d{3}$'
        
        if not re.match(pattern, customer_id):
            return False, "Customer ID must be in format CUST001 (CUST followed by 3 digits)", None
        
        # Validate the number part
        num_part = customer_id[4:]
        try:
            num_value = int(num_part)
            if num_value < 1 or num_value > 999:
                return False, "Customer ID must be between CUST001 and CUST999", None
        except ValueError:
            return False, "Customer ID must be in format CUST001 (CUST followed by 3 digits)", None
        
        return True, "Customer ID is valid", customer_id
    
    @staticmethod
    def validate_name(name):
        """Validate customer name"""
        name = str(name).strip()
        
        if not name or len(name) == 0:
            return False, "Name cannot be empty", None
        
        if len(name) > 100:
            return False, "Name is too long (max 100 characters)", None
        
        # Allow letters, spaces, hyphens, apostrophes, and periods
        if not re.match(r'^[A-Za-z\s\-\'\.]+$', name):
            return False, "Name can only contain letters, spaces, hyphens, and apostrophes", None
        
        return True, "Name is valid", name.title()
    
    @staticmethod
    def validate_email(email):
        """Validate email address"""
        email = str(email).strip().lower()
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(pattern, email):
            return False, "Invalid email format", None
        
        return True, "Email is valid", email
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number"""
        phone = str(phone).strip()
        
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)
        
        if len(digits) < 10 or len(digits) > 15:
            return False, "Phone number must be 10-15 digits", None
        
        return True, "Phone number is valid", digits
    
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
        password = str(password)
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters", None
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter", None
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter", None
        
        if not re.search(r'\d', password):
            return False, "Password must contain at least one digit", None
        
        return True, "Password is strong", password
    
    @staticmethod
    def validate_date(date_str, date_format="%Y-%m-%d"):
        """Validate date string"""
        date_str = str(date_str).strip()
        
        try:
            datetime.strptime(date_str, date_format)
            return True, "Date is valid", date_str
        except ValueError:
            return False, f"Date must be in format {date_format}", None
    
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
        trans_type = str(trans_type).strip().upper()
        
        valid_types = ['DEPOSIT', 'WITHDRAWAL', 'TRANSFER_IN', 'TRANSFER_OUT']
        
        if trans_type not in valid_types:
            return False, f"Transaction type must be one of: {', '.join(valid_types)}", None
        
        return True, "Transaction type is valid", trans_type

class ValidationError(Exception):
    """Custom exception for validation errors"""
    def _init_(self, message):
        super()._init_(message)
        self.message = message