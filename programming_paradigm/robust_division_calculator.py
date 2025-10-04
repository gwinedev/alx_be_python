import sys
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both inputs must be valid numeric values (integers or decimals)."
    
    try:
        return num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
print(safe_divide(10, 5))
print(safe_divide(10, 0))
print(safe_divide("ten", 5))