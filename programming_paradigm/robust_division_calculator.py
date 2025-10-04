import sys
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        return f'The result of the division is {num / den}'
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."