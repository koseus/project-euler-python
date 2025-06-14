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
    for i in range(3, sqrt_n, 2):  # only odd divisors
        if n % i == 0:
            return False
    return True
