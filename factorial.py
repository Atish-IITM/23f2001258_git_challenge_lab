# factorial.py
def factorial(n):
    """Calculates the factorial of a non_negative integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(n, 0, -1):
        result *= i 
    return result 
