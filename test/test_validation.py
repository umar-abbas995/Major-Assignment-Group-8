"""
Test cases for validation module
"""

from validation import Validation

def test_validation():
    """Run validation tests"""
    
    print("Testing Validation Module...")
    print("-" * 40)
    
    # Test amount validation
    print("1. Amount Validation:")
    print(f"   Valid amount 100.50: {Validation.validate_amount('100.50')}")
    print(f"   Negative amount: {Validation.validate_amount('-50')}")
    print(f"   Invalid input: {Validation.validate_amount('abc')}")
    
    # Test account number
    print("\n2. Account Number Validation:")
    print(f"   Valid ACC001: {Validation.validate_account_number('ACC001')}")
    print(f"   Invalid AC001: {Validation.validate_account_number('AC001')}")
    
    # Test email
    print("\n3. Email Validation:")
    print(f"   Valid email: {Validation.validate_email('test@example.com')}")
    print(f"   Invalid email: {Validation.validate_email('test@')}")
    
    print("\n" + "=" * 40)
    print("Validation tests completed!")

if __name__ == "_main_":
    test_validation()