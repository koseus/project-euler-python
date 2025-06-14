from utils.math_helpers import is_prime

def solve():
    """
    Find the sum of all the primes below two million.
    """
    return sum(i for i in range(2, 2000000) if is_prime(i))
