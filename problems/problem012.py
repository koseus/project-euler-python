from utils.math_helpers import get_factors

def solve():
    """
    Find the first triangle number to have over five hundred divisors.
    """

    i = 1
    triangle_number = 1  # First triangle number
    
    while len(get_factors(triangle_number)) < 501:
        i += 1
        triangle_number += i  # Add next number to running sum
    return triangle_number

