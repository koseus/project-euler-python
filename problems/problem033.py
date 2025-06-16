def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def solve():
    """
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """
    fractions = []
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if is_curious(a, b):
                fractions.append((a, b))
    
    # Initialize product numerator and denominator
    product_num = 1
    product_den = 1
    
    # Multiply all fractions
    for a, b in fractions:
        product_num *= a
        product_den *= b
    
    # Reduce to lowest terms
    common_divisor = gcd(product_num, product_den)
    return product_den // common_divisor

def is_curious(a, b):
    """
    Check if a fraction a/b is a curious fraction.
    A curious fraction is one where cancelling a common digit in numerator and denominator
    gives the correct simplified fraction.
    
    Args:
        a: numerator (two-digit number)
        b: denominator (two-digit number)
    
    Returns:
        bool: True if the fraction is curious, False otherwise
    """
    # Skip trivial cases where either number ends in 0
    if a % 10 == 0 or b % 10 == 0:
        return False
    
    # Convert numbers to strings for digit comparison
    a_str = str(a)
    b_str = str(b)
    
    # Case 1: First digits match (e.g., 49/98)
    if a_str[0] == b_str[0]:
        return a / b == int(a_str[1]) / int(b_str[1])
    
    # Case 2: First digit of a matches second digit of b (e.g., 26/65)
    if a_str[0] == b_str[1]:
        return a / b == int(a_str[1]) / int(b_str[0])
    
    # Case 3: Second digit of a matches first digit of b (e.g., 16/64)
    if a_str[1] == b_str[0]:
        return a / b == int(a_str[0]) / int(b_str[1])
    
    return False
