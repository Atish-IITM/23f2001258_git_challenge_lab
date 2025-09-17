# divide.py
def divide(x, y):
    """Divide two numbers, with a special check for division by zero."""
    if y == 0:
        return "Error: Cannot divide by zero."
    return round(x / y, 5)
