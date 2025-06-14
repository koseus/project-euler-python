def is_prime(n):
    """
    Check if a number is prime.
    Returns True if prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Compute the Greatest Common Divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Compute the Least Common Multiple of a and b.
    """
    return a * b // gcd(a, b)
