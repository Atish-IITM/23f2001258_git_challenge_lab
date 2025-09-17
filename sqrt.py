# sqrt.py
def square_root(x):
    """Calculatea the square root of a non-negetive number."""
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return x ** 0.5
